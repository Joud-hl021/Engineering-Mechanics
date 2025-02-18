# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 22:26:14 2025

@author: Judea
"""

import math
import time
import matplotlib.pyplot as plt

# 📌 Define robot leg specifications
thigh_length = 100  # Thigh length in mm
shin_length = 100   # Shin length (below knee) in mm
step_length = 50    # Step length in mm
step_height = 20    # Step height while walking in mm
speed = 0.5         # Walking speed (seconds per step)
total_steps = 20    # Total number of steps

# 📌 Function to calculate joint angles
def calculate_leg_angles(x, y, thigh_length, shin_length):
    L = math.sqrt(x**2 + y**2)  
    if L > (thigh_length + shin_length):  
        L = thigh_length + shin_length - 1  

    theta1 = math.atan2(y, x)  
    cos_theta2 = (L**2 - thigh_length**2 - shin_length**2) / (2 * thigh_length * shin_length)

    if abs(cos_theta2) > 1:
        cos_theta2 = max(-1, min(1, cos_theta2))  
    
    theta2 = math.acos(cos_theta2)  
    return math.degrees(theta1), math.degrees(theta2)

# 📌 Function to generate walking trajectory
def generate_walk_trajectory(steps, step_length, step_height):
    trajectory = []
    for i in range(steps):
        x = step_length if i % 2 == 0 else 0  # Alternating foot forward
        y = step_height if i % 2 == 0 else 0  # Lift foot at every alternate step
        trajectory.append((x, y))
    return trajectory

# 📌 Function to send motor commands
def send_motor_commands(theta1, theta2, step_num):
    print(f"🦿 Step {step_num}: Hip Angle {theta1:.2f}°, Knee Angle {theta2:.2f}°")
    time.sleep(speed)  # Simulate real movement delay

# 📌 Generate trajectory and execute walking
trajectory = generate_walk_trajectory(total_steps, step_length, step_height)

for step_num, pos in enumerate(trajectory):
    theta1, theta2 = calculate_leg_angles(pos[0], pos[1], thigh_length, shin_length)
    send_motor_commands(theta1, theta2, step_num + 1)

# 📌 Plot foot trajectory during walking
plt.figure(figsize=(6, 4))
x_points, y_points = zip(*trajectory)
plt.plot(x_points, y_points, marker='o', linestyle='-', color='b')
plt.xlabel("Horizontal Distance (mm)")
plt.ylabel("Vertical Height (mm)")
plt.title("Foot Trajectory During Walking")
plt.grid()

# ✅ Show the plot
plt.show()
