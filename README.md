# LINH KIỆN ĐIỆN TỬ

## Mục lục

1. [Các shield mở rộng cho board dạng D1 mini](./D1mini.md)
2. [Các loại motor](./Motors.md)
3. [Các module truyền thông](./Communications.md)
4. [Các màn hình hiển thị](./Screens.md)
5. [Các linh vật tư phụ kiện như mạch in, dây dẫn, thiếc](./noname.md)

### MPU

-  MPU**9250** / MPU**6500** /  
  ![20240218_095519](https://github.com/neittien0110/linhkiendientu/assets/8079397/b4d4cd04-8c82-48e1-9c96-baf6b5fa8c58)
  - [Mua MPU 6500, mặc dù tên là 9250, nhưng thực tế là 6500](https://shopee.vn/M%C3%B4-%C4%90un-C%E1%BA%A3m-Bi%E1%BA%BFn-9-Tr%E1%BB%A5c-MPU-9250-GY-9250-I2C-SPI-Chuy%C3%AAn-D%E1%BB%A5ng-i.578443443.22041043458)

### Khác

- Đo lượng oxi và nhịp tim MAX102 \
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

- Bộ tắt/bật AC-220V, điều khiển bằng RF 433MHz. Đã có sẵn chuyển đổi AC-DC để nuôi mạch RF nên không cần nguòn DC.\
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
  - [Mua sắm](https://shopee.vn/M%C3%B4-%C4%91un-C%C3%B4ng-T%E1%BA%AFc-Truy%E1%BB%81n-Nh%E1%BA%ADn-T%C3%ADn-Hi%E1%BB%87u-Kh%C3%B4ng-D%C3%A2y-RF-Dc-220V-1-K%C3%AAnh-433MHz-i.201091220.7509764367)

- Ky-023 Joystick Nút Điều Khiển JoyStick PS2 STM32 Cho Tay Cầm Chơi Game \
  ![Ky-023](https://github.com/neittien0110/linhkiendientu/assets/8079397/b2ae4aa5-44e2-4f26-aab2-f59fbf2aab3a)\
  ```plain
  1. Điện áp hoạt dộng: DC 3.3V~5V
  2. Pin JRX và JRY: 2 chân analog, là 2 biến trở cho biết mức độ kéo theo phương X và phương Y.
  3. Pin SW: =1 nếu Joystick được bấm. 
  ```
  - [Mua sắm](https://shopee.vn/M%C3%B4-%C4%91un-c%E1%BA%A3m-bi%E1%BA%BFn-5-pin-tr%E1%BB%A5c-k%C3%A9p-X-Y-cho-tay-c%E1%BA%A7m-ch%C6%A1i-game-Ps2-Ky-023-i.148048328.7241683324)

- Bàn phím ma trận 4x5, 4x4, 4x3
  - ![Bàn phím ma trận](https://github.com/neittien0110/linhkiendientu/assets/8079397/93ed6070-e95a-4c00-bcd4-20367764aa88)
  - [Hướng dẫn lập trình](http://arduino.vn/bai-viet/915-huong-dan-su-dung-module-ban-phim-4x4-voi-arduino)
  - [Mua sắm](https://shopee.vn/B%C3%A0n-Ph%C3%ADm-16-Ph%C3%ADm-4x4-4x4-4-*-4-Matrix-Array-Matrix-i.81431289.20537984830)

- Tect6000 - Transistor ánh sáng  nồi đồng cối đá
  - Phải mắc thêm trở như hình dưới\
    ![Cách mặc mạch](https://github.com/neittien0110/linhkiendientu/assets/8079397/d7ff5a29-b269-4eae-b5e0-96e900c24c3f)
     
  - [Mua sắm](https://shopee.vn/Set-1206-C%E1%BA%A3m-Bi%E1%BA%BFn-Nhi%E1%BB%87t-%C4%90%E1%BB%99-Tect6000-B%E1%BA%A3o-V%E1%BB%87-M%C3%B4i-Tr%C6%B0%E1%BB%9Dng-TEMT6000X01-i.972724310.22849595571)

- Module cảm biến rung \
  ![Module cảm biến rung](https://github.com/neittien0110/linhkiendientu/assets/8079397/f7f86d6f-51d5-4432-9f28-a93878fa076d)
  - Vcc = 3.3~5V  
  - [Mua sắm](https://shopee.vn/M%C3%B4-%C4%91un-c%E1%BA%A3m-bi%E1%BA%BFn-rung-3.3v-5v-chuy%C3%AAn-d%E1%BB%A5ng-d%C3%A0nh-cho-arduino-uno-r3-i.325406709.8705690745)

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
