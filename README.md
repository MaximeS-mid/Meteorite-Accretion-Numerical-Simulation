# Modeling the Abrasion of a Meteorite

**Author:** Maxime S.

**Date:** 2022

---

## 📌 Project Overview

This project aims to model the **abrasion of a meteorite** as it enters Earth's atmosphere. The study is inspired by the **Centrale TSI 2015 Physics-Chemistry exam** and a classroom exercise, but extends these models by relaxing key assumptions (e.g., constant meteorite mass) and implementing a **numerical simulation in Python**.

The project is divided into three parts:
1. **Simplified model** (constant mass).
2. **Improved model** (variable mass).
3. **Numerical simulation** and analysis of parameter influence.

---

## 🔍 Problem Statement

A meteorite enters the atmosphere at a speed of **19 km/s** and an angle of **70°**. The goal is to:
- Model its **trajectory**, **velocity**, and **mass loss** due to atmospheric abrasion.
- Compare the simplified model (constant mass) with a more realistic model (variable mass).
- Analyze the influence of parameters such as the **drag coefficient** (\(C_D\)) and **atmospheric thickness** (\(H\)).

---

## 📚 Methodology

### 1. Theoretical Models
- **Simplified model**: Assumes the meteorite's mass remains constant during atmospheric entry. The equation of motion is derived from drag force and gravity.
- **Improved model**: Considers mass loss due to sublimation, using energy conservation and momentum variation. The meteorite is modeled as a **spherical body with variable mass**.

### 2. Numerical Simulation
- **Python implementation**: Uses the **Euler method** to solve the differential equations for velocity and mass as a function of position.
- **Stopping conditions**: The simulation stops when the meteorite reaches the impact point or when its velocity falls below a critical threshold.
- **Parameter study**: The influence of \(C_D\) and \(H\) on the meteorite's mass and velocity is analyzed.

---

## 📊 Results

### Key Findings
- The **simplified model** (constant mass) predicts an unrealistic mass loss, exceeding the meteorite's initial mass.
- The **improved model** (variable mass) provides more realistic results, with a final mass of **63 tons** (0.5% of the initial mass) for \(C_D = 0.3\) and \(H = 20\) km.
- The **drag coefficient** (\(C_D\)) and **atmospheric thickness** (\(H\)) significantly affect the meteorite's mass and velocity:
  - Higher \(C_D\) leads to faster deceleration and mass loss.
  - Thicker atmospheres (\(H > 30\) km) invalidate the assumption of negligible gravity compared to drag force.

### Visualizations
- **Graphs**: Mass and velocity as a function of position for different \(C_D\) and \(H\) values.
- **Tables**: Summary of remaining mass at impact for various parameters.

![Mass and velocity vs. position for varying \C_D\ and \(H = 20\) km](images/abrasion_image)

---
