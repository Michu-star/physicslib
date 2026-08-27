import numpy as np
import matplotlib.pyplot as plt

from ode import euler_first_order, rk4_first_order, euler, rk4

# test Euler vs RK4 first order
'''
def derivative_y(x, y):
    return np.cos(x)

t = np.linspace(0, 10, 100)

y_analytic = np.sin(t)
y_euler = euler_first_order(t, 0, derivative_y)
y_rk4 = rk4_first_order(t, 0, derivative_y)

# plot it
plt.plot(t, y_analytic, color='r', label='analytic')
plt.plot(t, y_euler, color='b', label='euler')
plt.plot(t, y_rk4, color='g', label='rk4')
plt.legend()
plt.show()
'''

# test Euler vs RK4 any order (for a second order ODE)
'''
def state_derivative(x, state):
    x, v = state

    return np.array([
        v,
        -x,
    ])

y0 = np.array([0., 1.])

t = np.linspace(0, 10, 100)
y_analytic = np.sin(t)
y_euler = euler(t, y0, state_derivative)
y_rk4 = rk4(t, y0, state_derivative)

# plot it
plt.plot(t, y_analytic, color='r', label='analytic')
plt.plot(t, y_euler[:, 0], color='b', label='euler')
plt.plot(t, y_rk4[:, 0], color='g', label='rk4')
plt.show()
'''

# test rk RK4 on a set of coupled ODEs of first order
'''
a' = b
b' = -a
'''


def state_derivative(x, state):
    a, b = state

    return np.array([
        b,
        -a,
    ])


a0, b0 = 0, 1

y0 = np.array([a0, b0])

x = np.linspace(0, 2, 100)

solution = rk4(x, y0, state_derivative)

# plot it
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

ax1.plot(x, solution[:, 0], color='r', label='a')
ax1.plot(x, solution[:, 1], color='b', label='b')
ax1.set_title("Plot x vs a and b")
ax1.legend()

ax2.plot(solution[:, 0], solution[:, 1], color='g')
ax2.set_title("Plot a vs b")
ax2.set_xlabel("a")
ax2.set_ylabel("b")
ax2.set_aspect('equal')

plt.tight_layout()
plt.show()
