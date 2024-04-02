# CÁC LINH KIỆN DÀNH RIÊNG CHO DÒNG BOARD WEMOS D1 MINI

1. Màn hình oled 0.66" 

![Màn hình oled 0.66" ](https://github.com/neittien0110/linhkiendientu/assets/8079397/0345bcad-891b-4011-90d1-d04f9f6ba400)

  ```
  Điểm ảnh: 64x48
  Điện áp hoạt động: 3.3V 
  Ic trình điều khiển: SSD1306 
  Giao diện: IIC (I2C) 
  Địa chỉ IIC: 0x3C hoặc 0x3D
  ```

  |D1 mini trên board|GPIO trên MCU|Oled Shield|
  |--|--|--|
  |D1|5|SCL|
  |D2|4|SCA|
  
  - [Tài liệu của hãng Wemos](https://www.wemos.cc/en/latest/d1_mini_shield/oled_0_66.html)
  - [Mua sắm](https://shopee.vn/product/770245757/16467277917)
  
2. Relay (Rơ le) đơn kênh AC 250V

![Relay (Rơ le) đơn kênh AC 250V](https://github.com/neittien0110/linhkiendientu/assets/8079397/d9e46094-b61f-43f3-be2b-87ab3933a368)

  |D1 mini trên board|GPIO trên MCU|Relay Shield|
  |--|--|--|
  |D1|5|Điều khiển relay tắt bật|
  > Relay chính hãng cho phép cấu hình để chuyển từ chân mặc định D1, thành chân pin khác. Tuy nhiên, loại rẻ tiền không thể.
  
  - [Tài liệu của hãng Wemos](https://www.wemos.cc/en/latest/d1_mini_shield/relay.html)
  - [Mua sắm](https://shopee.vn/M%C3%B4-%C4%91un-r%C6%A1-le-WEMOS-D1-mini-ESP8266-chuy%C3%AAn-d%E1%BB%A5ng-ch%E1%BA%A5t-l%C6%B0%E1%BB%A3ng-cao-i.148048328.5320322534)
