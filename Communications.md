## NRF24L01

NRF24L01 có các đặc tính gồm
- truyền dữ liệu không dây
- tần số 2.4 GHz
- giao tiếp **SPI**
- cự li 200m.
- Điện áp: **3.3v**
- Cho phép truyền từ xa như xây dựng xe điều khiển bằng sóng Radio trực tiếp 

![Nhiều loại module](https://github.com/neittien0110/linhkiendientu/assets/8079397/4996a4d0-8c2c-4f1a-81ae-f3ddff203a02)

- Pinout 
  - VIN: Module power supply
  - GND: Ground
  - MOSI: Data transmit for SPI protocol
  - MISO: Data receive for SPI protocol
  - SCK: SPI Clock
  - IRQ: Interrupt for SPI protocol
  - CSN: Module select for SPI protocol (reverse)
  - CE: Enable SPI protocol

- Các dạng module:\
  - loại có 2x4 chân 2.54mm\
    ![loại có 2x4 chân 2.54mm](https://github.com/neittien0110/linhkiendientu/assets/8079397/aa02c8fd-27ce-4cdd-a4a7-51e1cd9a4414)
  - Loại có antenna ngoài\
    ![Loại có antenna ngoài](https://github.com/neittien0110/linhkiendientu/assets/8079397/f3381c85-4f95-4d1e-b57c-57d6b0e46a04)\
  - Mini: có 8 chân SMT 1.27mm\
    ![Loại có 8 chân siêu nhỏ](https://github.com/neittien0110/linhkiendientu/assets/8079397/fb93ba72-3feb-4d96-b5eb-f20c87608d7c)\
    [Xem thêm tài liệu](https://howtomechatronics.com/tutorials/arduino/arduino-wireless-communication-nrf24l01-tutorial/#:~:text=The%20pins%20CSN%20and%20CE,t%20have%20to%20be%20used.)


- Mô hình kết nôi. \
  ![Desktop-MCUs](https://github.com/neittien0110/linhkiendientu/assets/8079397/c1c8056c-a1c2-4c80-b323-5f125d5d3942)
  > Chưa thành công: MCU-MCU thì okay,  Laptop-Laptop thì okay, nhưng Laptop-MCU thì không nhận được dữ liệu


- [Mua sắm](https://shopee.vn/M%C3%B4-%C4%91un-truy%E1%BB%81n-d%E1%BB%AF-li%E1%BB%87u-kh%C3%B4ng-d%C3%A2y-NRF24L01-2.4G-2.4GHz-NRF24L01-phi%C3%AAn-b%E1%BA%A3n-n%C3%A2ng-c%E1%BA%A5p-NRF24L01-PA-LNA-1000-GT24-i.812409307.20422229589).  Lưu ý cố thể mua loại SMD không hàn pin, để tiện hàn lên PCB nhưng loại này sử dụng chân 1.25 mm

## Module HC-12 RF UART 433Mhz

  ![image](https://github.com/user-attachments/assets/b4852145-e92e-44f5-b1b2-8677865bb842)
- Thông số:
  - Khoảng cách tối đa: 1000m
  - Điện áp hoạt động:	3.3V - 5V
  - Dòng tiêu thụ chế độ chờ:	16mA
  - Công suất:	80mW -200mW, có thể cài đặt
  - Chuẩn giao tiếp:	UART
  - Tốc độ: 5 kbps
  - Tần số: 433.4 - 473.0MHz
  - Kích thước: 27.8mm × 14.4mm × 4mm
- Các chân pin:
  - Vcc  : Cấp nguồn 3.3V – 5V.
  - GND: Cấp nguồn 0V
  - RXD : Nhận dữ liệu UART
  - TXD : Truyền dữ liệu UART
  - SET : Thiết lập các thông số
  - ANT1 : Gắn anen dây rời SMA
  - GND: Cấp nguồn 0V
  - ANT2 : Hàn anten lò xo
  - GND: Cấp nguồn 0V
  - NC : Không kết nối
- Cách sử dụng:
  - Các module phải có cùng kênh sóng, địa chỉ, kênh và địa chỉ phải khác 0.
  - Để cài đặt module, đưa module vào chế độ AT command: nối chân SET xuống mass trước khi cấp nguồn, sau đó cấp nguồn, module sẽ tự động reset về các thông số gốc: Baurate: 9600, stop bits:1, parity: none.
  - Để cài đặt Baurate của module dùng lệnh: AT+Bxxxx (trong đó xxxx là số baudrate, ví dụ 9600, 38400, 115200, ... )
  - Để cài đặt kênh sóng dùng: AT+Cxxx (trong đó xxx là số kênh từ 000 đến 127)
  - Để cài đặt địa chỉ dùng: AT+Axxx (trong đó xxx là địa chỉ từ 000 đến 255)
  - Để cài đặt công suất phát sóng dùng: AT+Px (trong đó x từ 1 đến 8, mặc định là 8 ~ 10 dBm)
  - Sau khi cài đặt xong nối chân SET lên VCC hoặc để hở để về chế độ hoạt động bình thường: tất cả dữ liệu truyền qua UART vào module sẽ được truyền đến tất cả các module khác có cùng kênh sóng và địa chỉ, và truyền ra bằng UART.
- [Tài liệu hướng dẫn từ Nshop](https://hshop.vn/mach-thu-phat-rf-uart-si4463-433mhzkhoang-coch-1km)
- [Code mẫu](https://howtomechatronics.com/tutorials/arduino/arduino-and-hc-12-long-range-wireless-communication-module/)
- [Mua sắm](https://shopee.vn/1-M%C3%B4-%C4%90un-433mhz-hc-12-si4463-Kh%C3%B4ng-D%C3%A2y-bluetooth-1000m-M%E1%BB%9Bi-i.81431289.18486007983)

## Bộ thu không dây 4 kênh YK-04 433MHZ IC2262 / 2272

  ![Ảnh minh họa](https://down-vn.img.susercontent.com/file/7e2c6c7ab361b8449ff05bbee8660e0f.webp)
 - Thông số
  1.Điện áp hoạt động: 5V
  2.Dòng điện hoạt điện: 10mA @ 12V
  3. Công suất tăng: 10 mw @ 12V
  4. Chế độ điều chế: ASK (Điều chế biên độ)
  5. Tần số truyền: 433MHZ
  6. Khoảng cách truyền tín hiệu: 50-100M (không gian mở, độ nhạy của máy thu là -100dbm)
  7. Mã: mã cố định (tức là không [học được mã mới từ bộ điều khiển như bộ này](https://nshopvn.com/product/mach-thu-song-rf-315mhz-hoc-lenh-3891-s0/))
- Bộ điều khiển nhựa là đầu phát. Mạch PCB có mã YK-04 là bộ thu. 4 nút trên bộ điều khiển khi bấm sẽ tương ứng với 4 chân D0-D3 trên bộ thu
   ![Ảnh mua sản phẩm](https://down-vn.img.susercontent.com/file/vn-11134103-7r98o-ltgf5k69uwi297.webp)
- [Mua sắm](https://shopee.vn/B%E1%BB%99-%C4%91i%E1%BB%81u-khi%E1%BB%83n-t%E1%BB%AB-xa-kh%C3%B4ng-d%C3%A2y-4-k%C3%AAnh-4-Module-kh%C3%B4ng-d%C3%A2y-433MHZ-IC2262-2272-i.201091220.5212508592)

## Bộ thu không dây 1 kênh ZX-011 RF 433mHz-315Hz 

![image](https://github.com/user-attachments/assets/b46a5902-8aff-4595-83b5-49ce7d2aa89a)
![image](https://github.com/user-attachments/assets/78c6bda4-921c-43b2-93ae-cafdf543d14f)
![image](https://github.com/user-attachments/assets/eeef6e8f-e4f4-4e7d-9c03-a45419c238e8)


- THÔNG SỐ KỸ THUẬT
  - Hỗ trợ chế độ điều chế ASK/OOK , độ nhạy thu đạt -108dBm ;
  - Tần số làm việc: 315 MHz , 433,92 MHz , băng thông khoảng ± 150KHz ;
  - Phạm vi đầu vào điện áp nguồn: 2.2V-5.0V ;
  - Tính chọn lọc tốt và khả năng triệt tiêu nhiễu ;
  - Khả năng triệt tiêu sóng dao động cục bộ tốt, nhiều module nhận có thể hoạt động cùng nhau (nghĩa là gửi một lần và nhận nhiều lần) mà không gây nhiễu lẫn nhau và sử dụng cùng nhau không ảnh hưởng đến khoảng cách nhận;
  - Phạm vi nhiệt độ: -40-85℃ có thể hoạt động bình thường ngay cả dưới nhiệt độ môi trường khắc nghiệt;
  - Kích thước nhỏ

- ỨNG DỤNG
  - Công tắc, ổ cắm điện không dây
  - Rèm điều khiển từ xa, điều khiển ra vào, xe điện
  - Hệ thống an ninh, giám sát
  - Kiểm soát phòng khách sạn
  - Sản phẩm nhà thông minh
- [Mua sắm](https://shopee.vn/M%E1%BA%A1ch-thu-ph%C3%A1t-t%C3%ADn-hi%E1%BB%87u-RF-433mhz-315Mhz-Ch%C6%B0a-gi%E1%BA%A3i-m%C3%A3-module-thu-ph%C3%A1t-kh%C3%B4ng-d%C3%A2y-s%C3%B3ng-RF-i.134796651.18903502931?sp_atk=6cc9abf7-a2bd-4805-9c67-f86a0cf05dc4&xptdk=6cc9abf7-a2bd-4805-9c67-f86a0cf05dc4)

## Module thu phát RF 433Mhz

![image](https://github.com/user-attachments/assets/e22a9361-875a-43cd-bb45-d933226c37d7)

Video hướng dẫn![[Video hướng dẫn Video](https://www.youtube.com/watch?app=desktop&v=b5C9SPVlU4U&t=153s)](https://github.com/user-attachments/assets/312c3442-db62-47a4-af35-a1c77c7e7aac)

- Thông số mô-đun máy thu
  - Mã sản phẩm: MX-RM-5V
  - Điện áp hoạt động: DC5V dòng tĩnh: 4MA                   
  - Tần số nhận: 433,92mHz   
  - Độ nhạy của máy thu: - 105DB
  - Kích thước: Ăng-ten bên ngoài 30 * 14 * 7mm: Dây lõi đơn 32CM quấn thành hình xoắn ốc

- Thông số kỹ thuật của đầu máy phát
  - Mô hình sản phẩm: MX-FS
  - Khoảng cách phóng: 20 -200 mét (điện áp khác nhau, kết quả khác nhau)
  - Điện áp hoạt động: 3.5-12V
  - Kích thước: 19 * 19mm
  - Cách làm việc: Tốc độ truyền AM:
  - Công suất truyền 4KB / S: 10mW              
  - Tần số truyền: 433M
  - Ăng-ten bên ngoài: 25cm dòng đa lõi hoặc lõi đơn thông thường
  - Sơ đồ chân từ trái → phải: (DATA; VCC; GND)

- Môi trường ứng dụng: Công tắc điều khiển từ xa, mô-đun thu, xe máy, sản phẩm chống trộm ô tô, sản phẩm an ninh gia đình, cửa điện, cửa chớp, cửa sổ, ổ cắm điều khiển từ xa, đèn LED điều khiển từ xa, cửa điện điều khiển từ xa âm thanh từ xa, điều khiển từ xa cửa nhà để xe, Cửa có thể thu vào điều khiển từ xa, cổng âm lượng từ xa, cửa chảo, mở cửa điều khiển từ xa, hệ thống điều khiển thiết bị đóng cửa, rèm điều khiển từ xa, máy chủ báo động, báo động, ô tô điện điều khiển từ xa xe máy, điều khiển từ xa MP3.

- [Code mẫu](http://arduino.vn/bai-viet/289-truyen-tin-hieu-voi-module-radio-frequence-433mhz)
- [Mua sắm](https://shopee.vn/B%E1%BB%99-thu-v%C3%A0-m%C3%B4-%C4%91un-ph%C3%A1t-kh%C3%B4ng-d%C3%A2y-RF-315Mhz-433MHZ-5V-DC-433MHZ-kh%C3%B4ng-d%C3%A2y-cho-Arduino-Raspberry-Pi-ARM-MCU-WL-B%E1%BB%99-t%E1%BB%B1-l%C3%A0m-i.578443443.29260588424?sp_atk=12f88405-d196-4787-814f-98ab2009db7c&xptdk=12f88405-d196-4787-814f-98ab2009db7c)


# Mô-đun truyền phát RF 315 MHz 433 MHz truyền dẫn đường dài H34P H34S H34C H34A

![image](https://github.com/user-attachments/assets/79a48f52-01da-4bca-9658-491f258f20f3)

- [Mua sắm](https://shopee.vn/M%C3%B4-%C4%91un-truy%E1%BB%81n-ph%C3%A1t-RF-315-MHz-433-MHz-M%C3%B4-%C4%91un-truy%E1%BB%81n-%C4%91%E1%BB%99ng-%C4%90i%E1%BB%81u-khi%E1%BB%83n-t%E1%BB%AB-xa-kh%C3%B4ng-d%C3%A2y-Truy%E1%BB%81n-d%E1%BA%ABn-%C4%91%C6%B0%E1%BB%9Dng-d%C3%A0i-H34P-H34S-H34C-H34A-i.81431289.28500865201?sp_atk=ac554eae-2979-42d5-be5d-1b55448c985f&xptdk=ac554eae-2979-42d5-be5d-1b55448c985f)

## JDY-41

![front](https://github.com/user-attachments/assets/5a0075e3-35aa-4c98-9076-63d2bc41f06a)
![rear](https://github.com/user-attachments/assets/472ab972-bfd5-4e1f-9001-919c74e13383)

- Thông số:
  - Sóng mang: 2.4GHz

- [Datasheet](https://www.postavrobota.cz/fotky46704/fotov/_ps_2370JDY-41-Manual.pdf)
  
![layout](https://github.com/user-attachments/assets/34a6fa4d-ea2d-44ba-b0d6-323e37e07f80)

- [JDY-41 Shield](https://easyeda.com/editor#id=14db2118aee146ca99ca9489d7a761b9|85960bbc2d5c4422a18e05993adbe9b9)
![Schematic](https://github.com/user-attachments/assets/3b0f69d8-b91b-4f27-8b1e-8977342b3108)
![PCB](https://github.com/user-attachments/assets/7b6a13cc-7e3f-42cd-a130-23ba62fd04e6)



## Module CH340E BTE17-06B
  ![image](https://github.com/user-attachments/assets/7e47a6a2-754b-4d04-b720-af1ff082dcb8)

- Thông số:
  - Có 2 chân nguồn cấp vào là VDD và 3v3. Trong đó VDD cho phép điện áp **3.3v tới 5v**, trong khi chân 3.3v có thẻ dùng để cấp cho mạch ngoài nhưng dòng tối đa 50mA.
- [Mua sắm, chọn đúng loại CH340E màu tím](https://shopee.vn/M%C3%B4-%C4%90un-Chuy%E1%BB%83n-%C4%90%E1%BB%95i-CH340E-CH340C-CH9340C-USB-Sang-TTL-5V-3.3V-CH340G-Chuy%C3%AAn-D%E1%BB%A5ng-Cho-Mini-i.578443443.16598012132). Lưu ý rằng loại CH340C màu đen thì có hiện tượng giao tiếp Serial với ESP32 được, nhưng không thể nạp code được
