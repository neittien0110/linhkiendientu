# NGUỒN CẤP

Lượt mua 1\
![5 loại mạch sạc](https://github.com/neittien0110/linhkiendientu/assets/8079397/0b6255f2-a802-4468-9825-3dca0ae40674)\
Lượt mua 2\
  [trái trên](#mp1584en-buck-hạ-áp-từ-24v12v9v5v-ra-3v3---đầu-ra-có-thể-điều-chỉnh-hoặc-cố-định-áp), [phải trên](#mô-đun-sạc-pin-lithium-giảm-xả-5v2a--24a--có-đầu-vàođầu-ra-thường-mở)\
  [trái giữa](mini560-buck-hạ-áp-đầu-ra-33v), [phải giữa](#mini-360-module-hạ-áp-có-điều-chỉnh-bằng-chiết-áp-một-biến-thể-khác)\
  [trái dưới](#cr-1850s-buck-vào-45--18v-ra-3v3), [phải dưới](#module-sạc-xả-pin-lithium-với-đầu-ra-42v)\
  ![6 loại module](https://github.com/user-attachments/assets/6bab7762-b1da-4cea-b58b-7382c279bbcc)\
  
- [IC nguồn AMS1117 và các module liên quan](#ic-nguồn-ams1117-và-các-module-liên-quan)
  - [Module nguồn ổn áp dùng AMS1117](#module-nguôn-ổn-áp-dùng-ams1117)
- [Module chuyển đổi AC 220V --> DC 5V/0.7A](#module-chuyển-đổi-ac-220v----dc-5v07a)
- [HW-626 module tăng áp 5V](#hw-626-module-tăng-áp-5v)
- [Mini-360 module hạ áp có điều chỉnh bằng chiết áp](#mini-360-module-hạ-áp-có-điều-chỉnh-bằng-chiết-áp)
- [Mini560 buck hạ áp đầu ra 3.3V](#mini560-buck-hạ-áp-đầu-ra-33v)
- [Mini-360 module hạ áp có điều chỉnh bằng chiết áp (một biến thể khác)](#mini-360-module-hạ-áp-có-điều-chỉnh-bằng-chiết-áp-một-biến-thể-khác)
- [MP1584EN buck hạ áp từ 24V/12V/9V/5V ra 3v3 - Đầu ra có thể điều chỉnh (hoặc cố định áp)](#mp1584en-buck-hạ-áp-từ-24v12v9v5v-ra-3v3---đầu-ra-có-thể-điều-chỉnh-hoặc-cố-định-áp)
- [CR-1850S buck vào 4,5 ~ 18V ra 3V3](#cr-1850s-buck-vào-45--18v-ra-3v3)
- [Mô đun tăng áp 0.9-5V sang 5V](#module-tăng-áp-09-5v-sang-5v)
- [Mạch sạc, bảo vệ pin lithium 1 cell, cổng usb type-C](#mạch-sạc-bảo-vệ-pin-lithium-1-cell-cổng-usb-type-c)
- [Mạch sạc Lithium bao gồm màn hình của tẩu thuốc lá điện tử](#mạch-sạc-lithium-bao-gồm-màn-hình-của-tẩu-thuốc-lá-điện-tử)
- [Mạch sạc Lithium bao gồm màn hình của tẩu thuốc lá điện tử Rifbar Turbo](#mạch-sạc-lithium-bao-gồm-màn-hình-của-tẩu-thuốc-lá-điện-tử-rifbar-turbo)
- [Mạch sạc Lithium có màn hình nhỏ](#mạch-sạc-lithium-có-màn-hình-nhỏ)
- [Mạch sạc Lithium có màn hình nhỏ 2](#mạch-sạc-lithium-có-màn-hình-nhỏ-2)
- [Mạch sạc MH-CD42 có nút Key nhưng không usb](#mạch-sạc-mh-cd42-có-nút-key-nhưng-không-usb)
- [Module sạc xả pin Lithium với đầu ra 4.2v](#module-sạc-xả-pin-lithium-với-đầu-ra-42v)
- [Mô-đun sạc pin Lithium giảm xả 5V2A / 2.4A  có đầu vào/đầu ra thường mở](#mô-đun-sạc-pin-lithium-giảm-xả-5v2a--24a--có-đầu-vàođầu-ra-thường-mở)
- [Mạch sạc LX-LBC3 5v](#mạch-sạc-lbc3)
- [Mạch sạc pin type-C 3.7v](#mạch-sạc-pin-type-c-37v)
- [Sạc pin lithium cổng USB Type C ra 5V 2A có nút K](#sạc-pin-lithium-cổng-usb-type-c-ra-5v-2a-có-nút-k)
- [LX-LCBST sạc pin lithium và kiêm xả pin có điều chỉnh điện áp](#lx-lcbst-sạc-pin-lithium-và-kiêm-xả-pin-có-điều-chỉnh-điện-áp)
- [HW-357 Sạc pin lithium và kiêm tăng áp booster](#hw-357-sạc-pin-lithium-và-kiêm-tăng-áp-booster)
- [Board điều khiển đèn pin sạc](#board-điều-khiển-đèn-pin-sạc)
- [Đế pin và pin](#đế-pin-và-pin)
  - [Pin 10440 và đế. Pin AAA](#pin-10440-và-đế-pin-aaa)
  - [Pin 14250 và đế.](#pin-14250-và-đế)
  - [Pin 14500 và đế. Pin AA](#pin-14500-và-đế-pin-aa)
  - [Pin 16430 và đế.](#pin-16430-và-đế)
  - [Pin 18650 và đế](#pin-18650-và-đế)

[Xem thêm các module nguồn có thư viện easyeda, lcsc](./EasyEDA_Library.md)

## IC nguồn AMS1117 và các module liên quan

  ![image](https://github.com/user-attachments/assets/2e4109d8-ff87-4a24-9fa3-deb7e6ec5f16)

- Mô tả:
  - Có thể hàn trực tiếp AMS1117 lên PCB cắm vì khoảng cách giữa 3 pin là 2.23mm (~2.54mm). Trường hợp tệ nữa thì bỏ qua tụ lọc, cứ hàn duy nhất AMS1117.
  - Đã ghi nhận module AMS1117 có sẵn trên các module ổn áp không đúng. Phải replace thì module mới chạy được.

- [Mua sắm AMS1117 3v3](https://shopee.vn/B%E1%BB%99-50-Linh-Ki%E1%BB%87n-%C4%90i%E1%BB%87n-T%E1%BB%AD-AMS1117-LDO-SOT-223-AMS1117-3.3V-1.2V-1.5V-1.8V-2.5V-5.0V-ADJ-AMS1117-LM1117-11117-i.762880341.19239851949)
- [Mua sắm AMS1117 5v](https://shopee.vn/B%E1%BB%99-50-Linh-Ki%E1%BB%87n-%C4%90i%E1%BB%87n-T%E1%BB%AD-AMS1117-LDO-SOT-223-AMS1117-3.3V-1.2V-1.5V-1.8V-2.5V-5.0V-ADJ-AMS1117-LM1117-11117-i.762880341.19239851949)

### Module nguôn ổn áp dùng AMS1117

- Schematic, Footprint\
  ![Schematic](https://github.com/user-attachments/assets/4ecc98be-0662-41ac-967b-cc05c7ad4a40))
  ![pcb](https://github.com/user-attachments/assets/709aae76-57b3-48d1-8913-a9e84563c85d)

  [easyeda](https://easyeda.com/editor#id=83ae564cc18f40ada42dd9197d966455|508dd84037644c9a8733925a4745d4fd|7176a7f8643d4ade9dfa48dc8249514c)
  - [Mua sắm](https://shopee.vn/Ams1117-1.2V-1.5V-1.8V-2.5V-3.3V-5V-M%C3%B4-%C4%91un-c%E1%BA%A5p-ngu%E1%BB%93n-AMS1117-5.0V-M%C3%B4-%C4%91un-ngu%E1%BB%93n-AMS1117-3.3V-Cho-b%E1%BB%99-t%E1%BB%B1-l%C3%A0m-i.578443443.25185784279?sp_atk=12c5d8f2-042e-404b-ba21-18e91ceacc1b&xptdk=12c5d8f2-042e-404b-ba21-18e91ceacc1b)
   > Lưu ý: Đã ghi nhận module AMS1117 có sẵn trên các module ổn áp không đúng. Phải replace thì module mới chạy được.

## Module chuyển đổi AC 220V --> DC 5V/0.7A

  ![Mô đun hạ áp 5V 700mA (3.5W) ](https://github.com/neittien0110/linhkiendientu/assets/8079397/f3d0672b-4d9d-41c3-8161-97430e645f51)

- Thông số:
  - Hiệu suất: 80%
- Ý nghĩa sử dụng: xây dựng các module thu thập dữ liệu tiện lợi, lấy nguồn từ ổ cắm 220V
- [Mua sắm](https://shopee.vn/M%C3%B4-%C4%90un-H%E1%BA%A1-%C3%81p-5V-700mA-(3.5W)-AC-DC-220V-5V-i.578443443.16971764350)

## HW-626 module tăng áp 5V

![HW-626 1](https://github.com/neittien0110/linhkiendientu/assets/8079397/90339a0d-07ea-4c27-84d0-15087571f061)
![HW-626 2](https://github.com/neittien0110/linhkiendientu/assets/8079397/b84f7fa6-f92c-4835-8180-2d697d7180af)

- Thông số:
  - Điện áp vào: 0.9V ~ 5V (Nếu quá 5V sẽ cháy)
  - Điện áp ra: 5V
  - Cường độ dòng xả: 480 mA
  - Kích thước: 11 *10,5* 7,5mm
  - Hiệu suất: 85%
  - Tần số biến đổi điện áp: 150kHz
- Sử dụng:\
  ![HW-626 sử dụng](https://github.com/neittien0110/linhkiendientu/assets/8079397/e3ab22c7-6828-4853-a5d4-34e48d06b939)
- Nguyên lý:
  ![Chu kì nạp/phóng](https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Boost_operating.svg/200px-Boost_operating.svg.png)
  ![Minh họa chu kì phóng](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Boost_converter_anim.gif/400px-Boost_converter_anim.gif)
- [Mua sắm](https://shopee.vn/M%C3%B4-%C4%91un-t%C4%83ng-%C3%A1p-0.9-5V-sang-5V-1.5V-1.8V-2.5V-3V-3.3V-3.7V-4.2V-sang-5V-thay-th%E1%BA%BF-ti%E1%BB%87n-d%E1%BB%A5ng-i.578443443.11667335774)  

## Mini-360 module hạ áp có điều chỉnh bằng chiết áp

  ![image](https://github.com/neittien0110/linhkiendientu/assets/8079397/7daa1d98-b675-4837-a487-94a8532c80c5)
  ![image](https://github.com/user-attachments/assets/0d4f52e5-a5a0-45c9-9b15-31bb1eb5e340)

  > Xem thêm module có vẻ hay hơn [Mini-360 module hạ áp có điều chỉnh bằng chiết áp (một biến thể khác)](#mini-360-module-hạ-áp-có-điều-chỉnh-bằng-chiết-áp-một-biến-thể-khác), kích thước y hệt

- Thông số:
  - Tên model: Mini-360 (mô-đun buck chỉnh lưu đồng bộ kích thước cực nhỏ DC-DC)
  - Thuộc tính mô-đun: Không bị cô lập
  - Chỉnh lưu: Chỉnh lưu đồng bộ
  - Điện áp đầu vào: 4,75V-23V
  - Điện áp đầu ra: 1.0V-17V
  - Dòng điện đầu ra: Giảm mức 3A, dài 1.8A
  - Hiệu suất chuyển đổi: 96% (tối đa)
  - Tần số chuyển đổi: 340KHz
  - Độ gợn sóng đầu ra: 30mV (không tải)
  - Điều chỉnh tải: ± 0,5%
  - Điều chỉnh điện áp: ± 2,5%
  - Nhiệt độ hoạt động: -40 độ C đến +85 độ C
- [Mua sắm](https://shopee.vn/M%C3%B4-%C4%91un-h%E1%BA%A1-%C3%A1p-mini360-mini-360-DC-th%E1%BA%A5p-h%C6%A1n-LM2596-i.578443443.12390124552)
- [Xem thêm các module nguồn có thư viện easyeda ,lcsc](./EasyEDA_Library.md)

## Mini-360 module hạ áp có điều chỉnh bằng chiết áp (một biến thể khác)

![image](https://github.com/user-attachments/assets/fa353b46-ae82-486b-b2b5-7173c4d7dd4c)
![image](https://github.com/user-attachments/assets/1ce9f5bb-41bc-4927-8c81-20b641a3c8aa)
![image](https://github.com/user-attachments/assets/1d9e0b8d-a4b1-4ad9-aec5-dfb58f6f5b77)

- Ưu điểm: board có chân [Castellated Holes](https://morepcb.com/wp-content/uploads/2023/07/PCB-Edges-and-Castellated-Holes.png) để tiện dán trực tiếp lên board khác

- So sánh mini360 màu xanh và mini360 biến thể màu đen
  ![so sánh 1](https://github.com/user-attachments/assets/0119689f-fc1b-4934-a8ed-177c8ef5b997)
  ![so sánh mặt trên](https://github.com/user-attachments/assets/1abfe4b1-5d3f-44a7-a3cd-47b330370f2e)
  ![so sánh mặt đáy](https://github.com/user-attachments/assets/947b4683-d454-4d7f-9bf9-cbade7282ab9)

- Module mini360 màu đen bên phải ở giữa\
  ![6 loại module](https://github.com/user-attachments/assets/6bab7762-b1da-4cea-b58b-7382c279bbcc)

- [Mua sắm](https://shopee.vn/Dc-dc-3A-Mini-Buck-M%C3%B4-%C4%91un-Ngu%E1%BB%93n-%C4%91i%E1%BB%87n-%C3%B4-t%C3%B4-6V9V12V-30V-%C4%91%E1%BA%BFn-3.3V-5V-%C4%90%E1%BA%A7u-ra-i.1456687807.27374003733)

## Mini560 buck hạ áp đầu ra 3.3V

![image](https://github.com/user-attachments/assets/5cd83fb0-cfc2-433f-9b21-8bb3a2958cf7)

- Đã test thử với đầu vào USB Type-C thì đầu ra 3v4
- Nhược điểm: lỗ to hơn 2.54mm, mạch khá lớn
- Thông số:
  - Điện áp đầu vào: 5V-20V
  - Đầu ra: 3.3v, < 5A (Khoảng cách dài chạy trên 4A cần để thêm tản nhiệt)
  - Chênh lệch điện áp In-Out: > 1.7V
  - Tần số chuyển đổi: 500KHz
  - Hiệu suất chuyển đổi: 99% (Cao nhất)
  - Nhiệt độ làm việc: -40℃Đến + 85℃
  - Chế độ chỉnh lưu: Bộ chỉnh lưu đồng bộ
- [Mua sắm](https://shopee.vn/Dc-dc-mini560-DC-Buck-B%E1%BB%99-%C4%91i%E1%BB%81u-ch%E1%BB%89nh-%C4%91i%E1%BB%87n-%C3%A1p-M%C3%B4-%C4%91un-ngu%E1%BB%93n-Hi%E1%BB%87u-su%E1%BA%A5t-cao-%C4%90%E1%BA%A7u-ra-3.3V-5V-9V-12V-5A-i.1456687807.25840639942)

## MP1584EN buck hạ áp từ 24V/12V/9V/5V ra 3v3 - Đầu ra có thể điều chỉnh (hoặc cố định áp) 

![image](https://github.com/user-attachments/assets/3c3fb27f-82fb-482a-9a9a-fd37ddfa95e3)
![image](https://github.com/user-attachments/assets/08e93326-bf0d-49f7-9af5-4e6a446c401f)
Ảnh chụp thật
![image](https://github.com/user-attachments/assets/58e93057-4762-427b-beeb-8ac002d6e4e2)
![image](https://github.com/user-attachments/assets/79292227-364d-42b0-bba8-ba81fa670d5b)
- Module MP1584EN màu đen bên trái ở trên\
  ![6 loại module](https://github.com/user-attachments/assets/6bab7762-b1da-4cea-b58b-7382c279bbcc)
- Ưu điểm: board có chân [Castellated Holes](https://morepcb.com/wp-content/uploads/2023/07/PCB-Edges-and-Castellated-Holes.png) để tiện dán trực tiếp lên board khác
- Nhược điểm: khoảng cách giữa các cụm 2 chân pin là không chẵn cho 2.54mm nên cắm Breadboard được, không căm lên PCB Test được.\
  ![image](https://github.com/user-attachments/assets/3309925a-f4c3-45d8-ae2a-c92a46011ab5)
- đã test ok khi kết hợp với module sạc và xả tăng áp 5v, để có đầu ra 3v3)\
  ![image](https://github.com/user-attachments/assets/6fca43ec-89c3-43e7-9299-8c4ed460b10a)
- Thông số:
  - Điện áp đầu vào: 5.3V-26V
  - Điện áp đầu ra: 3.3V
  - Dòng điện đầu ra: < 3A. Kiểm soát làm việc trong thời gian dài trong vòng 1.8A
  - Hiệu suất chuyển đổi: 96% (Đỉnh)
  - Chênh lệch điện áp Vin-Vou > 2V. Càng nhỏ, Hiệu quả càng cao
  - Ripple đầu ra: < 30mV
  - Nhiệt độ làm việc: -40°C ~ + 85°C
  - Kích thước mô-đun: 22,3 * 17 * 4,2mm
- Ở đầu vào, đã test cắm ngược cực In+, In- thì mạch sẽ bị nóng, nhưng không hỏng.
- [Mua sắm](https://shopee.vn/Dc-dc-B%E1%BA%A3ng-b%C6%B0%E1%BB%9Bc-xu%E1%BB%91ng-3A-B%E1%BB%99-%C4%91i%E1%BB%81u-ch%E1%BB%89nh-%C4%91i%E1%BB%87n-%C3%A1p-M%C3%B4-%C4%91un-ngu%E1%BB%93n-24V-12V-9V-%C4%91%E1%BA%BFn-3.3V5V-%C4%90%E1%BA%A7u-ra-c%C3%B3-th%E1%BB%83-%C4%91i%E1%BB%81u-ch%E1%BB%89nh-MP1584EN-i.1456687807.27374129575)

## CR-1850S buck vào 4,5 ~ 18V ra 3V3 

![image](https://github.com/user-attachments/assets/c535385d-8c10-444f-92d6-34ddae2524c3)

 - Đã test thử với đầu vào từ USB Type-C 5v thì cho đầu ra 3v4.\
   ![image](https://github.com/user-attachments/assets/c75e688d-d310-4d68-a308-18392fee7434)

- Ưu điểm:
  - board có chân [Castellated Holes](https://morepcb.com/wp-content/uploads/2023/07/PCB-Edges-and-Castellated-Holes.png) để tiện dán trực tiếp lên board khác
  - 2 chân pin theo chiều ngang thì chẵn theo 2.54mm
  - 2 chân pin theo chiều dọc thì phải 1 lỗ tròn và một lỗ Castellated mới chẵn theo 2.54mm.
- Nhược điểm:
  - Chỉ phù hợp với áp vào cao. 5v đã là thấp rồi.

- Thông số:
  - Điện áp vào: 5v - 18V
  - Dòng ra hiện tại tối đa 5A
  - Chênh lệch điện áp **Vin-Vout: > 1V**
  - Dòng tĩnh 0,2ma
  - Hiệu suất chuyển đổi lên đến 95%  
  - Bảo vệ ngắn mạch đầu ra gợn sóng thấp 400khz
- Về vấn đề nhiệt độ:
  - Phạm vi nhiệt độ hoạt động: -40°C đến + 150°C
  - Tích hợp bảo vệ quá nhiệt
  - Dòng cực đại 6A, có thể liên tục đầu ra 5A trong thời gian ngắn (Chip sẽ bảo hiểm quá nhiệt) và nên có thêm thanh tản nhiệt
  - Nếu ko có tản nhiệt, điện áp ra ổn định ở mức 3.3V 3,8A
- Độ dày của bảng là 4,5mm.
- Với module đầu ra 3v3, hoặc 5v thì sử dụng điện cảm 3R3 (Sẽ có một số lỗi trong các lô điện cảm khác nhau)
- Giao diện của bảng mạch:
  - Trong IN +: Đầu vào Dc Tích cực 4,5V-18V
  + Cực âm đầu vào In-, cực âm đầu ra, đều được nối thông với nhau
  + Sử dụng **dây đồng đấu nối phải đủ dày** để chịu dược dòng cao
 - Thư viện EasyEDA:
   ![image](https://github.com/user-attachments/assets/d26f87ab-a6bf-4b75-8e9a-3ba2589e0cfd)
 - [Mua sắm](https://shopee.vn/Dc-dc-Buck-M%C3%B4-%C4%91un-ngu%E1%BB%93n-%C4%90%E1%BA%A7u-v%C3%A0o-6-5-~-16V-%C4%91%E1%BA%BFn-5V-M%C3%B4-%C4%91un-%C4%91i%E1%BB%81u-ch%E1%BB%89nh-%C4%91i%E1%BB%87n-%C3%A1p-Ch%C3%A2n-4A-18V-Gi%C3%A1-tr%E1%BB%8B-%C4%91%E1%BB%89nh-6A-i.1456687807.28324156443)

## Module tăng áp 0.9-5V sang 5V

  ![Mô đun tăng áp 0.9-5V sang 5V](https://github.com/user-attachments/assets/4b04538b-44b5-4156-b5a8-f5dd588fd862)

- Vào: điện áp từ 0.9 tới 5V (nhưng không quá 5V)
- Ra: 5V, dòng tối đa 480mA
- Nếu áp đầu vào 0.8V thì đầu ra chỉ có 7mA
- Tần số hoạt động: 150KHz
- Hiệu suất chuyển đổi điển hình: 85%
- Kích thước: 11*10,5*7,5mm
- [Mua sắm](https://shopee.vn/M%C3%B4-%C4%91un-t%C4%83ng-%C3%A1p-0.9-5V-sang-5V-1.5V-1.8V-2.5V-3V-3.3V-3.7V-4.2V-sang-5V-thay-th%E1%BA%BF-ti%E1%BB%87n-d%E1%BB%A5ng-i.578443443.11667335774)

## Mạch sạc, bảo vệ pin lithium 1 cell, cổng usb type-C

 ![Mặt trước](https://github.com/user-attachments/assets/2380024b-18dc-442a-809f-6d27fc04010a) \
 ![Mặt sau](https://github.com/user-attachments/assets/cb8b3304-9575-4929-a528-08e374275941) \

- Có led báo tải đầu ra, màu trắng mờ là không tải, trắng sáng là tải cao.
- Có 4 chân out, nhưng thực chất là từng cặp 2 pin được nối với nhau và đấu sẵn dây để nối pin lithium 1 cell. Điện áp sạc 4.0~4.2V
  ![trước](https://github.com/user-attachments/assets/a2aa2509-1192-416d-9f1b-86398889dac3)
  ![sau](https://github.com/user-attachments/assets/207bd6ed-3916-4cbe-b895-dbbfd462ad64)

- Lưu ý: chỉ để sạc pin. Không có chức năng ổn định điển áp xả
- [Mua sắm](https://vn.shp.ee/U41J8Mi)

## Mạch sạc Lithium bao gồm màn hình của tẩu thuốc lá điện tử

  ![image](https://github.com/user-attachments/assets/771d7522-3ade-4b06-93b2-af6c7c79852b)\
  [Video](https://cvf.shopee.vn/file/api/v4/11110107/mms/vn-11110107-6khwe-m3w6qtvxfkqk3c.16000071734444452.mp4)
  
- Thông số
  - kích thước mạch 7cm x 2cm cao 0.5cm
  - màn hình 2.8 x 1.4cm
  - Có điều chỉnh được công suất
  - Có time lapse
- Chú ý: hàng tháo lắp từ máy móc nào đó, không có nguồn gốc, khả năng cao là mạch sạc châm thuốc lá điện tử
- [Mua sắm](https://shopee.vn/m%E1%BA%A1ch-linh-ki%E1%BB%87n-%C4%91i%E1%BB%87n-t%E1%BB%AD-c%C3%B3-m%C3%A0n-h%C3%ACnh-ko-r%C3%B5-th%C3%B4ng-s%E1%BB%91-gi%C3%A1-b%C3%A1n-cho-a.e-nghi%C3%AAn-c%E1%BB%A9u.-i.523359606.26520937742)

## Mạch sạc Lithium bao gồm màn hình của tẩu thuốc lá điện tử Rifbar Turbo

  ![image](https://github.com/user-attachments/assets/b2806c31-2e30-4fe9-81d3-ebf6fd15869a)
  ![image](https://github.com/user-attachments/assets/319e6e8a-0d39-4221-8b33-64256152e7cd)\
  [video](https://down-ws-sg.vod.susercontent.com/api/v4/11110107/mms/vn-11110107-6khwg-m6yyplg6oiw194.16000071741150273.mp4)

- Thông số
  - dành cho pin __3.7v /0.5A__ sạc đầy là 4.2v / 18650 . lithium . lipo...
  - dòng sạc 0.5 A
  - có công tắc gạt để tắt/bật
  - 1 motor rung

- [Mua sắm](https://shopee.vn/m%E1%BA%A1ch-s%E1%BA%A1c-pin-c%C3%B3-m%C3%A0n-h%C3%ACnh-hi%E1%BB%83n-th%E1%BB%8B-s%E1%BA%A1c-pin-3.7v-ch%C3%A2n-s%E1%BA%A1c-type-c-i.523359606.24042209767)

## Mạch sạc Lithium có màn hình nhỏ

  ![image](https://github.com/user-attachments/assets/1c521e39-459b-420d-b957-0b3285d9f53b)
  [Video](https://down-zl-sg.vod.susercontent.com/api/v4/11110107/mms/vn-11110107-6khw8-m4rgbbl9g3n4f1.16000071736337108.mp4)
  
- Thông số
  - dành cho pin __3.7v /0.5A__ sạc đầy là 4.2v / 18650 . lithium . lipo...
  - tự ngắt khi đầy pin
  - khi gần đầy pin mạch sẽ tự động hạ dòng sạc để bảo vệ pin không bị chai
  - USB Type-C
- Sử dụng:
  - Đấu nối dây đen đỏ và cực pin là sạc được luôn
  - KHÔNG xả pin
  - Có chân D+, D- nên khả năng là có giao tiếp USB 2.0\
    ![image](https://github.com/user-attachments/assets/040c09c6-421c-42a3-acaf-fab74358dcf6)
  - Và có 3 chân M+, MG, M- chưa rõ mục đích\
    ![image](https://github.com/user-attachments/assets/bcc3a520-b6e7-4a08-82a0-0b40247433d9)
- [Mua sắm](https://shopee.vn/m%E1%BA%A1ch-s%E1%BA%A1c-pin-c%C3%B3-m%C3%A0n-h%C3%ACnh-hi%E1%BB%83n-th%E1%BB%8B-pin-3.7v-0.5A-ch%C3%A2n-s%E1%BA%A1c-type-c.-i.523359606.24840283168)

## Mạch sạc Lithium có màn hình nhỏ 2

  ![image](https://github.com/user-attachments/assets/5d401d8b-3bb7-42b3-9479-14b652fea47d)\
  [Video](https://down-bs-sg.vod.susercontent.com/api/v4/11110107/mms/vn-11110107-6khwh-m3x2lmqs1meg72.16000071734498017.mp4)

- Thông số
  - dành cho pin __3.7v /0.5A__ sạc đầy là 4.2v / 18650 . lithium . lipo...
  - tự ngắt khi đầy pin
  - khi gần đầy pin mạch sẽ tự động hạ dòng sạc để bảo vệ pin không bị chai
  - USB Type-C
  - Có motor rung
  - Có 2 dây H+, H-
- Sử dụng:
  - Đấu nối dây đen đỏ và cực pin là sạc được luôn
  - KHÔNG xả pin  
- [Mua sắm](https://shopee.vn/m%E1%BA%A1ch-s%E1%BA%A1c-pin-c%C3%B3-m%C3%A0n-h%C3%ACnh-hi%E1%BB%83n-th%E1%BB%8B-pin-3.7v-0.5A-ch%C3%A2n-s%E1%BA%A1c-type-c-i.523359606.28020978193)

## Mạch sạc MH-CD42 có nút Key nhưng không usb

Phiên bản chuẩn, tự tắt nếu dòng tải thấp (Footkeyboard là không đủ 50mA, vẫn bị tắt)
![Phiên bản chuẩn](https://github.com/neittien0110/linhkiendientu/assets/8079397/c848dfda-a559-4a2f-9240-a1ca9779ec2f)

Phiên bản cải tiến, không tự tắt
![Phiên bản cải tiến](https://github.com/user-attachments/assets/fb7a3294-caf9-496a-ad42-ffa75ae81ed7)

- Thông số:
  - 3 cặp lỗ PCB để Vào 5V
  - có 4 led chỉ định mức pin;
  - có __nút bấm K__ và  __pad K tự hàn__
  - công suất vẫn __KHÔNG ĐỦ__ để nuôi 1 serve sg90 cho thùng rác
  - Điện áp đầu vào: DC 4v5 ~ 5v5
  - Điện áp đầu ra:  DC __5v__
  - Dòng sạc : 02.1A
  - Dòng xả pin : 03.5A
  - Điện áp khi đầy pin: 4.2VDC
  - Hiệu suất : 96%
  - Điện áp đầu ra : 5VDC
  - Dòng áp ra : 02.4A
  - Nhiệt độ : -20~85 độ
  - Kích thước : 16x25mm
- CÓ 2 PHIÊN BẢN:
  1. Phiên bản Tiêu Chuẩn màu đen: nếu tải nhỏ hơn 50mA, đầu ra (OUT 5V) sẽ bị tắt sau 30 giây: nếu tải lớn hơn 50mA, đầu ra sẽ được bật liên tục. Để bỏ chức năng này cho một số mạch tiết kiệm năng lượng (như Vi điều khiển ở chế độ Sleep) cứ sau chu kỳ <20s ta dùng chân IO kích 1 xung LOW (duy trì 100ms) vào chân Key (tương đương 1 cái nhấn - nhả)...hoặc mua Phiên bản Cải Tiến để tránh mất thời gian.
  2. __Phiên bản Cải Tiến màu trắng: Dù có tải hay không tải thì vẫn luôn xuất ra nguồn 5V__. 
- [Video](https://youtu.be/7wipikQeQaM?si=ZpH4JvTmLkixtUVS)
- [Mua sắm bản tiêu chuẩn](https://shopee.vn/B%E1%BA%A3ng-M%E1%BA%A1ch-T%C4%83ng-%C3%81p-DC-5V-2.1A-4.2V-3.7V-lithium-18650-Ch%E1%BA%A5t-L%C6%B0%E1%BB%A3ng-Cao-i.578443443.17381782504)
- [Mua sắm bản cải tiến](https://shopee.vn/Mh-cd42-DC-5V-2.1A-B%E1%BA%A3ng-t%E1%BB%B1-l%C3%A0m-ngu%E1%BB%93n-di-%C4%91%E1%BB%99ng-4.2V-S%E1%BA%A1c-X%E1%BA%A3-(t%C4%83ng-c%C6%B0%E1%BB%9Dng)-b%E1%BA%A3o-v%E1%BB%87-pin-m%C3%B4-%C4%91un-ch%E1%BB%89-b%C3%A1o-3.7V-lithium-18650-i.176393725.24721940429?xptdk=b1f6753d-0e7d-4416-b580-6cadfabc4557)


## Module sạc xả pin Lithium với đầu ra 4.2v

![image](https://github.com/user-attachments/assets/53c5e4e7-f397-4f6a-b60b-c1738999ce44)
![image](https://github.com/user-attachments/assets/d94ebe18-1672-4b40-81d2-f124e1d07e02)
\Ảnh chụp thật\
![image](https://github.com/user-attachments/assets/49be39ff-51a2-48f3-8719-398b54b9f182)
![image](https://github.com/user-attachments/assets/30e6d040-fba2-4c99-8365-a3ba36d0f0ba)

> Rất giống [MH-CD42], bằng chiều rộng, nhưng ngắn hơn về chiều dài.

- __Ưu điểm__
  - 6 chân pin và giãn cách đều khớp với 2.54m. vì vậy cắm tốt trên breadboard và cả pcb test
  - Luôn xả 5v kể cả khi không có tải và kể cả khi xả từ pin
  - 4 led hiển thị tự tắt sau tầm 30 giây.
- Nhược điểm
  -  Nút K chỉ có tác dụng bật đèn hiển thị, không tác động lên quá trình tắt nguồn. Nút K tích cực mức thấp với 3 chân tin hiệu ra và 3 chân nối GND
     Đã thử nghiệm: có đấu nối nút K ngoài bằng cách lấy dây GND nối vào chân ở gần lỗ khoét bắt vít. ![vị trí đấu nút K](https://github.com/user-attachments/assets/af294863-6f87-4461-87cb-f73e67e06931)
- Thông số:
  - Lắp pin ngược cực sẽ bị cháy board.
  - Công tắc đồng bộ 2a để sạc hiệu quả
  - Dòng điện đầu ra tối đa 2.4a
  - Đầu ra cố định Thường mở 5v, có hỗ trợ bù tổn thất đường dây
  - Hỗ trợ trong khi sạc và đặt
  - Có 4 led chỉ thị mức độ pin sạc
  - Mức tiêu thụ nguồn ở chế độ chờ: < 150μA
  - Có bảo vệ ngắt sạc Pin khi đầy, quá tải, bảo vệ xả quá dòng
  - Kích thước: 16.2 mm x 16.2 mm
-  Các chân Gnd bao gồm của Đầu vào, của Đầu ra, của pin âm bản đều được nối thông với nhau.

- [Mua sắm](https://shopee.vn/3.7v-4.2V-18650-Pin-Lithium-T%C4%83ng-C%C6%B0%E1%BB%9Dng-S%E1%BA%A1c-B%E1%BA%A3ng-%C4%90i%E1%BB%87n-B%E1%BA%A3o-V%E1%BB%87-5V-2.4-S%E1%BA%A1c-X%E1%BA%A3-M%C3%B4-%C4%90un-T%C3%ADch-H%E1%BB%A3p-i.1456687807.28224156185)

## Mô-đun sạc pin Lithium giảm xả 5V2A / 2.4A  có đầu vào/đầu ra thường mở

![image](https://github.com/user-attachments/assets/19d85885-f9e4-41f8-9ae3-c11831f962cf)
![image](https://github.com/user-attachments/assets/f047be6d-123e-4f35-8f51-146a27b6ee49)

- Ưu điểm:
- __Ưu điểm__
  - 4 chân pin và giãn cách đều khớp với 2.54m, với 3 pin empty ở giữa. vì vậy cắm tốt trên breadboard và cả pcb test
  - Luôn xả 5v kể cả khi không có tải và kể cả khi xả từ pin
  - 4 led hiển thị tự tắt sau tầm 5 giây, sáng yếu
- Nhược điểm
  -  Nút K chỉ có tác dụng bật đèn hiển thị, không tác động lên quá trình tắt nguồn. Nút K tích cực mức thấp với 3 chân tin hiệu ra và 3 chân nối GND. Tác động lên nút bấm ở góc như ảnh dưới đây để active.
  ![image](https://github.com/user-attachments/assets/27a11d91-166d-45cb-9034-aea5bfbc69c2)

- Ảnh chụp thật:\
  Sạc cho pin với điện áp 4v2\
  ![image](https://github.com/user-attachments/assets/21e33b7e-9039-484a-8c6b-be1df6d3019a)
  Pin xả và tăng áp ra cổng Out/In kết hợp, điện áp chỉ đạt xấp xỉ 5v\
  ![image](https://github.com/user-attachments/assets/ccab6204-2eb7-4340-854f-e4e0118c59be)

- Thông số:
  1. Đầu vào và đầu ra với cùng một cổng/cặp pin
  2. Nếu không sạc thì cổng in/out sẽ có điện áp 5V
  3. Mô-đun có bảo vệ hai lớp (Chip điều khiển chính + IC bảo vệ).
  4. Điện áp sạc: DC4.5V-5.5V (Khuyến nghị DC5V)
  5. Dòng sạc: 0-2.1A.
  6. Điện áp sạc khi đủ và điện áp cắt: 4.2V Đất 1%;
  7. Dòng xả: 5V / 2.4A
  8. Dòng tĩnh: 80μA;
  9. Hiệu quả xả: < 96%;
  10. Nhiệt độ môi trường: -20°C ~ + 85°C;
- Có các chức năng bảo vệ quá dòng (0CP), Bảo vệ quá áp (0VP), Bảo vệ ngắn mạch (SCP), Bảo vệ quá nhiệt (0TP), Mô-đun đi kèm với chức năng bảo vệ pin Lithium (Thích hợp cho pin Lithium, Polyme, 18650... mà không cần bảo vệ có mạch bảo vệ).
- [Mua sắm](https://shopee.vn/M%C3%B4-%C4%91un-s%E1%BA%A1c-pin-Lithium-gi%E1%BA%A3m-x%E1%BA%A3-5V2A-2.4A-th%E1%BB%B1c-t%E1%BA%BF-c%E1%BB%95ng-type-c-c%C3%B3-th%E1%BB%83-%C4%91%E1%BA%A7u-v%C3%A0o-%C4%91%E1%BA%A7u-ra-th%C6%B0%E1%BB%9Dng-m%E1%BB%9F-i.1456687807.28074129517)

## Mạch sạc LX-LBC3

![image](https://github.com/user-attachments/assets/7b1f1bca-bbc6-42c8-8d39-bcc2e21e24b4)
![image](https://github.com/user-attachments/assets/ee02f746-2b6c-409e-b8a4-fcd25109f93f)

![LBC3](https://github.com/neittien0110/linhkiendientu/assets/8079397/669912ed-90d6-4065-8315-ed398e0b679b)
![image](https://github.com/user-attachments/assets/4bf46b76-748b-4c88-8f50-7e3f239aecc1)

- EasyEDA Library:
  - ![LBC3 Schematic](https://github.com/neittien0110/linhkiendientu/assets/8079397/0c22b791-1c5f-4ac9-8812-d8701d00dd13)
  - ![LBC3 Footprint](https://github.com/neittien0110/linhkiendientu/assets/8079397/6b51f648-e510-441b-90e7-1788d7607365)
  - ![LBC3](https://github.com/neittien0110/linhkiendientu/assets/8079397/b7dba5cf-dc4f-444c-9675-24fc3a66a166)|[Shopee](https://shopee.vn/ZIQQUCU-18650-M%C3%B4-%C4%91un-S%E1%BA%A1c-Pin-lithium-C%E1%BB%95ng-type-c-4.2V-4.35V-5V-i.880593108.22552543642)|

- Casestudy:
   - Khi pin lithium sụt về 3.7v thì
     - cắm trực tiếp pin vào Esp32+BLE thì vẫn chạy thành công
     - cắm pin vào mạch LX-LBC3 thì đầu ra vẫn đạt 5V. Qua mạch giảm áp Mini-360 thì vẫn có V đầu ra 3.7v nhưng khi có tải là nhảy áp liên tục.
     - cắm pin vào mạch LX-LBC3 thì đầu ra vẫn đạt 5V. Qua mạch giảm áp Mini-360 điều chỉnh ở mức 3.2v thì khi có tải sẽ dùng được lâu hơn.
      ![image](https://github.com/user-attachments/assets/67d65ffc-3ba4-4315-a1db-9d4e35186d34)

- Mô tả:
  - Sạc pin Lithium/18650, 
  - Điện áp đầu ra: 5V ở dạng type-c và 2 chân pin 2.0mm đấu nối trực tiếp với VBUS và GND của type C. __Vào/ra 2 chiều__
  - Điện áp đầu vào: 4.5 ~ 5.5V
  - Sạc điện áp cắt: 4.2V
  - Dòng sạc: 1.2A
  - Tự động chuyển đổi đầu vào và đầu ra. Khi không có điện áp đầu vào tự động chuyển đổi thành đầu ra.
  - Điện áp ra: 5V, dòng xả: 450mA
  - Bảo vệ quá xả: 2.9V
  - Đèn báo: Xanh lá khi ở chế độ sạc pin, xanh dương ở chế độ xả.
  - Kích thước: 16x12mm

- Thông số:
  1. Kích thước nhỏ, chiều dài, chiều rộng và chiều cao chỉ 16 * 12 * 4,4mm.
  2. Áp dụng cho pin liti một cell (kết nối song song không giới hạn)
  3. Dòng sạc tối đa 1.2A, dòng điện 1A ổn định có thể được sử dụng theo yêu cầu.
  4. Dòng xả: 0.45A
  5. Bảo vệ quá tải 2.9v, điện áp cắt sạc 4.2V
  6. USB Type-C, cùng với 2 chân pin, là cồng nguồn sạc đầu vào, nhưng sẽ tự động chuyển sang chế độ đầu ra khi không có điện áp. Thời gian chuyển đổi từ 1-2 giây. Nói cách khác là USB Type-C vừa là cổng nguồn vào, vừa là cổng nguồn ra.
  7. Hỗ trợ dòng điện nhỏ, đầu ra 5V, đầu ra hỗ trợ khoảng 450ma. Nếu đầu ra là 1A, điện áp sẽ khoảng 4,9V-4,5V tùy theo điều kiện nguồn.
  8. Đèn xanh nhấp nháy khi sạc. Đèn xanh luôn sáng khi sạc đầy. 
  9. Công suất tiêu thụ ở chế độ chờ khoảng 0,8mA.

- Hướng dẫn:
  - Mô-đun có thể được sử dụng bằng cách kết nối các điện cực âm và dương của pin liti 3.7V. Bản thân mô-đun có tính năng bảo vệ quá tải và quá tải, đồng thời pin liti cũng có thể được trang bị bảng bảo vệ.
  - Cổng Type-c, lỗ hàn và giao diện đầu vào và đầu ra dành riêng ở mặt sau là ba bộ giao diện giống nhau và được kết nối trực tiếp trên đường truyền, vì vậy không có sự khác biệt giữa ba Bộ giao diện.
  - Theo hệ thống dây nhận dạng (các bộ phận có cùng màu được kết nối vật lý), có thể sử dụng đầu vào cổng C hoặc đầu vào dây. Pin sạc, nếu có nhiều, thì phải đấu song song vì đây là sạc 1S. Dây cần được hàn, và dây không được quá mỏng, nếu không dây sẽ không hoạt động bình thường. 
  -__Không thể đảo ngược pin.__
  
- Các tính năng:
  - Chu kỳ sạc tự động kết thúc khi dòng điện sạc giảm xuống 100mA sau khi đạt đến điện áp phao cuối cùng.
  - Khi điện áp pin thấp hơn 2,9V, pin sẽ được sạc trước với dòng điện 200mA.
  - Có bo mạch bảo vệ, bảo vệ quá áp, bảo vệ quá xả, bảo vệ quá dòng. Giá trị bảo vệ quá xả: 2.9V.
  - Lần đầu tiên sử dụng pin, cần kết nối nguồn điện để kích hoạt bo mạch bảo vệ.
- Các biện pháp phòng ngừa:
  - Không kết nối ngược lại pin và kết nối với bo mạch chống cháy.
  - Kết nối đầu sạc trước khi kết nối pin và kiểm tra xem đèn sạc của mô-đun có bình thường hay không.
  - Dây không được quá mỏng, nếu không dòng điện cấp nguồn không thể theo kịp và phải hàn dây.

- [Mua sắm](https://shopee.vn/ZIQQUCU-18650-M%C3%B4-%C4%91un-S%E1%BA%A1c-Pin-lithium-C%E1%BB%95ng-type-c-4.2V-4.35V-5V-i.880593108.22552543642)

## Mạch sạc pin type-C 3.7v

![siêu nhỏ](https://github.com/neittien0110/linhkiendientu/assets/8079397/4c13fa2d-04d9-4a24-b7ce-17c3bc5618ee)
![image](https://github.com/user-attachments/assets/0e8a728c-ffc8-4efd-8bdb-c13e7d74b602)
![image](https://github.com/user-attachments/assets/4c917abd-81ac-4d98-9c6b-53fa569ed330)
![kich thuoc](https://github.com/user-attachments/assets/ca3e740e-5e5c-4f87-ba94-8386ce126bc2)

- Thông số:
  - Nguồn vào: usb typeC, 2 chân pin In+, In-
  - Ra 4.2V; 
  - Cần kích hoạt khi dùng lần đầu;
  - Đèn đỏ đang sạc và đèn xanh đã đầy.
  
- EasyEDA lib:
  - Thư viện tp4056 mini from neittien0110\
    ![image](https://github.com/neittien0110/linhkiendientu/assets/8079397/0c853180-5ec5-4429-9358-4821e98c0b64)|
  - ![Schematic](https://github.com/neittien0110/linhkiendientu/assets/8079397/7f493957-2a8f-4fb7-92be-038cc5914ca6)
  - ![Footprint mini](https://github.com/neittien0110/linhkiendientu/assets/8079397/325dcbf4-7300-4426-b4be-407d7a0d65cc)
- [Mua sắm](https://shopee.vn/M%E1%BA%A1ch-S%E1%BA%A1c-Pin-Si%C3%AAu-Nh%E1%BB%8F-4.2V-1A-Ch%C3%A2n-S%E1%BA%A1c-Type-C-C%C3%B3-B%E1%BA%A3o-V%E1%BB%87-Pin-i.456730649.22554426428)|
- [Mua sắm](https://shopee.vn/ZIQQUCU-18650-M%C3%B4-%C4%91un-S%E1%BA%A1c-Pin-lithium-C%E1%BB%95ng-type-c-4.2V-4.35V-5V-i.880593108.22552543642)

## Sạc pin lithium cổng USB Type C ra 5V 2A có nút K

![sạc có đèn báo và nút bấm](https://github.com/neittien0110/linhkiendientu/assets/8079397/b1e6b720-bc40-4d8d-b745-112071fdaaa4)
![Giải thích pin](https://github.com/user-attachments/assets/bdc90a9b-c49d-4db3-b775-cf90bb596fa9)
[Video](https://youtu.be/mD2fCQCn4aY?si=OcyU8dAayVQjNBef)

- Thông số:
  - Vào Usb TypeC 5V, hoặc cặp cặp lỗ PCB vào/ra pin;
  - Điện áp sạc pin: 4.2V. Dòng sạc: 2.4A ±5%
  - có 4 led chỉ định mức pin. _tự ngắt mạch sau khoảng 15 không có tải._
  - __Ra cặp lỗ PCB 5V__
  - __có nút bấm K tự hàn__. 
  - không bảo vệ ngược dòng
  - Kích thước 4.4mm(H) x 20.3mm (W) x 25.4 mm(26.3 nếu tính cả phần usb thòi ra) (L)
  - 2 lỗ 5V cắm vừa PCB (2x2.54mm), nhưng 2 lỗ đấu pin thì ko vừa và phải hàn phủ lên pcb.
  - Đầu ra: hàn chân hoặc đầu USB A cái
  - Điện áp ra: 5~ 5.15V
  - Dòng đầu ra: có thể đạt 2A
  - Hiệu suất chuyển đổi: 92.5% ( đối với đầu vào 3.6V, đầu ra 5V 2A)
  
- [Thông số ở NShop](https://nshopvn.com/product/mach-sac-xa-pin-18650-cong-type-c-co-den-bao)
- [Mua sắm](https://shopee.vn/M%C3%B4-%C4%91un-s%E1%BA%A1c-pin-lithium-c%E1%BB%95ng-USB-Type-C-5V-2A-DIY-i.578443443.14279169398)

## LX-LCBST sạc pin lithium và kiêm xả pin có điều chỉnh điện áp

![image](https://github.com/user-attachments/assets/bb655304-1d70-48d6-b6b7-81287c6d6de5)
![image](https://github.com/user-attachments/assets/e4e38919-0904-43c2-97db-c4f2d307d72c)

- [Mua sắm](https://shopee.vn/Tp4056-3.7V-4.2V-9V-5V-2A-C%C3%B3-Th%E1%BB%83-%C4%90i%E1%BB%81u-Ch%E1%BB%89nh-B%C6%B0%E1%BB%9Bc-L%C3%AAn-M%C3%B4-%C4%90un-18650-Lithium-Li-ion-Pin-S%E1%BA%A1c-X%E1%BA%A3-B%E1%BA%A3ng-%C4%90i%E1%BB%87n-DIY-B%E1%BB%99-i.176393725.25922921429?xptdk=88b502ac-a364-463e-acea-a8a09ce0a260)

## HW-357 Sạc pin lithium và kiêm tăng áp booster

![image](https://github.com/user-attachments/assets/ba8142cc-ecb4-4352-a94f-1de9b59c2479)
![image](https://github.com/user-attachments/assets/f84cb5b2-5f97-460f-bc3c-1f353099b723)

> Nhược điểm: vị trí 2 lỗ cấp điện áp ra rất tệ vì cùng phía với cổng USB, dường như để cấp áp ra ngoài thiết bị. Dùng module [LX-LCBST](#) tốt hơn. Ngoài ra, tích hợp thêm tăng áp trên 4v nên không thể cấp trực tiếp cho MCU.
> 
- Thông số:
  - Điện áp đầu vào: 4.5~8V từ USB Type-C hoặc 2 lỗ PCB
  - Điện áp đầu ra: __4.0-27V DC__ (Có thể điều chỉnh liên tục, đã test)
  - Điện áp sạc pin lithium: 4.2V DC
  - Dòng sạc pin lithium: Max. 1a
  - Dòng xả: Max. 2a
- [Mua sắm](https://shopee.vn/B%E1%BA%A3ng-M%E1%BA%A1ch-S%E1%BA%A1c-Pin-Lithium-Li-ion-18650-3.7V-4.2V-TP4056-Chuy%C3%AAn-D%E1%BB%A5ng-i.578443443.16942863022)
- [Mua sắm](https://shopee.vn/3.7v-9V-5V-2A-C%C3%B3-Th%E1%BB%83-%C4%90i%E1%BB%81u-Ch%E1%BB%89nh-B%C6%B0%E1%BB%9Bc-L%C3%AAn-Boost-18650-Pin-Lithium-S%E1%BA%A1c-M%C3%B4-%C4%90un-T%C3%ADch-H%E1%BB%A3p-4.3-27V-i.176393725.25221943887?xptdk=8afbbd9e-a9e2-4c5b-9a03-6b6297a9a4c8)


## Board điều khiển đèn pin sạc

![image](https://github.com/user-attachments/assets/b993f9f0-ff34-47cf-b33d-ff10cc77d66f)
![image](https://github.com/user-attachments/assets/0f1a650a-924d-43d8-80bd-24d0f955de25)

- Thông số:
  - Một bảng tích hợp công tắc Tact
  - Điện áp đầu vào: 3,7 ~ 4,2V (Một pin)
  - Cổng sạc: USB Type-C.
  - Chiều dài bên bảng điều khiển: Khoảng 17,5mm
- Thích hợp cho việc sử dụng hạt đèn pin công suất 10w.- 
- [Mua sắm](https://shopee.vn/%C4%90%C3%A8n-pin-m%E1%BA%A1nh-B%E1%BA%A3ng-m%E1%BA%A1ch-truy%E1%BB%81n-%C4%91%E1%BB%99ng-B%E1%BA%A3ng-m%E1%BA%A1ch-Ph%E1%BB%A5-ki%E1%BB%87n-t%E1%BB%B1-l%C3%A0m-B%E1%BA%A3ng-m%E1%BA%A1ch-typec-C%E1%BB%95ng-s%E1%BA%A1c-X%E1%BA%A3-s%E1%BA%A1c-M%C3%B4-%C4%91un-t%C3%ADch-h%E1%BB%A3p-i.1456687807.29674146507)



## Đế pin và pin

![image](https://github.com/user-attachments/assets/71c1a7c8-7325-456d-ae82-8f3f0f1a87ef)
![image](https://github.com/user-attachments/assets/257f6f5a-7bfc-4fc6-8cde-1f24c6ab5e9c)

### Pin 10440 và đế. Pin AAA

  ![Pin 10440](https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m1s76w602c3j4e@resize_w450_nl.webp)
  
- [Mua pin 10440](https://shopee.vn/Pin-s%E1%BA%A1c-size-10440-(-AAA)-3.7v-1000mAh-d%C3%B9ng-cho-%C4%91%C3%A8n-led-xe-%C4%91%E1%BB%93-ch%C6%A1i-i.1086477386.28460105821)
- [Mua sắm đế 10440 đấu dây và có sẵn công tắc](https://shopee.vn/%C4%90%C3%AA%CC%81-pin-con-tho%CC%89-AAA-c%C6%A1%CC%83-nho%CC%89-loa%CC%A3i-1pin-2-pin-3-pin-4-pin-co%CC%81-n%C4%83%CC%81p-co%CC%81-c%C3%B4ng-t%C4%83%CC%81c-ON-OFF-Pin-con-tho%CC%89-xi%CC%A3n-i.1032535693.22147972594?sp_atk=5caa4bb6-7ce0-4f70-8efe-f46cb05cf0da&xptdk=5caa4bb6-7ce0-4f70-8efe-f46cb05cf0da)
- [Mua sắm đề 10400 đấu dây](https://shopee.vn/%C4%90%E1%BA%BF-pin-%C4%91%C5%A9a-AAA-1-2-3-4-cell-m%E1%BA%AFc-n%E1%BB%91i-ti%E1%BA%BFp-H%E1%BB%99p-%C4%91%E1%BB%B1ng-pin-ti%E1%BB%83u-AAA-d%C3%A2y-h%C3%A0n-s%E1%BA%B5n-v%C3%A0-l%E1%BB%97-b%E1%BA%AFt-v%C3%ADt-lo%E1%BA%A1i-1-2-3-4-ng%C4%83n-i.281350512.20358421991?sp_atk=1f4b6e5e-a6e2-4e2d-a419-a87d270f33a3&xptdk=1f4b6e5e-a6e2-4e2d-a419-a87d270f33a3)

### Pin 14250 và đế

  ![Pin 14250](https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m1s7a4z94g9f86@resize_w450_nl.webp)
  
- [Mua pin 14250](https://shopee.vn/Pin-s%E1%BA%A1c-nhi%E1%BB%81u-l%E1%BA%A7n-3.7v-14250-d%C3%B9ng-cho-m%C3%A1y-laze-%C4%91%C3%A8n-laze-%C4%91%E1%BA%A1i-b%C3%A0ng-m%C3%A1y-%C4%91o-kho%E1%BA%A3ng-c%C3%A1ch-dung-l%C6%B0%E1%BB%A3ng-i.1086477386.29160180468)
- [Mua sắm đế 14250 chân hàn](https://shopee.vn/5x1-2AA-14250-Pin-L%C6%B0u-Tr%E1%BB%AF-K%E1%BA%B9p-H%E1%BB%99p-%C4%90%E1%BB%B1ng-3.6V-V%E1%BB%9Bi-PCB-Pin-H%C3%A0n-ch%C3%AC-i.183696794.29304863025)

### Pin 14500 và đế. Pin AA

  ![Pin 14500](https://down-vn.img.susercontent.com/file/vn-11134207-7r98o-lzoi9pk0n0b120.webp)
  
- [Mua pin 14500 chân hàn](https://shopee.vn/Pin-Sony-14500-AA-3.7V-680mAh-Pin-Chuy%C3%AAn-D%C3%B9ng-Cho-B%C3%A0n-Ch%E1%BA%A3i-%C4%90i%E1%BB%87n-Philips-Sonicare-i.1086477386.28659691274)
- [Mua sắm đế 14500 nối dây](https://shopee.vn/%C4%90%E1%BA%BF-Pin-AAA-Kh%C3%B4ng-N%E1%BA%AFp-1-Pin-2-Pin-3-Pin-4-Pin-%C4%90%E1%BA%BF-Pin-Ti%E1%BB%83u-AAA-(C%E1%BB%A1-Pin-Con-Th%E1%BB%8F-Lo%E1%BA%A1i-B%C3%A9)-(G%E1%BB%ACI-%C4%90%C6%A0N-T%E1%BB%AA-20K)-Pin-1-5V-i.1032535693.22773460473?sp_atk=a715e5c3-f695-4156-b910-b1c1f25e4444&xptdk=a715e5c3-f695-4156-b910-b1c1f25e4444)

  ### Pin 16430 và đế

  ![Pin 16340](https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m1s74pr2uqmra3@resize_w450_nl.webp)
  
- [Mua pin 16340](https://shopee.vn/Cr123a-16340-17335-lir123a-PCB-m%E1%BB%99t-ph%E1%BA%A7n-c%C3%B3-Pin-H%E1%BB%99p-Pin-Gi%C3%A1-%C4%91%E1%BB%A1-Pin-Lithium-3V-i.821639995.26706689693)
- [Mua sắm đế 16340](https://shopee.vn/Cr123a-16340-17335-lir123a-PCB-m%E1%BB%99t-ph%E1%BA%A7n-c%C3%B3-Pin-H%E1%BB%99p-Pin-Gi%C3%A1-%C4%91%E1%BB%A1-Pin-Lithium-3V-i.821639995.26706689693)

### Pin 18650 và đế

  ![Pin 18650](https://down-vn.img.susercontent.com/file/vn-11134207-7r98o-lxoa5g4kq5ej61@resize_w450_nl.webp)
  
- [Mua pin 18650](https://shopee.vn/Cell-pin-EVE-18650-25P-dung-l%C6%B0%E1%BB%A3ng-2500mah-X%E1%BA%A3-12C-30A-Pin-Th%C3%A1o-kh%E1%BB%91i-ch%C3%ADnh-h%C3%A3ng-%C4%90%E1%BA%B9p-nh%C6%B0-m%E1%BB%9Bi-i.95243985.20313052510?sp_atk=a523534f-10e2-461b-836b-9e549ad8ce07&xptdk=a523534f-10e2-461b-836b-9e549ad8ce07)
- [Mua sắm đế 18650 hàn](https://shopee.vn/%C4%90%E1%BA%BF-Pin-18650-1-2-3-4-Pin-Ch%C3%A2n-H%C3%A0n-%C4%90%E1%BA%BF-1-Pin-18650-%C4%90%E1%BA%BF-2-Pin-18650-%C4%90%E1%BA%BF-3-Pin-18650-%C4%90%E1%BA%BF-4-Pin-18650-i.998840499.18284093774?sp_atk=5302faee-fe8a-4238-9277-5ca992019806&xptdk=5302faee-fe8a-4238-9277-5ca992019806)
