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


## Module CH340E BTE17-06B
  ![image](https://github.com/user-attachments/assets/7e47a6a2-754b-4d04-b720-af1ff082dcb8)

- Thông số:
  - Có 2 chân nguồn cấp vào là VDD và 3v3. Trong đó VDD cho phép điện áp **3.3v tới 5v**, trong khi chân 3.3v có thẻ dùng để cấp cho mạch ngoài nhưng dòng tối đa 50mA.
- [Mua sắm, chọn đúng loại CH340E màu tím](https://shopee.vn/M%C3%B4-%C4%90un-Chuy%E1%BB%83n-%C4%90%E1%BB%95i-CH340E-CH340C-CH9340C-USB-Sang-TTL-5V-3.3V-CH340G-Chuy%C3%AAn-D%E1%BB%A5ng-Cho-Mini-i.578443443.16598012132). Lưu ý rằng loại CH340C màu đen thì có hiện tượng giao tiếp Serial với ESP32 được, nhưng không thể nạp code được
