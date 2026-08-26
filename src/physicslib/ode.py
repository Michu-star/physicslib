import numpy as np


# These functions solve ODEs of only the first order
def euler_first_order(x, y0, derivative_y):
    dx = np.diff(x)
    y = np.zeros_like(x)
    y[0] = y0

    for i in range(len(x) - 1):
        y[i + 1] = y[i] + derivative_y(x[i], y[i]) * dx[i]

    return y


def rk4_first_order(x, y0, derivative_y):
    dx = np.diff(x)
    y = np.zeros_like(x)
    y[0] = y0

    for i in range(len(x) - 1):
        k1 = derivative_y(x[i], y[i])
        k2 = derivative_y(x[i] + dx[i]/2, y[i] + k1 * dx[i]/2)
        k3 = derivative_y(x[i] + dx[i]/2, y[i] + k2 * dx[i]/2)
        k4 = derivative_y(x[i] + dx[i], y[i] + k3 * dx[i])

        slope = (k1 + 2 * k2 + 2 * k3 + k4) / 6

        y[i + 1] = y[i] + slope * dx[i]

    return y


# Helper function for Euler and RK4
def derivative_state(x, state, last_derivative, args=()):
    derivative = np.zeros_like(state)

    # y', ..., y^(n-1)
    derivative[:-1] = state[1:]
    # y^n
    derivative[-1] = last_derivative(x, state, *args)

    return derivative


# These functions solve ODEs of any order
def euler(x, y0, nth_derivative_y, args=()):
    dx = np.diff(x)
    n = len(y0)

    y = np.zeros((np.size(x), n))
    y[0] = y0

    for i in range(len(x) - 1):
        # y, y', ..., y^(n-1)
        y[i + 1] = y[i] + derivative_state(x[i], y[i], nth_derivative_y, args) * dx[i]

    return y


def rk4(x, y0, nth_derivative_y, args=()):
    dx = np.diff(x)
    n = len(y0)

    y = np.zeros((np.size(x), n))
    y[0] = y0

    for i in range(len(x) - 1):
        k1 = derivative_state(x[i], y[i],
                              nth_derivative_y, args)

        k2 = derivative_state(x[i] + dx[i] / 2,
                              y[i] + k1 * dx[i] / 2,
                              nth_derivative_y, args)

        k3 = derivative_state(x[i] + dx[i] / 2,
                              y[i] + k2 * dx[i] / 2,
                              nth_derivative_y, args)

        k4 = derivative_state(x[i] + dx[i],
                              y[i] + k3 * dx[i],
                              nth_derivative_y, args)

        slope = (k1 + 2 * k2 + 2 * k3 + k4) / 6

        y[i + 1] = y[i] + slope * dx[i]

    return y


def rk4_system(x, y0, state_derivative, args=()):
    dx = np.diff(x)
    n = len(y0)

    y = np.zeros((np.size(x), n))
    y[0] = y0

    for i in range(len(x) - 1):
        k1 = state_derivative(x[i], y[i], *args)

        k2 = state_derivative(x[i] + dx[i] / 2,
                              y[i] + k1 * dx[i] / 2,
                              *args)

        k3 = state_derivative(x[i] + dx[i] / 2,
                              y[i] + k2 * dx[i] / 2,
                              *args)

        k4 = state_derivative(x[i] + dx[i],
                              y[i] + k3 * dx[i],
                              *args)

        slope = (k1 + 2 * k2 + 2 * k3 + k4) / 6

        y[i + 1] = y[i] + slope * dx[i]

    return y
