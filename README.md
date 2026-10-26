# `physicslib` — Numerical ODE Solvers in Python

A lightweight, installable Python library providing explicit numerical integrators for scalar first-order ordinary differential equations (ODEs) and coupled systems of first-order ODEs.

## Implemented Methods

All integrators are located in `physicslib.ode` and operate on arbitrary (potentially non-uniform) 1D grids `x`:

- **Explicit Euler Method** (`euler_first_order`, `euler`):
  First-order explicit integration step:
  $$\mathbf{y}_{i+1} = \mathbf{y}_i + \mathbf{f}(x_i, \mathbf{y}_i)\,\Delta x_i$$

- **Classical 4th-Order Runge–Kutta (RK4)** (`rk4_first_order`, `rk4`):
  Fourth-order accurate single-step integration ($\mathcal{O}(\Delta x^4)$ global truncation error):
  $$\mathbf{k}_1 = \mathbf{f}(x_i, \mathbf{y}_i)$$
  $$\mathbf{k}_2 = \mathbf{f}\!\left(x_i + \frac{\Delta x_i}{2},\, \mathbf{y}_i + \frac{\Delta x_i}{2}\mathbf{k}_1\right)$$
  $$\mathbf{k}_3 = \mathbf{f}\!\left(x_i + \frac{\Delta x_i}{2},\, \mathbf{y}_i + \frac{\Delta x_i}{2}\mathbf{k}_2\right)$$
  $$\mathbf{k}_4 = \mathbf{f}(x_i + \Delta x_i,\, \mathbf{y}_i + \Delta x_i\,\mathbf{k}_3)$$
  $$\mathbf{y}_{i+1} = \mathbf{y}_i + \frac{\Delta x_i}{6}\left(\mathbf{k}_1 + 2\mathbf{k}_2 + 2\mathbf{k}_3 + \mathbf{k}_4\right)$$

## Installation

Install directly from GitHub:

```bash
pip install git+https://github.com/Michu-star/physicslib.git
```

Or install locally in editable mode:

```bash
pip install -e .
```

## Usage Example

```python
import numpy as np
from physicslib.ode import rk4

# Harmonic oscillator: y'' = -omega^2 * y  ->  state = [y, v]
def harmonic_rhs(t, state, omega):
    y, v = state
    return np.array([v, -omega**2 * y])

t = np.linspace(0.0, 10.0, 1000)
y0 = np.array([1.0, 0.0])

solution = rk4(t, y0, harmonic_rhs, args=(2.0,))
```
