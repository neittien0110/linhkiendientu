import streamlit as st
import serial
import time
import pandas as pd
import logging
import sys
import matplotlib.pyplot as plt

# --- Cấu hình Logger ---
# Ghi log vào file pm.log (như yêu cầu gốc)
LOG_FILE = 'pm.log'
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE, mode='a')
    ]
)
logger = logging.getLogger(__name__)

# --- Hàm Xử lý Dữ liệu ---

def calculate_checksum(data):
    """Tính toán Check-sum từ DATA 1 đến DATA 6."""
    # Tổng các byte từ index 2 đến index 7 (DATA 1 đến DATA 6)
    return sum(data[2:8]) & 0xFF

def parse_sds011_data(data):
    """Giải mã 10 byte dữ liệu từ cảm biến SDS011."""
    if len(data) != 10:
        return None
    
    # 1. Kiểm tra Header, Commander No. và Tail
    if data[0] != 0xAA or data[1] != 0xC0 or data[9] != 0xAB:
        return None
    
    # 2. Kiểm tra Check-sum
    checksum_calculated = calculate_checksum(data)
    checksum_received = data[8]
    
    if checksum_calculated != checksum_received:
        return None

    # 3. Tính toán giá trị PM2.5 và PM10
    # Công thức: value = (High byte * 256 + Low byte) / 10
    pm25_raw = data[3] * 256 + data[2]
    pm25 = pm25_raw / 10.0
    
    pm10_raw = data[5] * 256 + data[4]
    pm10 = pm10_raw / 10.0
    
    # 4. Trả về kết quả
    return {
        'time': pd.to_datetime(time.time(), unit='s'),
        'PM2.5': pm25,
        'PM10': pm10
    }

# --- Hàm Vẽ Đồ thị ---

def plot_with_thresholds(df):
    """
    Vẽ đồ thị PM2.5 và PM10 theo thời gian với các dải ngưỡng chất lượng không khí (AQI).
    Giới hạn trục Y (Y-axis) sẽ được điều chỉnh để tập trung vào dữ liệu hiện tại.
    """
    
    if df.empty:
        return None

    fig, ax = plt.subplots(figsize=(10, 5))
    
    # --- Định nghĩa Ngưỡng và Màu Sắc ---
    # Ngưỡng: (max_value, color, label)
    THRESHOLDS = [
        (25, 'green', 'Tốt (<= 25)'),
        (50, 'yellow', 'TB (26-50)'),
        (150, 'orange', 'Kém (51-150)'),
        (2000, 'red', 'Xấu (> 150)') # Dùng giá trị lớn để bao phủ
    ]
    
    # Tìm giá trị PM lớn nhất hiện tại (cả PM2.5 và PM10)
    current_max_pm = max(df['PM2.5'].max(), df['PM10'].max()) if not df.empty else 0
    
    # 1. Xác định giới hạn Y tối đa (ymax)
    # Lấy ngưỡng PM lớn nhất mà dữ liệu hiện tại đã chạm tới, sau đó làm tròn lên 5 hoặc 10
    
    ymax = 50 # Giá trị mặc định cho ngưỡng TB
    for max_pm, _, _ in THRESHOLDS:
        if current_max_pm <= max_pm:
            ymax = max_pm
            break
        elif current_max_pm > THRESHOLDS[-2][0]: # Nếu vượt ngưỡng Kém (150)
            ymax = current_max_pm * 1.2 # Tăng 20% so với giá trị max hiện tại
            break
            
    # Đảm bảo ymax tối thiểu là 50 để luôn hiển thị ngưỡng Vàng
    ymax = max(50, ymax) 
    
    # --- Vẽ các dải ngưỡng ---
    # Lặp lại THRESHOLDS để vẽ dải màu
    current_ymin = 0
    for max_value, color_name, label in THRESHOLDS:
        if current_ymin < ymax:
            # Chỉ vẽ các dải nằm trong giới hạn ymax
            draw_max = min(max_value, ymax)
            ax.axhspan(current_ymin, draw_max, color=color_name, alpha=0.1, label=label)
            current_ymin = max_value
        else:
            break # Dừng vẽ các dải vượt quá ymax

    # --- Vẽ Đường dữ liệu ---
    
    ax.plot(df['time'], df['PM2.5'], label='PM2.5 ($\mu g/m^3$)', color='blue', linewidth=2, marker='o', markersize=3)
    ax.plot(df['time'], df['PM10'], label='PM10 ($\mu g/m^3$)', color='red', linestyle='--', linewidth=1)

    # --- Định dạng Đồ thị ---
    
    ax.set_title('Dữ liệu PM2.5 và PM10 theo Thời gian với Ngưỡng')
    ax.set_xlabel('Thời gian')
    ax.set_ylabel('Nồng độ ($\mu g/m^3$)')
    ax.grid(axis='y', linestyle='--')
    ax.legend(loc='upper left')
    
    fig.autofmt_xdate()
    
    # Đặt giới hạn trục Y theo tính toán
    ax.set_ylim(bottom=0, top=ymax)
    
    plt.tight_layout()
    return fig

# --- Hàm Streamlit chính ---

st.title("🌬️ Giám sát Bụi NOVA SDS011")

# Sử dụng sys.platform để xác định hệ điều hành và cung cấp giá trị mặc định cho cổng COM
if sys.platform.startswith('win'):
    default_port = "COM3"
elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
    default_port = "/dev/ttyUSB0"
else:
    default_port = "/dev/ttyACM0" 

port_name = st.sidebar.text_input(
    "1. Nhập Cổng COM/Serial", 
    value=default_port
)

start_button = st.sidebar.button("2. Bắt đầu Đọc Dữ liệu")

# Khởi tạo DataFrame trong session state
if 'data_frame' not in st.session_state:
    st.session_state.data_frame = pd.DataFrame(columns=['time', 'PM2.5', 'PM10'])

# --- Vòng lặp đọc dữ liệu ---

if start_button:
    status_text = st.empty()
    status_text.info(f"Đang cố gắng kết nối với {port_name}...")
    
    try:
        # Kết nối cổng Serial
        ser = serial.Serial(port=port_name, baudrate=9600, timeout=1)
        ser.flushInput()
        status_text.success(f"Đã kết nối thành công với {port_name}. Đang đọc dữ liệu...")
        
        # Thiết lập vùng hiển thị giao diện
        st.subheader("📊 Dữ liệu Trực tiếp")
        latest_data_container = st.empty()
        
        st.subheader("📈 Đồ thị Cập nhật (200 điểm gần nhất)")
        chart_container = st.empty()
        
        st.subheader("📜 Bảng Dữ liệu Thô (10 dòng mới nhất)")
        table_container = st.empty()

        # Vòng lặp chính để đọc và cập nhật giao diện
        while True:
            data = ser.read(10)
            
            if data:
                data_list = list(data)
                results = parse_sds011_data(data_list)
                
                if results:
                    # 1. Ghi log vào file
                    log_message = f"PM2.5: {results['PM2.5']:.2f} µg/m³ | PM10: {results['PM10']:.2f} µg/m³"
                    logger.info(log_message)
                    
                    # 2. Cập nhật DataFrame
                    new_row = pd.DataFrame([results])
                    st.session_state.data_frame = pd.concat(
                        [st.session_state.data_frame, new_row], 
                        ignore_index=True
                    )
                    
                    # 3. Hiển thị dữ liệu mới nhất
                    latest_data_container.markdown(
                        f"""
                        **Thời gian:** {results['time'].strftime('%H:%M:%S')} | 
                        **PM2.5:** **<span style="color:blue">{results['PM2.5']:.2f} µg/m³</span>** | 
                        **PM10:** **<span style="color:red">{results['PM10']:.2f} µg/m³</span>**
                        """, 
                        unsafe_allow_html=True
                    )
                    
                    # 4. Vẽ đồ thị với các dải ngưỡng (sử dụng 200 điểm gần nhất)
                    df_to_plot = st.session_state.data_frame.tail(200)
                    fig = plot_with_thresholds(df_to_plot)
                    chart_container.pyplot(fig, clear_figure=True)
                    
                    # 5. Cập nhật bảng dữ liệu
                    table_container.dataframe(st.session_state.data_frame.tail(10))
                else:
                    # Bỏ qua gói dữ liệu lỗi (checksum hoặc header/tail sai)
                    pass
                    
            time.sleep(1) # Đọc sau mỗi 1 giây

    except serial.SerialException as e:
        status_text.error(f"Lỗi kết nối cổng COM: {e}. Vui lòng kiểm tra tên cổng và đảm bảo cảm biến được cắm.")
    except Exception as e:
        status_text.error(f"Lỗi không xác định: {e}")

# Hiển thị hướng dẫn khi chưa bấm nút Start
if not start_button:
    st.info("Nhập tên cổng COM và bấm 'Bắt đầu Đọc Dữ liệu' để xem kết quả theo thời gian thực.")