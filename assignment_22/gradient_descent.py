import math

def gradient_descent(f, initial_point, alpha, delta, iterations):
    x_guess = initial_point[0]
    y_guess = initial_point[1]
    for i in range(iterations):
        x_derivative = (f(x_guess + 0.5 * delta, y_guess) - f(x_guess - 0.5 * delta, y_guess)) / delta
        y_derivative = (f(x_guess, y_guess + 0.5 * delta) - f(x_guess, y_guess - 0.5 * delta)) / delta
        x_guess -= alpha * x_derivative
        y_guess -= alpha * y_derivative
    return round(f(x_guess, y_guess), 6)
'''
print("Testing that 'gradient_descent' works...")
def f(x):
    return x**2 + 2*x + 1

assert gradient_descent(f, 0, 0.01, 0.0001, 10000) == 0
print(" ")
def f(x):
    return (x**2 + math.cos(x)) / math.exp(math.sin(x))
print("Minimum value of the graph of (x^2 + cos(x))/e^sin(x)):")
print(gradient_descent(f, 0, 0.01, 0.0001, 10000))
# this matches with the actual graph of the function
print(" ")
print("PASSED")
'''
# Problem 25-1
# a:
# The minimum of the function f(x, y) = 1 + x**2 + y**2 is 1

# b:
def f(x, y):
    return 1 + x**2 + y**2
assert gradient_descent(f, (1, 2), 0.01, 0.0001, 10000) == 1
# matches up with part a

# c.
'''
1 + x**2 + 2x + y**2 - 9y
= (x + 1)**2 + (y - 4.5)**2 - 4.5**2

minimum value is -(4.5**2) = -20.25
'''

# d.
def f(x, y):
    return 1 + x**2 + 2*x + y**2 + 9*y
assert gradient_descent(f, (0, 0), 0.01, 0.0001, 10000) == -20.25
# matches up with part c
