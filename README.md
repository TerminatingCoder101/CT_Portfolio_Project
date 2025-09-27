# Computational Finance Portfolio Project

The project explores **derivative pricing** using two core numerical methods:
- **Monte Carlo Simulation (MC)**
- **Finite Difference Methods (PDE Solvers)**

The goal is to compare the efficiency, accuracy, and usability of the approaches in European options pricing under the **Black–Scholes model**.

---

## 📌 Objectives

- Perform **Monte Carlo simulations** for European option pricing.
- Numerically solve the **Black–Scholes PDE** with finite difference methods.
- Compare two approaches based on accuracy, efficiency, and convergence.
- Present a modular and extensible computational finance codebase.

---

## 🧮 Mathematical Foundations

### 1. Black–Scholes Model

The derivative price \( V(S, t) \) of a derivative under the **Black–Scholes PDE** is described by:

\[
\frac{\partial V}{\partial t} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + r S \frac{\partial V}{\partial S} - rV = 0,
\]

where:
- \( S \) = underlying asset price  
- \( t \) = time  
- \( r \) = risk-free interest rate  
- \( \sigma \) = volatility  

For a European call option with maturity \( T \) and strike \( K \):  

\[
V(S, T) = \max(S - K, 0).
\]

---

### 2. Monte Carlo Simulation

We model the **underlying asset dynamics** by using **Geometric Brownian Motion (GBM):**

\[
dS_t = r S_t dt + \sigma S_t dW_t,
\]

which has the solution:

\[
S_T = S_0 \exp\left[\left(r - \tfrac{1}{2}\sigma^2\right)T + \sigma W_T\right],
\]

where \( W_T \sim \mathcal{N}(0, T) \).  

The **Monte Carlo price** of a European call is:

\[
C_0 = e^{-rT} \cdot \mathbb{E}[\max(S_T - K, 0)].
\]

---

### 3. Finite Difference Method (PDE Solver)

We discretize the Black–Scholes PDE on a spatial and temporal grid. 

- **Explicit Scheme**: Forward in time, central in space (conditionally stable).  
- **Implicit Scheme**: Backward in time, unconditionally stable.  
- **Crank–Nicolson Scheme**: Averages explicit and implicit, second-order accurate.  

The basic update formula for grid point \( (i, j) \) is based on the coefficients of the PDE:

\[
V^{n+1}_i = a_i V^n_{i-1} + b_i V^n_i + c_i V^n_{i+1},
\]

with coefficients depending on \( r, \sigma, S, \Delta t, \Delta S \).  

---

## ⚙️ Core Components

- `mc_simulation.py` → Monte Carlo pricing engine.  
- `pde_solver.py` → Finite difference solvers (Explicit, Implicit, Crank–Nicolson).  
- `utils.py` → Common functions (payoffs, error metrics, plotting).  
- `main.py` → Entry point for running experiments.  

---

## 📊 Results

### Monte Carlo vs PDE Pricing

We tested with parameters:  
- \( S_0 = 100, K = 100, r = 0.05, \sigma = 0.2, T = 1 \).  

- **Monte Carlo Price** (1M paths): ≈ `10.45`  
- **PDE (Crank–Nicolson)**: ≈ `10.43`  
- **Black–Scholes Closed Form**: ≈ `10.45`  

This shows **excellent agreement** between methods.

---

### Convergence of Monte Carlo

Error decreases as \( \frac{1}{\sqrt{N}} \) with number of paths:

![Monte Carlo Convergence](results/monte_carlo_convergence.png)

---

### PDE Stability & Accuracy

Crank–Nicolson achieves stable, accurate solutions compared to Explicit:

![PDE Stability](results/pde_solutions.png)

---

## 🚀 Achievements

- Created a general framework for **option pricing**.
- Highlighted significant differences between **stochastic simulation** and **deterministic PDE methods**.
- Verified correctness against **closed-form Black–Scholes solution**.

---
