import math

def gradient_descent(f, x0, alpha, delta, iterations):
    guess = x0
    for i in range(iterations):
        derivative = ((f(guess + 0.5 * delta) - f(guess - 0.5 * delta)) / delta)
        guess -= alpha * derivative
    return round(f(guess), 6)

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
