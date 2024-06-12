# ĐỘNG CƠ

## Mục luc

1. [Motor bước 28BYJ-48 5V](#motor-bước-28byj-48-5v)
2. [Motor rung](#motor-rung)
3. [Động cơ DC 130 kèm hộp số](#động-cơ-dc-130-kèm-hộp-số)
4. [Tùy chỉnh thư viện Servo của Arduino](#tùy-chỉnh-thư-viện-servo-của-arduino)
5. [Servo MG945](#servo-mg945)
6. [Servo MG996](#servo-mg996)
7. [Servo TD-8120mg](#servo-td-8120mg)

## Motor bước 28BYJ-48 5V

- Cấu trúc\
![image](https://github.com/neittien0110/linhkiendientu/assets/8079397/4df264fe-d8e8-4063-8d12-dcfec360ae1e)
- Ý nghĩa các dây dẫn \
  ![image](https://github.com/neittien0110/linhkiendientu/assets/8079397/9da96230-bcee-4116-bc9b-1090137d72a8)
- Mapping các dây dẫn của motor với board điều khiển công suất\
  |Màu dây của động cơ | Chân pin tren board công suất|
  |--|--|
  |Đỏ|Vdd|
  |Cam|D|
  |Vàng|C|
  |Hồng|B|
  |Xanh|A|

- Code minh họa
  ```C
  // Arduino stepper motor control code
  #include <Stepper.h> // Include the header file
  // change this to the number of steps on your motor
  #define STEPS 32
  // create an instance of the stepper class using the steps and pins
  Stepper stepper(STEPS, 8, 10, 9, 11);  // ứng với chân IN1, IN2, IN3, In4 trên board ULN2003
  int val = 0;
  void setup() {
    Serial.begin(9600);
    stepper.setSpeed(200);
  }
  
  void loop() {
    stepper.step(2048);
  }![image](https://github.com/neittien0110/linhkiendientu/assets/8079397/ed20cf22-dfe5-4061-9c10-8e381d6c8dca)
  ```
- Minh họa kết nối\
  ![image](https://github.com/neittien0110/linhkiendientu/assets/8079397/98d045ff-44d8-4e1f-aa27-ce384087b71d)
  ![Với Arduino](https://github.com/neittien0110/linhkiendientu/assets/8079397/740475db-1fa4-4598-a871-3e2b4c91b763)
  ![Giả lập](https://github.com/neittien0110/linhkiendientu/assets/8079397/aea87d7e-69bf-4a27-b41b-082da7aba309)

- Mua sắm: \
  <https://banlinhkien.vn/goods-653-dong-co-buoc-5v-step-motor-28byj-48-5vdc.html>

## Motor rung

- Xem hướng dẫn ghép nối với Arduino, và lắp trans cho công suất lớn hơn. [Xem](https://vn.ineed-motor.com/news/how-to-build-a-vibration-motor-circuit-35660008.html)
   
- Mua sắm: \

  |Ảnh|Mua sắm|
  |--|--|
  |![image](https://github.com/neittien0110/linhkiendientu/assets/8079397/5a1e36e7-b528-4fa5-b32e-716c787c3d9b)|[Module motor rung đã có sẵn transistor điều khiển công suất](https://dientutuonglai.com/module-rung-mini-arduino.html) \ [Shopee](https://shopee.vn/Pwm-Vibration-Engine-Vibration-Module-M%C3%B4-%C4%91un-%C4%91%E1%BB%99ng-c%C6%A1-rung-Pwm-cho-Arduino-Uno-Mega-2560-R3-DIY-i.148048328.3618802496)|
  |![image](https://github.com/neittien0110/linhkiendientu/assets/8079397/8a0a8b80-1c07-45b8-80cc-3822fe628779)|[Motor phi 8 mm, có băng dinh 3M để dán lên board](https://shopee.vn/Set-10-%C4%90%E1%BB%99ng-C%C6%A1-Rung-DC3V-0834-Cho-%C4%90i%E1%BB%87n-Tho%E1%BA%A1i-i.81431289.16385816403)|
  |![image](https://github.com/neittien0110/linhkiendientu/assets/8079397/5cd06926-f962-4ebc-98f3-a5a53ad44321)|[Motor rung dạng trụ 4x11mm 3VDC rất khỏe](https://shopee.vn/5Pcs-New-Arrival-Micro-Coreless-Vibration-Motor-Mini-DC-Motor-High-Speed-Vibrating-Motor-for-Professional-RC-4x11mm-DC-1.5V-3V-i.81431289.4134754620)|

## Động cơ DC 130 kèm hộp số

![DC Gear Motor TT](https://github.com/neittien0110/linhkiendientu/assets/8079397/7ac7a0b0-cbba-4488-a8aa-d6a76c4f93a4)

- English: DC Gear Motor TT - 130 RPM
- Thông số:
  - Tỷ lệ hộp số: 1:90
  - Nguồn điện: 3-6V
  - Tốc độ đầu ra: 110RPM (Vòng/phút) ~ 2 vòng/giây
  - Bắt vít M3 vào chính giữa trục để giữ bánh xe
  - Bánh răng kim loại\
![Cấu trúc DC Gear Motor TT 130](https://ae01.alicdn.com/kf/Sebeed03bd90f42299dafab84be57fa6c4.jpg)
![Mở nắp](https://github.com/neittien0110/linhkiendientu/assets/8079397/ee4d7f32-90f1-41e9-a3c7-f0b6d18b3e99)

- In 3D:
  - [Ke L gá hộp số](https://www.thingiverse.com/thing:1169412)
  - [Hộp gá vào Lego, chuyển đổi trục bánh xe giảm tốc thành trục + của Lego](https://www.thingiverse.com/thing:5140209)

## Tùy chỉnh thư viện Servo của Arduino

Cho phép khai báo chồng lên các khai bao sau trong [<Servo> của Arduino](https://www.arduino.cc/reference/en/libraries/servo/)

```C
#define MIN_PULSE_WIDTH       544     // Độ rộng xung, tính theo us, tương ứng với góc quay bé nhất
#define MAX_PULSE_WIDTH      2400     // Độ rộng xung, tính theo us, tương ứng với góc quay lớn nhất
#define DEFAULT_PULSE_WIDTH  1500     //  Độ rộng xung, tính theo us, tương ứng với góc chính giữa
#define REFRESH_INTERVAL    20000     // minimum time to refresh servos in microseconds
```
> File <https://github.com/arduino-libraries/Servo/blob/master/src/Servo.h>

## Servo MG945

  ![image](https://github.com/neittien0110/linhkiendientu/assets/8079397/1158d628-0a7b-4356-820a-c79b81509118)
  ![image](https://github.com/neittien0110/linhkiendientu/assets/8079397/2b5790b7-5af2-4c72-9541-3ebc4a6a41ae)
  
  [Video](https://youtu.be/t-BilDaseac?si=BBe57glP0zpceQmM)

- Thông số:
  - Góc quay 180*/360*
  - Bánh răng: chỉ có 1 bánh răng kim loại
  - Cùng kích cỡ với MG945, MG995, MG996, TD-8120mg, TD-8125mg
- Không nên mua, chẳng khác gì MG995, rất dễ bị trật bánh răng.
- [Mua sắm](https://shopee.vn/%C4%90%E1%BB%99ng-C%C6%A1-Servo-SG90-MG90S-MG945-MG946-MG995-MG996-Cho-M%C3%A1y-Bay-%C4%90i%E1%BB%81u-Khi%E1%BB%83n-Arduino-UNO-DIY-MG946R-MG996R-i.832347222.19878584195)

## Servo MG996

  ![image](https://github.com/neittien0110/linhkiendientu/assets/8079397/9814af4d-8e4c-4e5b-a2fe-c21a7058d0bc)
- Thông số:
  - Góc quay 180*, hoặc 360*. Trường hợp góc 360 thì dùng [Thiết bị kiểm tra servo](https://shopee.vn/product/176393725/6601794079?gad_source=1&gclid=EAIaIQobChMIi_Dzq4-6hgMV69QWBR3ogw-xEAYYAiABEgKgXPD_BwE) vẫn được, nhưng lại không khiển được bằng [RC FlySky i6](https://bizweb.dktcdn.net/thumb/grande/100/040/530/products/bo-dieu-khien-flysky-fs-i6rx-nang-cap-ia6b-3411-77349224-0e76feacd3c4e5afdc463a2368b23285-catalog-233.jpg?v=1670064529347).
  - Cùng kích cỡ với MG945, MG995, MG996, TD-8120mg, TD-8125mg

- [Mua sắm](https://shopee.vn/%C4%90%E1%BB%99ng-C%C6%A1-Servo-SG90-MG90S-MG945-MG946-MG995-MG996-Cho-M%C3%A1y-Bay-%C4%90i%E1%BB%81u-Khi%E1%BB%83n-Arduino-UNO-DIY-MG946R-MG996R-i.832347222.19878584195)

## Servo TD-8120mg
   ![ảnh 1](https://bizweb.dktcdn.net/100/190/540/files/td8120mg-1.png?v=1562724656942)
- Thông số:
  - TD-81**20mg**: momen 20kg.1cm
  - Điện áp: 4.8V - 8.4V
  - Cường độ dòng tiêu thụ tối đa: 2.7A
  - Bánh răng nối đĩa: Spline 25T (25 teeth/25 răng)
    ![ảnh 2](https://bizweb.dktcdn.net/100/190/540/files/td8120mg-2.png?v=1562724672885)
- Cùng kích cỡ với MG945, MG995, MG996, TD-8120mg, TD-8125mg
- Waveform điều khiển góc quay:
  Góc | Chu kỳ | Độ rộng xung
  --|--|--
  90&deg;|20 ms| 1 ~ 2 ms
  180&deg;|20 ms| 0.5 ~ 2.5 ms
  270&deg;|20 ms| 0.5 ~ 2.5 ms
  300&deg;|20 ms| 0.5 ~ 2.5 ms
  300&deg; xoay tròn liên tục|20 ms| 1 ~ 2 ms
  
  Tham khảo [Tùy chỉnh thư viện Servo của Arduino](#tùy-chỉnh-thư-viện-servo-của-arduino)
  
- [Datasheet](https://www.tinytronics.nl/index.php?route=product/product/get_file&file=2316/Data%20Sheet%20of%20TD-8120MG%20Digital%20Servo%20Motor.pdf)
- Mua sắm:
  - [Shopee](https://shopee.vn/%C4%90%E1%BB%99ng-C%C6%A1-Servo-TD-8120MG-TD-8125MG-Ch%E1%BB%91ng-Th%E1%BA%A5m-N%C6%B0%E1%BB%9Bc-20kg-25KG-180-%C4%90%E1%BB%99-Cho-Xe-%C4%90i%E1%BB%81u-Khi%E1%BB%83n-T%E1%BB%AB-Xa-i.869927552.18967205624?xptdk=c181ea3a-975a-4477-8111-3e9fd9a2c57d)
  - [AliEx](https://vi.aliexpress.com/item/1005004532499687.html)
