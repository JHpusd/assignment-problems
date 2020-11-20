import matplotlib.pyplot as plt
import math

a = 2.2145965786666670808
b = -0.693147181

def f(x):
    return 1 / (1 + math.exp(a + b * x))

x_coords = [1, 2, 3]
y_coords = []
for num in x_coords:
    y_coords.append(f(num))

plt.style.use('bmh')
plt.plot(x_coords, y_coords)
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('logistic_regression.png')
