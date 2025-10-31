## Mục lục

- [Góc, gia tốc, la bàn](#mpu)
- [Nhịp tim và SpO2](#nhịp-tim-và-spo2)
- [Phím bấm, bàn phim](#bàn-phím)
- [Đo khoảng cách](#đo-khoảng-cách)
- [Đo tốc độ](#đo-tốc-độ)
- [Loa, còi](#loa-còi)
- [Nhiệt độ Độ ẩm](#nhiệt-độ-độ-ẩm)]
- [Bụi](#bui)
- [Ánh sáng, hồng ngoại, uv](#ánh-sáng-hồng-ngoại-uv)
- [Định danh - Thẻ NFC, RFID, Vân tay](#thẻ-nfc-rfid)
- [Relay](#relay)


Và tham chiếu tới các trang khác:
1. [Các shield mở rộng cho board dạng D1 mini](./D1mini.md)
2. [Các loại motor](./Motors.md)
3. [Các module truyền thông](./Communications.md)
4. [Các màn hình hiển thị](./Screens.md)
5. [Nút bấm](./buttons.md)
6. [Các linh vật tư phụ kiện như mạch in, dây dẫn, thiếc, vỏ hộp](./noname.md)
7. [Linh kiện PCB để thiết kế board](./EasyEDA_Library.md)
8. [Mạch sạc pin Lithium](https://neittien0110.github.io/linhkiendientu/EasyEDA_Library.html#m%E1%BA%A1ch-s%E1%BA%A1c)
9. [Module nguồn cấp](./powersupply.md)
10. [Công cụ kiêm tra](./tools.md)

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

- Module cảm biến vật cản Radar RCWL-0516
  ![Ảnh radar RCWL-516](https://nshopvn.com/wp-content/uploads/2019/03/tren-tay-module-cam-bien-vat-can-radar-rcwl-0516-qzl0-1-600x600.jpg)
  - [Tài liệu, video hướng dẫn từ Nshop](https://nshopvn.com/product/module-cam-bien-vat-can-radar-rcwl-0516/)

## Đo tốc độ

- HB100 - Phát hiện và đo vận tốc chuyển động bằng microwave Doppler Radar
  ![image](https://github.com/user-attachments/assets/c57a4aba-c76f-4d45-a75d-b0a5fec52eaa)

  - Thông số:
    - tần số truyền: 10,525 GHz
    - Độ chính xác cài đặt tần số: 3MHz
    - Công suất đầu ra (tối thiểu): 13dBm EIRP
    - Điện áp hoạt động: 5V ± 0,25V
    - Dòng hoạt động (CW): tối đa 60mA, 37mA điển hình
    - phát sóng hài: < -10dBm
    - Chế độ xung:
    - dòng điện trung bình (5% DC): 2mA typ. chiều rộng 9 xung (Tối thiểu): 5uSec
    - chu kỳ tải (Tối thiểu): 1%
    ![image](https://github.com/user-attachments/assets/1b5d1354-4e16-480c-a4cd-069d83c0f535)
  - [Minh họa với Arduino](https://medium.com/@benjamindavidfraser/arduino-intrusion-monitoring-system-5e2d8cacf82e)
  - [Giải thích nguyên lý hoạt động và lắp breadboard](https://www.instructables.com/Easy-HB100-Amplifier/)
  - [Mua sắm](https://shopee.vn/Hb100-Microwave-Doppler-Radar-M%C3%B4-%C4%91un-kh%C3%B4ng-d%C3%A2y-C%E1%BA%A3m-bi%E1%BA%BFn-chuy%E1%BB%83n-%C4%91%E1%BB%99ng-HB100-C%E1%BA%A3m-bi%E1%BA%BFn-chuy%E1%BB%83n-%C4%91%E1%BB%99ng-l%C3%B2-vi-s%C3%B3ng-M%C3%A1y-d%C3%B2-chuy%E1%BB%83n-%C4%91%E1%BB%99ng-i.578443443.28419956894)
 
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

- Module ISD1820
  - Chức năng: ghi âm giọng nói bảng thoại và phát ra loa, bao gồm sẵn cả mic rên board và loa nối dây.
    ![image](https://github.com/user-attachments/assets/fdd89075-945c-46fd-8ed1-2ce419b35679)
  - Thông số:
    - Nguồn điện: 3-5V
    - Các nút bấm và chân pin điều khiển đều tích cực mức cao.
    - Nút/pin __REC__: điều khiển ghi âm, __nhấn giữ__ nút, hoặc tích cực chân pin trong toàn bộ thời gian ghi âm.
    - Nút/pin __PLAYE__: phát lại âm thanh đã ghi trước đó. Tích cực theo sườn. Bấm không cần giữ.
    - Nút/pin __PLAYL__: phát lại âm thanh đã ghi trước đó. Tích cực theo mức ==> Nhấn giữ để phát âm thanh, nhả nút là dừng. (_jumper không có tác dụng_)
    - Jumper __P-E__ để lặp liên tục đoạn âm thanh nếu được nối (thay thế cho vai trò của các nút __PLAYE, PLAYL__)
    - Jumper FT: từ mic khuyếch đại ra loa luôn.
    - Tốc độ 3.2k mẫu/s.
    - Thời gian ghi/phát mặc định 10s. Thay thế điện trở ROSC để có thời gian ghi dao động từ 8s tới 20s. Chi tiết trong file pdf bên dưới.
  - [Schematic và hướng dẫn chi tiết. PDF](https://www.electroniclinic.com/wp-content/uploads/2020/01/isd1820-datasheet.pdf)
  - [Mua sắm](https://shopee.vn/M%C3%B4-%C4%91un-ghi-%C3%A2m-ISD1820-m%C3%B4-%C4%91un-gi%E1%BB%8Dng-n%C3%B3i-b%E1%BA%A3ng-tho%E1%BA%A1i-b%E1%BA%A3ng-m%C3%B4-%C4%91un-%C4%91i%E1%BB%87n-tho%E1%BA%A1i-di-%C4%91%E1%BB%99ng-c%C3%B3-micr%C3%B4-Loa-i.770245757.42550598573?sp_atk=85d7cd2c-e491-495f-b2f3-beb54954713b&xptdk=85d7cd2c-e491-495f-b2f3-beb54954713b)
  - [Code mẫu tham khảo của Dương Đăng Duy với ISD1820, PIR, ESP32 Dev Module](https://github.com/duongdangduy95/AuraAlert_esp32)

- Loa chủ động:
  - Chức năng: phát âm thanh. [Tool thử tần số online](https://www.szynalski.com/tone-generator/)
  - Phân loại:
    - Điện áp: có loại 3v và 5V
    - Kích thước: rất nhiều dạng
  - Loa 9042: rất nhỏ, mỏng, không cùng cỡ chân pin với 12095.  [Dataheet](https://lcsc.com/datasheet/lcsc_datasheet_2409302231_YUEXIN-YX-KC9042-16R_C781849.pdf)
    - Khoảng cách 2 chân pin: 4mm. Có thể thiết kế connect 3pin thì loa này cắm vào pin 1 và pin 3 là phù hợp.
    - Đường kính ngoài: 9mm.
    - [LCSC](https://lcsc.com/product-detail/Buzzers_YUEXIN-YX-KC9042-16_C781849.html),  
    - [Mua sắm](https://shopee.vn/Set-5-Linh-Ki%E1%BB%87n-%C4%90i%E1%BB%87n-T%E1%BB%AD-12095-12085-9042-3v-5v-12v-12-*-9.5mm-16R-12-*-8.5mm-i.778834786.19356518887)
  - Loa 12095: loại phổ biến ở cửa hàng

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

- Gy-906 MLX90614ESF - Module cảm biến nhiệt độ không tiếp xúc
  ![image](https://github.com/user-attachments/assets/0195e8fb-ed97-404a-b1b1-bd2dc088bfb5)

  - Ứng dụng: đo nhiệt độ cơ thể người bằng cách dí gần trán
  - Thông số:
    - Độ phân giải đo: 0,02 ° C
    - Giao tiếp: I2C
  - [Hướng dẫn từ Nshop](https://nshopvn.com/product/cam-bien-nhiet-do-hong-ngoai-khong-tiep-xuc-gy-906-mx90614/)
  - [Mua sắm](https://shopee.vn/Gy-906-MLX90614ESF-M%C3%B4-%C4%91un-c%E1%BA%A3m-bi%E1%BA%BFn-nhi%E1%BB%87t-%C4%91%E1%BB%99-kh%C3%B4ng-ti%E1%BA%BFp-x%C3%BAc-MLX90614-m%E1%BB%9Bi-cho-t%C6%B0%C6%A1ng-th%C3%ADch-Arduino-i.578443443.28358962552)

- Module đốt nóng

   ![image](https://github.com/user-attachments/assets/393cdabb-d450-43a5-967e-fc19d7a00769)  ![image](https://github.com/user-attachments/assets/ee633705-5506-4531-87e0-ad67a2bf1e3f)  ![image](https://github.com/user-attachments/assets/38db4c11-80c4-4839-ba9f-d5dbddbf42de)

  -![Video](https://down-zl-sg.vod.susercontent.com/api/v4/11110103/mms/vn-11110103-6khw6-m6aieyv8yfwj28.16000051739670033.mp4)
  - Ứng dụng Sử dụng để  tự chế cháo các loại thiết bị đốt nóng, thay thế lõi mayso
  - Cấu trúc: Đây điện trở nhiệt Vonfram có tác dụng chuyển điện năng thành nhiệt năng trong quá trình cản trở dòng điện, để đốt làm nóng đỏ bộ phận đốt.
  - Thông số:
    - Điện áp: 3.7v-5v (có thể lấy trực tiếp từ pin lithium
    - Dòng: 1.5 ~ 2.5A
    - Công suất: 9-11W
    - Chất liệu: Sứ, đồng,  (Wolfram)
    - Kích thước: 15mm x 10mm
    - Trọng lượng: 1.2g
  - [Mua sắm](https://shopee.vn/Thi%E1%BA%BFt-b%E1%BB%8B-gia-nhi%E1%BB%87t-%C4%91%E1%BB%91t-n%C3%B3ng-ch%C3%A1y-DIY-d%C3%B9ng-pin-3.7v-5v-d%C3%B2ng-ra-tr%C3%AAn-2A-i.523359606.25740281518)

- Thiết bị đốt nóng Type-C
  
  ![image](https://github.com/user-attachments/assets/6d731265-5d89-4528-81e8-b8d3734591d5)
  [Video](https://cvf.shopee.vn/file/api/v4/11110107/mms/vn-11110107-6khwd-m3ee6t4p68x4f7.16000071733367351.mp4)
  - Thông số:
    - Chân nguồn: USB Type-C
    - Có 1 nút bấm nhấn/nhả để tắt bật, nhưng dễ bị gẫy khi vận chuyển
  - Chú ý: cần bỏ 1 con trở 103 ở phần đầu nguồn mới dùng được như trong video trên (shop thường gỡ trước khi bán)
  - [Mua săm](https://shopee.vn/s%E1%BA%A3n-ph%E1%BA%A9m-b%E1%BB%99-l%C3%A0m-n%C3%B3ng-ch%C3%A2n-ngu%E1%BB%93n-type-c-i.523359606.28269702790)

- Tấm nhiệt làm nóng 3v-5v hình tròn 3.5cm
  
  ![image](https://github.com/user-attachments/assets/9ca42c43-0f80-42ab-b362-8805bb6ba09d)
  - Thông số:
    - Điện trở 16 ohm
    - Gồm 3 lớp xếp chồng
      1. Băng dính xanh 
      2. Lớp nhiệt trở
      3. Băng dính 3M
    - Có sẵn header PH2.0 mm cái
    - Điện áp vào 5v thì tấm cho nhiệt khoảng 30-40 độ, tiêu thụ 0.3A \
      Điện áp vào 3v3 lấy trực tiếp từ pin lithium thì chỉ ấm một chút, hợp với sưởi ấm cơ thể
  - [Mua sắm](https://shopee.vn/t%E1%BA%A5m-nhi%E1%BB%87t-l%C3%A0m-n%C3%B3ng-3v-5v-h%C3%ACnh-tr%C3%B2n-3.5cm-i.523359606.25014804130)  

## Bụi
- Nova SDS011: bao gồm cả sensor, lồng đối lưu, quạt thông khí.
  <img width="419" height="265" alt="SDS011" src="https://github.com/user-attachments/assets/8f656b4d-fc42-4040-8214-6b90ca5665fa" />
  - Thông số:
    -   Đo đồng thời P2.5 và P10
    -   Điều kiện làm việc: __độ ẩm < 70%__
    -   Tốc độ mẫu: 1 mẫu/giây
  - Ý nghĩa của jack kết nối XH2.54 7 pin
    | pin | Name | comment |
    | :---: | :---: | :--- |
    | 1 | CTL | control pin, backup |
    | 2 | 1um | PM2.5 0-999 ug/m^3, PWM Ouput với chu kì 1004ms. Động rộng xung từ [2ms-1001ms] tương ứng với 0us-999u/m^3  |
    | 3 | 5V | 5V Input |
    | 4 | 25um | PM10 0-999 ug/m^3, PWM Output PWM Ouput với chu kì 1004ms. Động rộng xung từ [2ms-1001ms] tương ứng với 0us-999u/m^3 |
    | 5 | GND | ground |
    | 6 | R | RX of UART (TTL) |
    | 7 | T | TX of UART (TTL) |
  - Kết nối
    - Có thể lấy số liệu dạng analog ở chân pin 2, 4 như bảng trên
    - hoặc có thể lấy dữ liệu số qua giao tiếp serial:
      - baudrate=9600 bps, 8-bit data, no parity bit, one stop bit.
      - Cú pháp
        | STT byte | Name | Content |
        | :---: | :---: | :--- |
        | 0 | Message header | AA |
        | 1 | Commander No. | C0 |
        | 2 | DATA 1 | PM2.5 Low byte |
        | 3 | DATA 2 | PM2.5 High byte |
        | 4 | DATA 3 | PM10 Low byte |
        | 5 | DATA 4 | PM10 High byte |
        | 6 | DATA 5 | ID byte 1 |
        | 7 | DATA 6 | ID byte 2 |
        | 8 | Check-sum | Check-sum |
        | 9 | Message tail | AB |
  - [Homepage](https://www.sdnf.com/?list_13/55.html)
  - [Mua sắm](https://shopee.vn/NOVA-M%C3%B4-%C4%90un-C%E1%BA%A3m-Bi%E1%BA%BFn-Kh%C3%B4ng-Kh%C3%AD-Sds011-Pm2.5-Ch%E1%BA%A5t-L%C6%B0%E1%BB%A3ng-Cao-i.578443443.15128384320)
  - Tham khảo:
    -   [Nguyên lý, kết nối, chương trình đọc dữ liệu trên PC, shematic, ](https://www.open-electronics.org/sds011-the-air-quality-sensor/)
    -   [Code mẫu arduino từ nshop, đọc dữ liệu qua serial](https://nshopvn.com/product/module-cam-bien-bui-laser-sds011/)
    -   [Interfacing SDS011 Air Quality Sensor with ESP8266: DIY Air Pollution Monitor Part1 | SDS011+ESP8266](https://electronicsinnovation.com/interfacing-sds011-air-quality-sensor-with-esp8266-diy-air-pollution-monitor-part1/)
        <img width="768" height="886" alt="Interfacing SDS011 with ESP8266" src="https://github.com/user-attachments/assets/e0332006-ae4d-4db7-b2d9-4e53aa8fd0e0" />



## Ánh sáng, hồng ngoại. uv

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
  - [Mua sắm](https://shopee.vn/Module-c%E1%BA%A3m-bi%E1%BA%BFn-tia-UV-MCU-6075-I2C-CC3-i.310609561.8904452121)

- Tect6000 - Transistor ánh sáng nồi đồng cối đá
  - Phải mắc thêm trở như hình dưới\
    ![Cách mặc mạch](https://github.com/neittien0110/linhkiendientu/assets/8079397/d7ff5a29-b269-4eae-b5e0-96e900c24c3f)
  - [Mua sắm](https://shopee.vn/Set-1206-C%E1%BA%A3m-Bi%E1%BA%BFn-Nhi%E1%BB%87t-%C4%90%E1%BB%99-Tect6000-B%E1%BA%A3o-V%E1%BB%87-M%C3%B4i-Tr%C6%B0%E1%BB%9Dng-TEMT6000X01-i.972724310.22849595571)

- Led WS2812B RGB 5050 4 chân 5.0x5.0mm \
  ![Hình thực tế](https://github.com/user-attachments/assets/db460c6e-b8ef-4263-9963-dba6d9eda929)
  ![Nguyên lý](https://github.com/user-attachments/assets/964a476a-974b-4e78-9276-ea1362ae1518)
  - Thóng số:
    - Điện áp hoạt động: 3v5-5v3
  - [Mua sắm](https://shopee.vn/WS2812B-4-Led-RGB-5050-4-ch%C3%A2n-5.0x5.0mm-i.501501433.20276445920)

- Led WS2812B RGB 5050 4 chân 5.0x5.0mm dạng module led đơn \
  ![Front](https://github.com/user-attachments/assets/fe414bd7-9a8f-4dd6-808b-09ae44320ccf)
  ![Rear](https://github.com/user-attachments/assets/188b6027-9f9b-4a6b-87d2-76406d3db65d)
  - [Mua sắm](https://shopee.vn/Set-10-chip-%C4%91%C3%A8n-led-Dc-5v-3mm-X-10mm-Ws2812B-Smd-5050-Ic-Ws2812-i.81431289.11137056635)

- Led WS2812B RGB 5050 4 chân 5.0x5.0mm dạng module vuông, tròn \
  ![image](https://github.com/user-attachments/assets/a67bb2d9-0ca7-4465-9963-9587c6ed6fb0)
  - Thông số:
    - Loại module vòng tròn có 4 chân kết nối theo thứ tự là: DI / 5V / 0V /DO
    - Loại module hình vuông có 3 chân kết nối theo thứ tự là: V- /  IN / V +
  - [Mua sắm](https://shopee.vn/Rgb-V%C3%B2ng-%C4%90%C3%A8n-led-1-3-4-7-8-9-12-16-24-32-Bit-ws2812-5050-rgb-T%E1%BB%B1-L%E1%BA%AFp-R%C3%A1p-arduino-i.972724310.22355750623?sp_atk=42bb5391-8d7c-40f4-923c-713457118980&xptdk=42bb5391-8d7c-40f4-923c-713457118980)
  - [Mua sắm](https://shopee.vn/B%E1%BA%A3ng-M%E1%BA%A1ch-%C4%90%C3%A8n-LED-Nhi%E1%BB%81u-M%C3%A0u-S%E1%BA%AFc-4-16-25-64-bit-WS2812-5050-RGB-i.869927552.23538525625)

## Thẻ NFC RFID

- RC-522 - module đọc NFC 13.56Mhz
  - Minh họa sử dụng ESP32-Dev-Kit với module:
    ![ ](![image](https://github.com/user-attachments/assets/66991625-8106-44b3-bde3-d88501262904)\
    [Xem video kết quả](https://youtu.be/VQAy33XYFEY?si=3vtoG_t9ghqNWzda)
  - [Mua sắm](https://shopee.vn/M%C3%B4-%C4%91un-%C4%91%E1%BB%8Dc-th%E1%BA%BB-RFID-13.56MHz-RC522-MFRC522-NFC-MFRC-522-RC-522-Arduino-PIC-i.578443443.10867340272?sp_atk=b5f5e2d3-e871-4cd5-8062-d1113a27a100&xptdk=b5f5e2d3-e871-4cd5-8062-d1113a27a100)

- RDM6300 - module đọc RFID 125Khz
  - ![RDM6300](https://github.com/user-attachments/assets/d048636a-307d-4f5a-84ae-526e5a35391c)
  - Thông số:
    - Tần số thẻ RFID: __125KHz__
    - Khoảng cách phát hiện: 2cm-5cm
    - Giao tiếp: UART/Serial, 9600 bps
    - Điện áp hoạt động: 5V
    - Pin: ![image](https://github.com/user-attachments/assets/3f9aee53-54e3-4f3a-af4d-e136280307fd)
    - Kết nối MCU: ![image](https://github.com/user-attachments/assets/a60ec624-418b-4b57-9f44-e1e6f95283e8)   
  - [Hướng dẫn sử dụng từ Nshop](https://nshopvn.com/product/module-thu-phat-rfid-rdm6300-rf-125khz-uart-noi-tiep-dau-ra/)
  - [Schematic](https://www.makershop.de/download/RDM-6300.pdf)
  - [Mua sắm](https://shopee.vn/M%C3%B4-%C4%90un-%C4%90%E1%BB%8Dc-RFID-125Khz-RDM6300-UART-Cho-arduino-i.578443443.20706992299)

- Module cảm biến vân tay AS608
  - Thông số:
    - 162 vân tay
    - giao tiếp UART, 57600 bps
  - API, guide: [Datasheet](https://handsontec.com/dataspecs/sensor/AS608%20Finger%20print%20Sensor.pdf)
  - [Tải về phần mềm SFG kết nối module](http://www.adafruit.com/datasheets/SFGDemoV2.0.rar)
  - [Video demo sử dụng phần mềm SFG để lây ảnh vân tay, fingerprint](https://www.youtube.com/watch?v=9faXEHvMgMA)

## Relay

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
