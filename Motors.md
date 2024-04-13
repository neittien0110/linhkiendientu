# ĐỘNG CƠ

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

  
  
