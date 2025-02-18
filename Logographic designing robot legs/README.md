# 🦿 Bipedal Robot Walking Algorithm (20 Steps)

## **📌 Introduction**
This project implements a **bipedal walking algorithm** that simulates human-like movement for a robot using **inverse kinematics and physics principles**. The algorithm calculates joint angles for **hip and knee movements** over **20 steps**, ensuring a smooth, realistic gait.

---

## **🤖 What is This Algorithm?**
A **bipedal walking algorithm** is a **set of mathematical rules** that govern how a two-legged robot (like a humanoid) moves its legs to mimic **human walking**. The key components of this algorithm are:

1️⃣ **Trajectory Generation:** Determines how each leg moves through space.  
2️⃣ **Inverse Kinematics:** Computes joint angles (hip, knee) to achieve the desired movement.  
3️⃣ **Balance Control:** Ensures the robot remains stable while shifting weight.  

This is achieved using principles from **physics, biomechanics, and robotics**.

---

## **⚙️ Relation to Physics**
The algorithm is deeply rooted in physics concepts, particularly in **mechanics and motion dynamics**:

### **1️⃣ Kinematics - Motion Without Forces**
- The algorithm uses **inverse kinematics** to determine the required **joint angles**.
- It applies **trigonometry** to compute **hip and knee angles** based on the foot’s position.
- The **Law of Cosines** is used to calculate the bending of the knee.

**Mathematical Equation:**
\[
\theta_2 = \cos^{-1} \left(\frac{L^2 - a^2 - b^2}{2ab}\right)
\]
Where:
- \( L \) = Distance from hip to foot
- \( a, b \) = Lengths of thigh and shin
- \( \theta_2 \) = Knee angle

### **2️⃣ Dynamics - How Forces Affect Motion**
- Walking requires shifting the **center of mass (CoM)** to prevent falling.
- The equation for **balance** follows:
\[
ZMP = \frac{\sum (m_i \cdot x_i)}{\sum m_i}
\]
Where:
- \( ZMP \) = Zero Moment Point (balance point)
- \( m_i \) = Mass of each segment
- \( x_i \) = Position of each mass

### **3️⃣ Ground Reaction Force (GRF)**
- The robot must exert enough force against the ground to lift the foot.
- Newton’s **Third Law of Motion** applies:
\[
F_{\text{ground}} = -F_{\text{body}}
\]
Where:
- \( F_{\text{ground}} \) is the reaction force from the ground.
- \( F_{\text{body}} \) is the weight of the robot.

---

## **🛠️ How the Algorithm Works**
### **1️⃣ Step Planning**
- The robot lifts one leg **every alternate step**.
- The step length and height are predefined for balance.

### **2️⃣ Angle Calculation**
- Uses **inverse kinematics** to calculate required hip and knee angles.

### **3️⃣ Motor Commands**
- Converts angle calculations into signals for actuators.

---

## **🚀 Running the Simulation**
### **1️⃣ Install Required Libraries**
```bash
pip install matplotlib

2️⃣ Run the Python Script

python walking_algorithm.py

Graph Visualization

The foot trajectory is plotted, showing the movement pattern.


