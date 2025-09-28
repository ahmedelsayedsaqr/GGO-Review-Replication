import numpy as np

def sphere(x):
    return np.sum(x**2)

def rastrigin(x):
    n = len(x)
    return 10 * n + np.sum(x**2 - 10 * np.cos(2 * np.pi * x))

def ackley(x):
    n = len(x)
    return -20 * np.exp(-0.2 * np.sqrt(np.sum(x**2) / n)) - np.exp(np.sum(np.cos(2 * np.pi * x)) / n) + 20 + np.e

def rosenbrock(x):
    return np.sum(100 * (x[1:] - x[:-1]**2)**2 + (x[:-1] - 1)**2)

def griewank(x):
    i = np.arange(1, len(x) + 1)
    return np.sum(x**2) / 4000 - np.prod(np.cos(x / np.sqrt(i))) + 1

BENCHMARKS = {
    "sphere": (sphere, -100, 100),
    "rastrigin": (rastrigin, -5.12, 5.12),
    "ackley": (ackley, -32, 32),
    "rosenbrock": (rosenbrock, -5, 10),
    "griewank": (griewank, -600, 600),
}
