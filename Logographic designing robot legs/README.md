# 🦿 Bipedal Robot Walking Algorithm (20 Steps)

This project implements a **bipedal robot walking algorithm** that simulates human-like walking using **inverse kinematics**. The algorithm calculates joint angles for 20 steps and ensures smooth motion by controlling the **hip and knee joints** while visualizing the foot trajectory.

---

## 📌 Features
✅ Simulates **20 walking steps** for a two-legged robot  
✅ Calculates **hip and knee joint angles** using inverse kinematics  
✅ Implements **step alternation** to simulate natural walking  
✅ **Avoids math errors** with built-in range handling  
✅ Provides **a visual plot of foot movement**  
✅ **Compatible with Python Spyder & Jupyter Notebook**  

---

## 🛠️ How It Works
### 1️⃣ Inverse Kinematics Calculation
- **Hip Angle (θ1)** is determined using `atan2(y, x)`, which gives the **angle of the hip relative to the ground**.
- **Knee Angle (θ2)** is calculated using the **law of cosines** to determine the bending angle.

### 2️⃣ Walking Trajectory
- The robot **alternates foot movement** with a **fixed step length and height**.
- Each foot lifts **every alternate step** to simulate natural walking.

### 3️⃣ Motor Command Execution
- The calculated angles for **hip and knee** are **sent to the robot's motors**.
- A **delay is added** to simulate real-time movement.

---

## 📜 Code Overview
The full implementation can be found in **walking_algorithm.py**. The main components include:

### 🔹 Import Required Libraries
```python
import math
import time
import matplotlib.pyplot as plt
