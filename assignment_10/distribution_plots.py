import matplotlib.pyplot as plt
from random import random

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)

def probability(num_heads, num_flips):
    assert num_flips >= num_heads, "That's not possible"
    total_outcomes = 2 ** num_flips
    desired_outcomes = factorial(num_flips) / (
        factorial(num_heads)*factorial(num_flips - num_heads))
    return round((desired_outcomes / total_outcomes), 5)

def monte_carlo_probability(num_heads, num_flips):
    success = 0
    for i in range(1000):
        flip_list = []
        for n in range(num_flips):
            flip_result = round(random())
            if flip_result == 0:
                flip_list.append("H")
            else:
                flip_list.append("T")
        if flip_list.count("H") == num_heads:
            success += 1
    return (success/1000)

heads = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# part a
plt.style.use('bmh')
plt.plot(heads, [probability(num, 8) for num in heads], linewidth = 2.5)
# part b:
plt.plot(heads, [monte_carlo_probability(num, 8) for num in heads], linewidth = 0.75)
plt.plot(heads, [monte_carlo_probability(num, 8) for num in heads], linewidth = 0.75)
plt.plot(heads, [monte_carlo_probability(num, 8) for num in heads], linewidth = 0.75)
plt.plot(heads, [monte_carlo_probability(num, 8) for num in heads], linewidth = 0.75)
plt.plot(heads, [monte_carlo_probability(num, 8) for num in heads], linewidth = 0.75)
plt.legend(['True', 'MC1', 'MC2', 'MC3', 'MC4', 'MC5'])
plt.xlabel('Number of heads out of eight')
plt.ylabel('Probability')
plt.title('True to MC coin flips probabilties for 8 flips')
plt.savefig('coinflip_plot.png')