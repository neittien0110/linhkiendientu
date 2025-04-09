# NGUỒN CẤP

- [IC nguồn AMS1117 và các module liên quan](#ic-nguồn-ams1117-và-các-module-liên-quan)
  - [Module nguồn ổn áp dùng AMS1117](#module-nguôn-ổn-áp-dùng-ams1117)
- [Module chuyển đổi AC 220V --> DC 5V/0.7A](#module-chuyển-đổi-ac-220v----dc-5v07a)
- [HW-626 module tăng áp 5V](#hw-626-module-tăng-áp-5v)
- [Mini-360 module hạ áp có điều chỉnh bằng chiết áp](#mini-360-module-hạ-áp-có-điều-chỉnh-bằng-chiết-áp)
- [Mô đun tăng áp 0.9-5V sang 5V](#module-tăng-áp-09-5v-sang-5v)
- [Module hạ áp mini360 mini-360 DC thấp hơn LM2596](#module-hạ-áp-mini360-mini-360-dc-thấp-hơn-lm2596)
- [Mạch sạc, bảo vệ pin lithium 1 cell, cổng usb type-C](#mạch-sạc-bảo-vệ-pin-lithium-1-cell-cổng-usb-type-c)
- [Mạch sạc Lithium bao gồm màn hình của tẩu thuốc lá điện tử](#mạch-sạc-lithium-bao-gồm-màn-hình-của-tẩu-thuốc-lá-điện-tử)
- [Mạch sạc Lithium bao gồm màn hình của tẩu thuốc lá điện tử Rifbar Turbo](#mạch-sạc-lithium-bao-gồm-màn-hình-của-tẩu-thuốc-lá-điện-tử-rifbar-turbo)
- [Mạch sạc Lithium có màn hình nhỏ](#mạch-sạc-lithium-có-màn-hình-nhỏ)
- [Mạch sạc Lithium có màn hình nhỏ 2](#mạch-sạc-lithium-có-màn-hình-nhỏ-2)
- [Mạch sạc MH-CD42 có nút Key nhưng không usb](#mạch-sạc-mh-cd42-có-nút-key-nhưng-không-usb)
- [Mạch sạc LBC3 5v](#mạch-sạc-lbc3)
- [Sạc pin lithium cổng USB Type C ra 5V 2A có nút K](#sạc-pin-lithium-cổng-usb-type-c-ra-5v-2a-có-nút-k)
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

## Module tăng áp 0.9-5V sang 5V

  ![Mô đun tăng áp 0.9-5V sang 5V](https://github.com/user-attachments/assets/4b04538b-44b5-4156-b5a8-f5dd588fd862)

- Vào: điện áp từ 0.9 tới 5V (nhưng không quá 5V)
- Ra: 5V, dòng tối đa 480mA
- Nếu áp đầu vào 0.8V thì đầu ra chỉ có 7mA
- Tần số hoạt động: 150KHz
- Hiệu suất chuyển đổi điển hình: 85%
- Kích thước: 11*10,5*7,5mm
- [Mua sắm](https://shopee.vn/M%C3%B4-%C4%91un-t%C4%83ng-%C3%A1p-0.9-5V-sang-5V-1.5V-1.8V-2.5V-3V-3.3V-3.7V-4.2V-sang-5V-thay-th%E1%BA%BF-ti%E1%BB%87n-d%E1%BB%A5ng-i.578443443.11667335774)

## Module hạ áp mini360 mini-360 DC thấp hơn LM2596

  ![image](https://github.com/user-attachments/assets/0d4f52e5-a5a0-45c9-9b15-31bb1eb5e340)

- Thuộc tính mô-đun: Không bị cô lập
- Chỉnh lưu: Chỉnh lưu đồng bộ
- Điện áp đầu vào: 4,75V-23V
- Điện áp đầu ra: 1.0V-17V
- Dòng điện đầu ra: Giảm mức 3A, dài 1.8A
- Hiệu suất chuyển đổi: 96% (tối đa)
- Tần số chuyển đổi: 340KHz
- Độ gợn sóng đầu ra: 30mV (không tải)
- Điều chỉnh tải: ± 0,5% \
- Điều chỉnh điện áp: ± 2,5%
- Nhiệt độ hoạt động: -40 độ C đến +85 độ C
- Đặc điểm: Sử dụng cuộn cảm ứng điện được đúc nguyên khối và chip điều khiển bộ chỉnh lưu đồng bộ, nhỏ hơn và hiệu quả hơn
- [Mua sắm](https://shopee.vn/M%C3%B4-%C4%91un-h%E1%BA%A1-%C3%A1p-mini360-mini-360-DC-th%E1%BA%A5p-h%C6%A1n-LM2596-i.578443443.12390124552)

[Xem thêm các module nguồn có thư viện easyeda ,lcsc](./EasyEDA_Library.md)

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

![module](https://github.com/neittien0110/linhkiendientu/assets/8079397/c848dfda-a559-4a2f-9240-a1ca9779ec2f)

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

## Mạch sạc LBC3

![image](https://github.com/user-attachments/assets/7b1f1bca-bbc6-42c8-8d39-bcc2e21e24b4)
![image](https://github.com/user-attachments/assets/ee02f746-2b6c-409e-b8a4-fcd25109f93f)

![LBC3](https://github.com/neittien0110/linhkiendientu/assets/8079397/669912ed-90d6-4065-8315-ed398e0b679b)
![image](https://github.com/user-attachments/assets/4bf46b76-748b-4c88-8f50-7e3f239aecc1)

- EasyEDA Library:
  - ![LBC3 Schematic](https://github.com/neittien0110/linhkiendientu/assets/8079397/0c22b791-1c5f-4ac9-8812-d8701d00dd13)
  - ![LBC3 Footprint](https://github.com/neittien0110/linhkiendientu/assets/8079397/6b51f648-e510-441b-90e7-1788d7607365)
  - ![LBC3](https://github.com/neittien0110/linhkiendientu/assets/8079397/b7dba5cf-dc4f-444c-9675-24fc3a66a166)|[Shopee](https://shopee.vn/ZIQQUCU-18650-M%C3%B4-%C4%91un-S%E1%BA%A1c-Pin-lithium-C%E1%BB%95ng-type-c-4.2V-4.35V-5V-i.880593108.22552543642)|

- Mô tả:
  - Sạc pin Lithium/18650, 
  - Điện áp đầu ra: 5V ở dạng type-c và 2 chân pin 2.0mm đấu nối trực tiếp với VBUS và GND của type C
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
  6. USB Type-C là cồng nguồn sạc đầu vào, nhưng sẽ tự động chuyển sang chế độ đầu ra khi không có điện áp. Thời gian chuyển đổi từ 1-2 giây. Nói cách khác là USB Type-C vừa là cổng nguồn vào, vừa là cổng nguồn ra.
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
