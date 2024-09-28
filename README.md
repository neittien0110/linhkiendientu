# LINH KIỆN ĐIỆN TỬ

## Mục lục

- [Góc, gia tốc, la bàn](#mpu)
- [Nhịp tim và SpO2](#nhịp-tim-và-spo2)
- [Phím bấm, bàn phim](#bàn-phím)
- [Đo khoảng cách](#đo-khoảng-cách)
- [Loa, còi](#loa-còi)
- [Nhiệt độ Độ ẩm](#nhiệt-độ-độ-ẩm)
- [Tia UV](#tia-uv)
- [Khác](#khác)

Và tham chiếu tới các trang khác:
1. [Các shield mở rộng cho board dạng D1 mini](./D1mini.md)
2. [Các loại motor](./Motors.md)
3. [Các module truyền thông](./Communications.md)
4. [Các màn hình hiển thị](./Screens.md)
5. [Các linh vật tư phụ kiện như mạch in, dây dẫn, thiếc](./noname.md)
6. [Linh kiện PCB để thiết kế board](./EasyEDA_Library.md)
7. [Mạch sạc pin Lithium](https://neittien0110.github.io/linhkiendientu/EasyEDA_Library.html#m%E1%BA%A1ch-s%E1%BA%A1c)
8. [Module nguồn cấp](./powersupply.md)

## MPU

-  MPU**9250** / MPU**6500** / \
  ![20240218_095519](https://github.com/neittien0110/linhkiendientu/assets/8079397/14b33c4d-9f34-4473-ab0b-366a25a4f8c2)

- [Mua MPU 6500, mặc dù tên là 9250, nhưng thực tế là 6500](https://shopee.vn/M%C3%B4-%C4%90un-C%E1%BA%A3m-Bi%E1%BA%BFn-9-Tr%E1%BB%A5c-MPU-9250-GY-9250-I2C-SPI-Chuy%C3%AAn-D%E1%BB%A5ng-i.578443443.22041043458)

## Nhịp tim và SpO2

### MH-ET MAX30102: Đo lượng oxi và nhịp tim MAX102 màu đen\
  ![MAX30102 đen](https://github.com/neittien0110/linhkiendientu/assets/8079397/c281ac94-5d9c-4267-9074-5f8640a22af4)
- Nguyên lý: \
  ![nguyên lý đo nhịp tim và oxigen ](https://content.instructables.com/FPN/5MOB/LIHFO7XZ/FPN5MOBLIHFO7XZ.png?auto=webp&frame=1&fit=bounds&md=2543704f07f04af01c6d973041556e3f)
- Thông số:
  - Giao tiếp I2C sử dụng mức điên áp mặc định là 3.3V. Tuy nhiên, được phép sử dụng mức điện áp 1.8V nếu hàn dính 2 chân pad cấu hình điện áp ở mặt sau.
  - Tiêu thụ năng lượng ở mứ 600uA khi đo, và chỉ còn 0.7uA khi standby.
  - Có bộ nhớ đệm FIFO cho phép lưu 32~256 mẫu tùy theo setting và được ghi xoay vòng.
- Các chân giao tiếp:\ 
  ![Chân pin](https://content.instructables.com/FD7/1XUC/LIHFO82L/FD71XUCLIHFO82L.jpg?auto=webp&frame=1&fit=bounds&md=e9b4d49ff1fadeda8876c9a8feb7a90e)
  - VIN: in, Nguòn cấp 3.3V hoặc 5V)
  - SCL: in, tín hiệu đồng hồ của I2C
  - SDA: inout, tín hiệu dữ liệu của I2C
  - INT: out, báo ngắt tích cực mức *thấp*, và duy trì mức *thấp* cho tới khi được xóa bởi phần mềm. Nếu muốn sử dụng thì phải enable tính năng này trước đó.
  - IRD: in, dùng để điều khiển led hồng ngoại. Nếu muốn tự kiểm soát led hồng ngoại thì hãy sử dụng, ngược lại thì bỏ qua chân này.
  - RD:  in, Red LED data pin, dùng để đo dộ bão hòa oxy *SpO2) và nhịp tim (HR). Cách sử dụng tương tự như chân IRD.
  - GND: Ground
- Giải thích chi tiết:
  - Tiếng Anh: <https://lastminuteengineers.com/max30102-pulse-oximeter-heart-rate-sensor-arduino-tutorial/>
  - Tiếng Việt: <https://mecsu.vn/ho-tro-ky-thuat/may-do-oxy-xung-max30102-va-cam-bien-nhip-tim-voi-arduino.Db4>
  ![Phóng to 1](https://github.com/neittien0110/linhkiendientu/assets/8079397/75c3a16a-25bf-4e63-99cf-b7185b7d1ae2) \
  ![Mặt sau](https://github.com/neittien0110/linhkiendientu/assets/8079397/8ebe584e-ed53-4c8a-8086-63597cfd8810) 
- Video hướng dẫn: [xem 1](https://www.youtube.com/watch?v=0rsHJbog6dk), [xem 2](https://www.youtube.com/watch?v=cEtyMkubXj4)
- Cơ chế hoạt động của chân ngắt **Interrupt**: có 5 nguyên nhân khiên chân ngắt tích cực là:
  1. **Power Ready**: khi device được cấp điện trở lại, device sẽ mất một thơi gian ngắt để đi vào trạng thái hoạt động. Vậy ngắt được sinh ra để báo rằng device đã sẵn sàng để đo nhịp tim.
  2. **New Data Ready**: báo hiệu đã có dữ liệu đo SpO2 và Nhịp tim ở bộ đệm FIFO.
  3. **Ambient Light Cancellation**:  kích hoạt khi chức năng hủy sự can thiệp của ánh sáng môi trường của diot quang SpO2/HR đã đạt cực đại và có thể gây ảnh hưởng tới kết quả đo đầu ra.
  4. **Temperature Ready**: Báo hiệu rằng dữ liệu nhiệt độ gần nhất đã sẵn sàng để đọc. 
  5. **FIFO Almost Full:**: Bộ đệm FIFO đã đầy. Bên ngoài cần đọc thông tin sớm để tránh bị MAX30102 đo tiếp và ghi đè.
- [Tài liệu datasheet pdf](https://www.analog.com/media/en/technical-documentation/data-sheets/MAX30102.pdf)
- Lập trình:
  ```Arduino
    #define BLACK_MAX30102_WRITE_ADDRESS 0xAE  # Địa chỉ để thực hiện ghi dữ liệu vào device
    #define BLACK_MAX30102_WRITE_ADDRESS 0xAF  # Địa chỉ để thực hiện đọc dữ liệu từ device
  ```
  [Code mẫu EN](https://lastminuteengineers.com/max30102-pulse-oximeter-heart-rate-sensor-arduino-tutorial/)
  [Code mẫu VN](https://mecsu.vn/ho-tro-ky-thuat/may-do-oxy-xung-max30102-va-cam-bien-nhip-tim-voi-arduino.Db4)
- [Mua sắm](https://shopee.vn/M%C3%B4-%C4%91un-C%E1%BA%A3m-Bi%E1%BA%BFn-Nh%E1%BB%8Bp-Tim-MAX30102-MAX30100-i.820808044.16479616248)

### TÍM: Đo lượng oxi và nhịp tim MAX102
  ![max30102](https://github.com/neittien0110/linhkiendientu/assets/8079397/a59436a9-4e5e-4eee-bc49-09aef0d442ab)
  ```
  Cảm biến nhịp tim và oxy trong máu MAX30102
  IC chính: MAX30102
  Đo được nhịp tim và nồng độ Oxy trong máu.
  Điện áp sử dụng: 3.3~5VDC.
  Nhỏ gọn, siêu tiết kiệm năng lượng, thích hợp cho các thiết bị đo nhỏ gọn, Wearable Devices.
  Giao tiếp: I2C, mức tín hiệu TTL.
  Kích thước: 1.4 cm x 1.4 cm x 0.3 cm
  ```  
  - [Mua sắm pcb tím](https://shopee.vn/B%E1%BA%A3ng-m%E1%BA%A1ch-c%E1%BA%A3m-bi%E1%BA%BFn-max30102-max30100-cho-Arduino-Not-max30100-i.81431289.2337919080)
  - [Mua sắm MH-ET Live pcb đen](https://shopee.vn/product/148048328/6415419258?gad_source=1&gclid=EAIaIQobChMIjerb3saihQMVhqNmAh0uYgB4EAYYASABEgJ2B_D_BwE)
  - [3d case 1](https://www.thingiverse.com/thing:4395147)
  - [3d case 2](https://www.thingiverse.com/thing:4847827)

### Bàn phím
- Ky-023 Joystick Nút Điều Khiển JoyStick PS2 STM32 Cho Tay Cầm Chơi Game \
  ![Ky-023](https://github.com/neittien0110/linhkiendientu/assets/8079397/b2ae4aa5-44e2-4f26-aab2-f59fbf2aab3a)\
  ```plain
  1. Điện áp hoạt dộng: DC 3.3V~5V
  2. Pin JRX và JRY: 2 chân analog, là 2 biến trở cho biết mức độ kéo theo phương X và phương Y.
  3. Pin SW: =1 nếu Joystick được bấm. 
  ```
  - [Mua sắm](https://shopee.vn/M%C3%B4-%C4%91un-c%E1%BA%A3m-bi%E1%BA%BFn-5-pin-tr%E1%BB%A5c-k%C3%A9p-X-Y-cho-tay-c%E1%BA%A7m-ch%C6%A1i-game-Ps2-Ky-023-i.148048328.7241683324)

- Bàn phím ma trận 4x5, 4x4, 4x3\
  ![Bàn phím ma trận](https://github.com/neittien0110/linhkiendientu/assets/8079397/93ed6070-e95a-4c00-bcd4-20367764aa88)
  - [Hướng dẫn lập trình](http://arduino.vn/bai-viet/915-huong-dan-su-dung-module-ban-phim-4x4-voi-arduino)
  - [Mua sắm](https://shopee.vn/B%C3%A0n-Ph%C3%ADm-16-Ph%C3%ADm-4x4-4x4-4-*-4-Matrix-Array-Matrix-i.81431289.20537984830)

- Nắp nút nhấn B3F\
  ![Nắp nút nhấn B3F](https://github.com/neittien0110/linhkiendientu/assets/8079397/7379a7eb-b5bb-437f-bb3d-f6ef69ae43ec)
  - [Mua sắm](https://shopee.vn/-G%C3%B3i-10-c%C3%A1i-N%E1%BA%AFp-n%C3%BAt-nh%E1%BA%A5n-B3F-tr%C3%B2n-Xanh-V%C3%A0ng-i.501501433.23969870578)

- Nắp nút nhấn 6x6\
  ![Nắp nút nhấn](https://github.com/neittien0110/linhkiendientu/assets/8079397/232df378-91a4-46c1-985b-03a192abebee)
  - Đường kính vỏ nhựa ngoài: 6mm
  - Đường kính lỗ trong: 3mm
  - [Mua sắm](https://shopee.vn/-G%C3%B3i-10-c%C3%A1i-N%E1%BA%AFp-n%C3%BAt-nh%E1%BA%A5n-6x6-tr%C3%B2n-%C4%90%E1%BB%8F-V%C3%A0ng-Xanh-Tr%E1%BA%AFng-%C4%90en-i.501501433.14397655804)

## Đo khoảng cách
- Module SR-04 đo khoảng cách
  - Ý nghĩa: đo khoảng cách bằng siêu âm\
    ![HC SR-04](https://github.com/neittien0110/linhkiendientu/assets/8079397/7b263874-db23-4676-bda1-30a88b290205)
  - Thông số:
    - Điện áp hoạt động: 3.3-5V
    - Góc hoạt động: 15*
    - Khoảng cách: 2-200cm
    - Độ chính xác: 3mm (nhìn chung là thấp)
    - Không ảnh hưởng bởi mặt trời như cách đo bằng hồng ngoài, nên phù hợp với đo ngoài trời
  - Lập trình tham khảo: <https://nshopvn.com/product/cam-bien-sieu-am-hc-sr04/>
  - [Mua sắm](https://shopee.vn/B%E1%BA%A3ng-m%E1%BA%A1ch-ph%C3%A1t-hi%E1%BB%87n-s%C3%B3ng-si%C3%AAu-%C3%A2m-hc-sr04-hc-sr-04-cho-Arduino-i.395117932.9923497155)  

<span style="color:red;">Khi SR-04 bị hỏng, khoảng cách distance trả về luôn = 0.</span>

## Loa còi

- Còi Buzzer passive dạng SMD: MLT-8530
  ![image](https://github.com/neittien0110/linhkiendientu/assets/8079397/30b6f6f7-93e1-41c9-a539-da11b584c6bb)
  - Thông số:
    - Điện áp tối đa: 3.6V
    - Điện áp hoạt động: 2.5 ~ 4.5 V
    - Phát âm thanh ở tần số: 2.7kHz
  > Khoảng cách giữa 2 chân tin hiệu trùng khớp với loại còi Buzzer chân DIP thông thường
  - [Datasheet](https://wmsc.lcsc.com/wmsc/upload/file/pdf/v2/lcsc/1811151451_Jiangsu-Huaneng-Elec-MLT-8530_C94599.pdf)
  - [Trong thư viện JLCPCB](https://jlcpcb.com/partdetail/Jiangsu_HuanengElec-MLT8530/C94599)
  - [Mua sắm](https://shopee.vn/MLT-8530-Buzzer-passive-3.6V-2700Hz-8.5x8.5x3mm-i.501501433.23671510680)

## Nhiệt độ Độ ẩm

 - Mô Đun Cảm Biến Nhiệt Độ Và Độ Ẩm Độ Chính Xác Cao aht10 aht20 aht30
     ![Mặt trước](https://github.com/user-attachments/assets/e1ba86c2-1a0d-4c61-a17c-387fae4a88ce)
     ![Mặt sau](https://github.com/user-attachments/assets/0d7a8347-51e7-4fd0-925d-e8af597059cd)
   - Thông số:
     1. Kích thước mô-đun: 16 * 11 mm
     2. Loại giao diện: I2C
     3. Điện áp làm việc: 1,8-6,0 V
     4. Kích thước giao diện: 4 * 2,54mm cao độ
     5. Độ ẩm chính xác: ± 2% điển hình
     6. Độ phân giải độ ẩm: 0,024%
     7. Độ chính xác nhiệt độ: điển hình ± 0,3 ° C
     8. Độ phân giải nhiệt độ: Tiêu chuẩn 0,01 °C
     9. Nhiệt độ làm việc: -40°C - 85°C
   - Lập trình:
       ```C
         #define I2C_ADDRESS_AHT  0x38
         adafruit/Adafruit AHTX0@^2.0.5      ;https://github.com/adafruit/Adafruit_AHTX0
       ```
   - [Mua sắm](https://shopee.vn/M%C3%B4-%C4%90un-C%E1%BA%A3m-Bi%E1%BA%BFn-Nhi%E1%BB%87t-%C4%90%E1%BB%99-V%C3%A0-%C4%90%E1%BB%99-%E1%BA%A8m-%C4%90%E1%BB%99-Ch%C3%ADnh-X%C3%A1c-Cao-aht10-aht20-aht30-i2c-sht20-i.578443443.15990161525)

## Tia UV

 - Module cảm biến tia UV MCU-6075 I2C- CC3
     ![Mặt trước](https://github.com/user-attachments/assets/2be9052a-5fd1-4d27-a5b8-2123aa5a8886)
   - Thông số:
     1. Điện áp hoạt động: 3 – 5VDC
     2. Điện áp giao tiếp I2C: 3 – 5VDC
     3. Giao tiếp I2C, địa chỉ **0x10**
     4. Độ nhạy cao với tia UVA (320-400 nm) và UVB (280-320 nm)
   - Lập trình:
       ```C
         #define I2C_ADDRESS_UV  0x10
         adafruit/Adafruit VEML6075 Library@^2.2.2      ;https://github.com/adafruit/Adafruit_VEML6075
       ```
   - Lưu ý: vì lý do nào đó mà việc quét các địa chỉ I2C sẽ không phát hiện ra module này.
   - [Video![gif](https://i.ytimg.com/an_webp/WXK3HuP39Ig/mqdefault_6s.webp?du=3000&sqp=CLjO37cG&rs=AOn4CLDGpdSQArCTYYThJ9VMxZA_IJb5Mg)](https://youtu.be/WXK3HuP39Ig?si=hJhnxBdJ1F7y43LO)
   - Mua sắm](https://shopee.vn/Module-c%E1%BA%A3m-bi%E1%BA%BFn-tia-UV-MCU-6075-I2C-CC3-i.310609561.8904452121)

## Khác
- Bộ tắt/bật AC-220V, điều khiển bằng RF 433MHz. Đã có sẵn chuyển đổi AC-DC để nuôi mạch RF nên không cần nguòn DC.\
  ![image](https://github.com/neittien0110/linhkiendientu/assets/8079397/edf27568-3740-4564-ac54-600d3c5373d5)
  ![image](https://github.com/neittien0110/linhkiendientu/assets/8079397/dc7ef50f-6d9f-4c1b-8601-bfc1fe0a542d)

  ```plain
  1. Điện áp vào: AC85V-AC220V
  2. Tần số sóng điều khiển: 433 MHz
  3. Dải tần RF: Super 315mhz-433.92
  4. Mức độ nhạy bộ thu: -107dBm
  5. Khoảng cách điều khiển:> 100 m (trong điều kiện trống trải)
  6. Phương pháp giải mã: Giải mã bằng phần mềm trong MCU
  7. Số kênh điều khiển có thể lưu: 16
  8. Phương pháp điều khiển: mã cố định, hoặc học mã
  9. Kênh: 1CH
  10. Các chế độ hoạt động: (Jog / Non-Locked, Inter-lock / Latched, Self-lock / Self-Locked)
  11. Rated load: 10A 250VAC / 10A 125VAC
                   10A 30VDC / 10A 28VDC 
  12. Kích thước: 5.4 cm * 3.1 cm * 1.4 cm
  ```

  - 3 chế độ hoạt động
    - Chế độ Jog: Bấm giữ là khóa, nhả tay là mở.
    - Chế độ Self-lock / Self-Latched:  Bấm 1 lần là khóa, bấm lần nữa là mở khóa (cùng một nút)
    - Chế độ intersperre / Latched: Bâmt 1 nút để khóa, bấm nút khác để mở
  - Xóa & Học Mã:
    1. Chức năng xóa - Sau khi nhấn nút "KEY" 8 lần, đèn LED tắt và tất cả dữ liệu điều khiển từ xa trong bộ nhớ. Khi đèn LED nhấp nháy 5 lần, điều đó cho biết chức năng xóa đã hoàn tất.
    2. chức năng học - nhấp vào nút học "KEY", đèn báo LED cho biết bộ vi xử lý đã vào trạng thái học mã, nhấn nút điều khiển từ xa không dây thích hợp, đèn LED nhấp nháy 3 lần sau đó bật nó có nghĩa là mã thành công.
    3. Đèn LED nhấp nháy để xác định chức năng đã chọn.
    * nhấp nháy 1 lần chức năng chạy bộ
    * nhấp nháy 2 lần chức năng tự khóa
    * nhấp nháy 3 lần chức năng liên động
  
  - Nhược điểm: không lắp được nắp vào thân, vì relay cao quá. Khi dóng nắp thì ko thể bấm nút cấu hình, vì nút thấp ==> thay thế bằng nút có cán dài 11 mm
  - [Mua sắm](https://shopee.vn/M%C3%B4-%C4%91un-C%C3%B4ng-T%E1%BA%AFc-Truy%E1%BB%81n-Nh%E1%BA%ADn-T%C3%ADn-Hi%E1%BB%87u-Kh%C3%B4ng-D%C3%A2y-RF-Dc-220V-1-K%C3%AAnh-433MHz-i.201091220.7509764367), Mua kèm với [bộ điều khiển từ xa 433MHz](https://shopee.vn/B%E1%BB%99-%C4%91i%E1%BB%81u-khi%E1%BB%83n-t%E1%BB%AB-xa-kh%C3%B4ng-d%C3%A2y-4-k%C3%AAnh-4-Module-kh%C3%B4ng-d%C3%A2y-433MHZ-IC2262-2272-i.201091220.5212508592)

- Tect6000 - Transistor ánh sáng nồi đồng cối đá
  - Phải mắc thêm trở như hình dưới\
    ![Cách mặc mạch](https://github.com/neittien0110/linhkiendientu/assets/8079397/d7ff5a29-b269-4eae-b5e0-96e900c24c3f)
     
  - [Mua sắm](https://shopee.vn/Set-1206-C%E1%BA%A3m-Bi%E1%BA%BFn-Nhi%E1%BB%87t-%C4%90%E1%BB%99-Tect6000-B%E1%BA%A3o-V%E1%BB%87-M%C3%B4i-Tr%C6%B0%E1%BB%9Dng-TEMT6000X01-i.972724310.22849595571)

