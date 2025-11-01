import serial
import time
import argparse
import sys
import logging

# Thiết lập Logger để ghi log ra file và console
LOG_FILE = 'pm.log'
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE, mode='a'),  # Ghi vào file pm.log (mode 'a' để nối tiếp)
        logging.StreamHandler(sys.stdout)          # Ghi ra console
    ]
)
logger = logging.getLogger(__name__)

def calculate_checksum(data):
    """Tính toán Check-sum từ DATA 1 đến DATA 6."""
    # Tổng các byte từ index 2 đến index 7 (DATA 1 đến DATA 6)
    return sum(data[2:8]) & 0xFF

def parse_sds011_data(data):
    """
    Giải mã 10 byte dữ liệu từ cảm biến SDS011.
    Cấu trúc dữ liệu (từ bảng bạn cung cấp):
    0: AA (Message header)
    1: C0 (Commander No.)
    2: PM2.5 Low byte (DATA 1)
    3: PM2.5 High byte (DATA 2)
    4: PM10 Low byte (DATA 3)
    5: PM10 High byte (DATA 4)
    6: ID byte 1 (DATA 5)
    7: ID byte 2 (DATA 6)
    8: Check-sum
    9: AB (Message tail)
    """
    if len(data) != 10:
        return None, "Kích thước gói dữ liệu không hợp lệ."
    
    # 1. Kiểm tra Header và Tail
    if data[0] != 0xAA or data[1] != 0xC0 or data[9] != 0xAB:
        return None, "Header/Tail không khớp (AA C0 ... AB)."
    
    # 2. Kiểm tra Check-sum
    checksum_calculated = calculate_checksum(data)
    checksum_received = data[8]
    
    if checksum_calculated != checksum_received:
        return None, f"Check-sum lỗi. Nhận: {checksum_received:02X}, Tính: {checksum_calculated:02X}"

    # 3. Tính toán giá trị PM2.5 và PM10
    # Công thức: value = (High byte * 256 + Low byte) / 10
    
    # PM2.5: Low byte (index 2), High byte (index 3)
    pm25_raw = data[3] * 256 + data[2]
    pm25 = pm25_raw / 10.0
    
    # PM10: Low byte (index 4), High byte (index 5)
    pm10_raw = data[5] * 256 + data[4]
    pm10 = pm10_raw / 10.0
    
    # ID: ID byte 1 (index 6), ID byte 2 (index 7)
    sensor_id = f"{data[6]:02X}{data[7]:02X}"

    return {
        'PM2.5': pm25,
        'PM10': pm10,
        'ID': sensor_id
    }, "OK"

def read_sds011(port_name):
    """Đọc dữ liệu từ cổng COM và xử lý."""
    
    # Cấu hình giao tiếp nối tiếp cho SDS011 (thường là 9600, 8, N, 1)
    try:
        ser = serial.Serial(port=port_name, baudrate=9600, timeout=1)
        ser.flushInput() # Xóa buffer đầu vào
    except serial.SerialException as e:
        logger.error(f"Lỗi khi mở cổng COM {port_name}: {e}")
        return

    logger.info(f"Đang lắng nghe dữ liệu từ SDS011 trên cổng: {port_name}...")
    logger.info(f"Dữ liệu sẽ được ghi vào file: {LOG_FILE}")
    
    # Bắt đầu vòng lặp đọc dữ liệu
    while True:
        try:
            # Đọc 10 bytes dữ liệu. Vì SDS011 gửi liên tục, ta chỉ cần đọc gói 10 bytes.
            # Ta dùng ser.read() thay vì readline() vì dữ liệu là binary.
            data = ser.read(10)
            
            if data:
                # Chuyển đổi bytes thành list các integer (cho việc kiểm tra và tính toán)
                data_list = list(data)
                
                # Giải mã dữ liệu
                results, status = parse_sds011_data(data_list)
                
                if results:
                    log_message = f"PM2.5: {results['PM2.5']:.2f} µg/m³ | PM10: {results['PM10']:.2f} µg/m³ | ID: {results['ID']}"
                    logger.info(log_message)
                else:
                    logger.warning(f"Gói dữ liệu không hợp lệ: {status} - Dữ liệu thô: {data.hex().upper()}")
                    
            # Dừng 1 chút để không làm quá tải CPU và chờ gói dữ liệu tiếp theo
            time.sleep(1) 

        except serial.SerialTimeoutException:
            logger.warning("Hết thời gian chờ khi đọc dữ liệu.")
            time.sleep(1)
        except KeyboardInterrupt:
            logger.info("Chương trình dừng theo yêu cầu của người dùng.")
            break
        except Exception as e:
            logger.error(f"Lỗi không xác định: {e}")
            time.sleep(5)
            
    if 'ser' in locals() and ser.is_open:
        ser.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Đọc dữ liệu từ cảm biến SDS011 qua cổng COM và ghi log."
    )
    # Thêm đối số bắt buộc để nhận tên cổng COM
    parser.add_argument(
        "com_port", 
        type=str, 
        help="Tên cổng COM (ví dụ: COM3 trên Windows hoặc /dev/ttyUSB0 trên Linux)"
    )
    
    args = parser.parse_args()
    
    read_sds011(args.com_port)