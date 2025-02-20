# TRUYỀN THÔNG


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

## Bộ điều khiển từ xa không dây 4 kênh 4 Module không dây 433MHZ IC2262 / 2272

  ![Ảnh minh họa](https://down-vn.img.susercontent.com/file/7e2c6c7ab361b8449ff05bbee8660e0f.webp)
 - Thông số
    1.Điện áp hoạt động: 5V
    2.Dòng điện hoạt điện: 10mA @ 12V
    3. Công suất tăng: 10 mw @ 12V
    4. Chế độ điều chế: ASK (Điều chế biên độ)
    5. Tần số truyền: 433MHZ
    6. Khoảng cách truyền tín hiệu: 50-100M (không gian mở, độ nhạy của máy thu là -100dbm)
    7. Mã: mã cố định
- Bộ điều khiển nhựa là đầu phát. Mạch PCB có mã YK-04 là bộ thu. 4 nút trên bộ điều khiển khi bấm sẽ tương ứng với 4 chân D0-D3 trên bộ thu
   ![Ảnh mua sản phẩm](https://down-vn.img.susercontent.com/file/vn-11134103-7r98o-ltgf5k69uwi297.webp)
- [Mua sắm](https://shopee.vn/B%E1%BB%99-%C4%91i%E1%BB%81u-khi%E1%BB%83n-t%E1%BB%AB-xa-kh%C3%B4ng-d%C3%A2y-4-k%C3%AAnh-4-Module-kh%C3%B4ng-d%C3%A2y-433MHZ-IC2262-2272-i.201091220.5212508592)

## Module CH340E BTE17-06B
  ![image](https://github.com/user-attachments/assets/7e47a6a2-754b-4d04-b720-af1ff082dcb8)

- Thông số:
  - Có 2 chân nguồn cấp vào là VDD và 3v3. Trong đó VDD cho phép điện áp **3.3v tới 5v**, trong khi chân 3.3v có thẻ dùng để cấp cho mạch ngoài nhưng dòng tối đa 50mA.
- [Mua sắm, chọn đúng loại CH340E màu tím](https://shopee.vn/M%C3%B4-%C4%90un-Chuy%E1%BB%83n-%C4%90%E1%BB%95i-CH340E-CH340C-CH9340C-USB-Sang-TTL-5V-3.3V-CH340G-Chuy%C3%AAn-D%E1%BB%A5ng-Cho-Mini-i.578443443.16598012132). Lưu ý rằng loại CH340C màu đen thì có hiện tượng giao tiếp Serial với ESP32 được, nhưng không thể nạp code được
