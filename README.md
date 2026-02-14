
# Radiation-Aware Self-Optimizing 6T SRAM Using Reinforcement Learning Based Adaptive Body Biasing in 180nm CMOS

## Overview

This project presents a radiation-resilient 6T SRAM cell designed in 180nm CMOS and optimized using Reinforcement Learning (RL) combined with Dynamic Body Biasing (DBB).

The main objective of this work is to improve:

- Critical Charge (Qcrit)
- Static Noise Margin (SNM)
- Radiation recovery time

while maintaining reasonable delay and power.

Instead of manually tuning transistor sizing and body bias, a reinforcement learning agent is used to automatically search for optimal design parameters.

---

## Motivation

SRAM cells are highly sensitive to radiation-induced transient faults, especially in scaled technologies. A radiation strike can inject charge into a sensitive node and flip the stored data.

Traditional approaches improve robustness by:

- Increasing transistor sizing
- Layout hardening
- Adding redundancy

However, these methods increase area or power.

In this project, I explore an alternative approach:

Use reinforcement learning to automatically optimize transistor sizing and body bias voltage to maximize radiation tolerance.

---

## Project Structure

1_Baseline_Design
2_Radiation_Model
3_Manual_Body_Bias_Sweep
4_RL_Framework
5_Results

### 1_Baseline_Design
Contains baseline 6T SRAM behavior:
- Hold SNM butterfly curve
- Transient waveform
- Qcrit extraction
- Design parameters

### 2_Radiation_Model
Includes:
- Double exponential current pulse model
- Radiation-induced voltage disturbance
- Injection configuration

### 3_Manual_Body_Bias_Sweep
Before applying RL, body bias voltage was manually swept to observe:
- Qcrit variation
- SNM improvement
- Recovery time behavior

This validates the physical impact of body biasing.

### 4_RL_Framework
Contains the reinforcement learning implementation:
- Environment model
- DQN agent
- Reward function
- Training script

The agent adjusts:
- PMOS/NMOS sizing
- Body bias voltage

to maximize a reward function based on Qcrit and SNM.

### 5_Results
Includes:
- Qcrit improvement curves
- SNM comparison
- Delay and power comparison
- Recovery time comparison
- RL reward convergence plots
- Monte Carlo robustness evaluation

---

## Radiation Model

Radiation strike is modeled using a double exponential current pulse:

Iinj = I0 * exp(-t/tau1) * (1 - exp(-t/tau2))

This represents a realistic transient charge injection event in 180nm CMOS.

---

## Reinforcement Learning Strategy

State includes:
- Qcrit
- SNM
- Delay
- Power
- Body bias
- Transistor sizing ratio

Actions include:
- Adjust PMOS width
- Adjust NMOS width
- Modify body bias voltage

Reward is designed to:
- Maximize Qcrit
- Maximize SNM
- Penalize delay and power increase

---

## Key Results (Expected Trend)

| Metric | Baseline | After RL + DBB |
|--------|----------|----------------|
| Qcrit  | ~25 fC   | ~40 fC        |
| SNM    | ~180 mV  | ~220 mV       |
| Recovery Time | ~600 ps | ~350 ps |

The RL-based adaptive body biasing significantly improves radiation tolerance while keeping power overhead moderate.

---

## Tools Used

- Python (TensorFlow, NumPy, Matplotlib)
- Cadence Virtuoso
- Physics-based modeling for radiation effects

---

## Future Work

- Replace simulated environment with full SPICE-in-the-loop integration
- Extend to 65nm and below
- Explore PPO instead of DQN
- Investigate layout-level radiation hardening integration

---

## Author

Urbee Datta  
B.Tech – Electronics & Telecommunication Engineering  
Focus: VLSI + AI-driven circuit optimization
=======

>>>>>>> 5b58c8dea570d3aee4fa0f6deda53b0d4d016c26
