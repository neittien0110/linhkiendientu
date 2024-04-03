# ĐỘNG CƠ

## Motor bước 28BYJ-48 5V

- Cấu trúc
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

## Mua sắm
 - <https://banlinhkien.vn/goods-653-dong-co-buoc-5v-step-motor-28byj-48-5vdc.html>




  
