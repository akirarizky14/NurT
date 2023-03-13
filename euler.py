import numpy as np
import matplotlib.pyplot as plt

# Define the function f(t, y) in the Cauchy problem dy/dt = f(t, y)
class Koshi:
    def f(t, y):
        return -y + t
    # Define the initial condition y(0) = y0
    y0 = 1

    # Define the time interval [t0, tf] and the step size h
    t0 = 0
    tf = 1
    h = 0.01

    # Create arrays to store the time and solution values
    t = np.arange(t0, tf + h, h)
    y = np.zeros_like(t)
    y[0] = y0

    # Use the Euler method to solve the Cauchy problem
    for i in range(1, len(t)):
        y[i] = y[i-1] + h * f(t[i-1], y[i-1])


    # Plot the solution
    plt.plot(t, y)
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title('Solution of dy/dt = -y + t with y(0) = {}'.format(y0))
    plt.show()

