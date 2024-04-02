# LINH KIỆN ĐIỆN TỬ

### Tấm PCB

- 5x7cm \
![20240327_135952](https://github.com/neittien0110/linhkiendientu/assets/8079397/fda9ea6e-77a6-4aa4-9a4a-8954faaee34a)
  [Mua sắm](https://shopee.vn/B%E1%BB%99-5-B%E1%BA%A3ng-M%E1%BA%A1ch-PCB-K%C3%ADch-Th%C6%B0%E1%BB%9Bc-5x7cm-5-*-7-Hai-M%E1%BA%B7t-T%E1%BB%B1-L%C3%A0m-K%C3%ADch-Th%C6%B0%E1%BB%9Bc-5x7cm-i.842225361.21834716941)

### Dây diện

 - Dây 30 awg, đơn lõi, nhỏ, mảnh, dai, xỏ xuyên lô của PCB thoải mái, phù hợp để hàn
   ![30 awg](https://github.com/neittien0110/linhkiendientu/assets/8079397/3bc621a0-3e66-40fb-b1ad-07e7855f7ad2)
   ![xỏ lỗ](https://github.com/neittien0110/linhkiendientu/assets/8079397/95bc8f20-d05e-466a-a6ad-7b5a020a9eb9)
   [Mua sắm](https://shopee.vn/Cu%E1%BB%99n-d%C3%A2y-%C4%91%E1%BB%93ng-c%C3%A1ch-nhi%E1%BB%87t-280m-30awg-B-30-1000-chuy%C3%AAn-d%E1%BB%A5ng-i.201091220.5642271126)

### MPU

-  MPU**9250** / MPU**6500** /  
  ![20240218_095519](https://github.com/neittien0110/linhkiendientu/assets/8079397/b4d4cd04-8c82-48e1-9c96-baf6b5fa8c58)
  - [Mua MPU 6500, mặc dù tên là 9250, nhưng thực tế là 6500](https://shopee.vn/M%C3%B4-%C4%90un-C%E1%BA%A3m-Bi%E1%BA%BFn-9-Tr%E1%BB%A5c-MPU-9250-GY-9250-I2C-SPI-Chuy%C3%AAn-D%E1%BB%A5ng-i.578443443.22041043458)

- NRF24L01: truyền dữ liệu không dây, tần số 2.4 GHz, giao tiếp **SPI**, cự li 200m. Cho phép truyền từ xa như xây dựng xe điều khiển bằng sóng Radio trực tiếp \
  ![image](https://github.com/neittien0110/linhkiendientu/assets/8079397/4996a4d0-8c2c-4f1a-81ae-f3ddff203a02)
  - [Mua sắm](https://shopee.vn/M%C3%B4-%C4%91un-truy%E1%BB%81n-d%E1%BB%AF-li%E1%BB%87u-kh%C3%B4ng-d%C3%A2y-NRF24L01-2.4G-2.4GHz-NRF24L01-phi%C3%AAn-b%E1%BA%A3n-n%C3%A2ng-c%E1%BA%A5p-NRF24L01-PA-LNA-1000-GT24-i.812409307.20422229589).  Lưu ý cố thể mua loại SMD không hàn pin, để tiện hàn lên PCB nhưng loại này sử dụng chân 1.25 mm

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
