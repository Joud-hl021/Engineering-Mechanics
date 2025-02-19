# Robotic Arm Torque Calculation and Servo Selection

## 1. Introduction
This project involves calculating the required torque for each joint of a robotic arm (as shown in the provided image) and selecting suitable servo motors for each joint.

---

## 2. Torque Calculations

We assume:
- The payload (end effector load) is 1 kg.
- Gravitational acceleration (g) is 9.81 m/s².
- Arm segment lengths (from the image):
  - Segment 1 (Base to Joint 2): 15 cm (0.15 m)
  - Segment 2 (Joint 2 to Joint 3): 10 cm (0.10 m)
  - Segment 3 (Joint 3 to End Effector): 4 cm (0.04 m)

The torque \(\tau\) at each joint is given by:
\[
\tau = F \times d
\]
where:  
- \(\tau\) = Torque in N·m  
- \(F\) = Force in Newtons (N)  
- \(d\) = Distance from the joint (m)  

### 2.1 Force Due to the Payload
\[
F = m \times g = 1\,\text{kg} \times 9.81\,\text{m/s}^2 = 9.81\,\text{N}
\]

### 2.2 Torque at Each Joint

1. Joint 1 (Base)
   - The load is effectively acting at the full arm length (sum of all segments: 0.15 + 0.10 + 0.04 = 0.29 m).  
   \[
   \tau_1 = 9.81 \times 0.29 \approx 2.84\,\text{N·m}
   \]

2. Joint 2 (Elbow)
   - The load is effectively at the length of the second and third segments (0.10 + 0.04 = 0.14 m).  
   \[
   \tau_2 = 9.81 \times 0.14 \approx 1.37\,\text{N·m}
   \]

3. Joint 3 (Wrist)
   - The load is effectively at the length of the third segment only (0.04 m).  
   \[
   \tau_3 = 9.81 \times 0.04 \approx 0.39\,\text{N·m}
   \]

> Note: These calculations assume the arm segments themselves are massless, and only the 1 kg payload is considered. In a real design, you would include the mass of each arm segment, gripper, etc.

---

## 3. Servo Motor Selection

When choosing servo motors, it’s recommended to have a safety margin above the calculated torque (e.g., 20-30% higher). Below is an example selection:

| Joint           | Required Torque (N·m) | Recommended Servo   | Approx. Rated Torque | Purchase Link                                                                 |
|-----------------|-----------------------|---------------------|----------------------|--------------------------------------------------------------------------------|
| Joint 1     | ~2.84 N·m            | JMC 180W AC Servo   | 3.0 N·m             | [Alibaba Link](https://www.alibaba.com/product-detail/JMC-180w-AC-servo-motor-60ST-M01330_1600784390045.html) |
| Joint 2     | ~1.37 N·m            | MG996R              | ~1.8 N·m            | [Amazon Link](https://www.amazon.sa/dp/B07MFK266B)                            |
| Joint 3     | ~0.39 N·m            | MG90S               | ~0.4 N·m            | [Jeem3 Link](https://jeem3.com/nDEWBb)                                        |

> Important: Make sure the servo motor’s rated torque meets or exceeds the required torque. Also check operating voltage, current, and physical dimensions.

---

## 4. Usage Instructions
1. Mount the Servos: Install each servo at its corresponding joint.  
2. Power Supply: Ensure a suitable power supply that can provide the necessary voltage and current for all servos.  
3. Controller/Driver: Use a microcontroller (e.g., Arduino, ESP32, etc.) and appropriate drivers or servo shields to control the servos.  
4. Calibration: Calibrate the arm’s angles and test with lower weights before applying the full 1 kg payload.

---

## 5. Contributing
- Fork this repository.  
- Make your changes (e.g., different servo suggestions, refined calculations).  
- Create a Pull Request for review.

---

## 6. References
- [Engineering Toolbox: Torque & Force Calculations](https://www.engineeringtoolbox.com)  
- [Servo Database](https://www.servodatabase.com)
