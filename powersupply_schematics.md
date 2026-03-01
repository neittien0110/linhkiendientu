# THIẾT KẾ MODULE NGUỒN

## CÔNG SUẤT: Pin --> tăng áp 5V với LB-03 --> hạ áp cho điều khiển

Cơ bản: Dùng LX-03 (tăng áp lên 5V) rồi qua AMS1117-3.3 là phương án:
### Ưu điểm: 
- rất ổn định điện áp với 3v3 chuẩn, vi điều khiển không chết, không sập.
- Chống nhiễu tốt
### Nhược điểm
- Pin khai thác được khi >=3v4
- Hao phí điện năng

```mermaid
flowchart TB
 subgraph subGraph0["KHỐI 1: NGUỒN TỔNG (V-Main: 5V)"]
        LX03["LX-03: Sạc & Tăng áp"]
        USB["Cổng USB"]
        PIN[("Pin 18650")]
        SW{"Công tắc"}
  end
 subgraph subGraph1["KHỐI ĐIỀU KHIỂN"]
        D1["Diode 1N5817/SS12/SS14<br><i>(chống dòng ngược về nuôi động cơ)</i>"]
        C_H1["Tụ hóa 470uF (Lọc thô)"]
        C_G1["Tụ gốm 104 (Lọc tinh)"]
        AMS["AMS1117-3.3V"]
        C_H2["Tụ hóa 470uF (Bù áp)"]
        C_G2["Tụ gốm 104 (Lọc cao tần)"]
        ESP32["Mainboard"]
  end
 subgraph subGraph2["KHỐI 3 ĐỘNG CƠ (Mở rộng)"]
        PAD["2 Pad hở - Jumper"]
        C_H3["Tụ hóa <b>470uF </b>x2 <br>Tích điện cho Motor khởi động"]
        C_G3["Tụ gốm 104 <br>Chống nhiễu ngược"]
        DRV["Driver Motor"]
        C_H4["Tụ hóa 470uF <br>Hỗ trợ xả dòng, bảo vệ driver khi đổi tốc độ"]
        C_G4["4x Tụ CBB 104 (Dập tia lửa)"]
        M["4x Động cơ 130"]
  end
    USB L_USB_LX03_0@--> LX03
    PIN L_PIN_LX03_0@<--> LX03
    LX03 L_LX03_SW_0@-- 5V --> SW
    SW L_SW_D1_0@-- "Dây 0.5mm" --> D1
    D1 -- "4.7V<br><b>Dây 0.8mm</b>" --> C_H1
    C_H1 -- Gần &lt; 10mm --> C_G1
    C_G1 -- Sát chân Vin &lt; 3mm --> AMS
    AMS -- "3.3V<br><b>Dây 1.0mm</b>" --> C_H2
    C_H2 -- Gần &lt; 10mm --> C_G2
    C_G2 -- Sát chân VCC &lt; 3mm --> ESP32
    SW L_SW_PAD_0@== "Dây 2.0mm" ==> PAD
    PAD L_PAD_C_H3_0@== 5V<br> ==> C_H3
    C_H3 L_C_H3_C_G3_0@== "Gần Driver<br>Dây 2.5mm để chịu 4A" ==> C_G3
    C_G3 L_C_G3_DRV_0@== Sát chân VCC Driver ==> DRV
    DRV L_DRV_C_H4_0@== "Sau Driver<br>Dây 1.0mm" ==> C_H4
    C_H4 L_C_H4_C_G4_0@== Hàn tại motor ==> C_G4
    C_G4 L_C_G4_M_0@==> M

    style D1 fill:transparent,stroke:#333
    style C_H1 fill:#FFE0B2
    style C_G1 fill:#FFE0B2
    style AMS fill:#FFE0B2
    style C_H2 stroke:#000000,fill:#BBDEFB
    style C_G2 fill:#BBDEFB
    style ESP32 fill:#BBDEFB,stroke:#333
    style PAD fill:#fff,stroke:#333,stroke-dasharray: 5 5
    style C_H3 fill:#FFCDD2
    style C_G3 fill:#FFCDD2
    style DRV fill:#FFCDD2
    style C_H4 fill:#FFCDD2
    style C_G4 stroke:#000000,fill:#C8E6C9
    style M fill:#C8E6C9

    L_USB_LX03_0@{ animation: slow } 
    L_PIN_LX03_0@{ animation: none } 
    L_LX03_SW_0@{ animation: slow } 
    L_SW_D1_0@{ animation: slow } 
    L_SW_PAD_0@{ animation: slow } 
    L_PAD_C_H3_0@{ animation: slow } 
    L_C_H3_C_G3_0@{ animation: slow } 
    L_C_G3_DRV_0@{ animation: slow } 
    L_DRV_C_H4_0@{ animation: slow } 
    L_C_H4_C_G4_0@{ animation: slow } 
    L_C_G4_M_0@{ animation: slow }
```    

## Pin --> hạ áp bằng diot Schottky 

Cơ bản: Dùng trực tiếp pin lithium rồi hạ áp bằng diot SS12/SS14
### Ưu điểm: 
- Giá rẻ
- Ít tổn hao pin
### Nhược điểm
- Pin khai thác được khi >=3v5 
- Nhiễu lớn hơn


## TIẾT KIỆM: Pin --> tăng áp 5V với LB-03 --> hạ áp cho điều khiển
