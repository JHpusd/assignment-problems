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
    return round((desired_outcomes / total_outcomes), 6)

'''
print("Asserting that 'probability' works...")
assert probability(5, 8) == 0.21875
print("PASSED")
print("\n")
'''

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
'''
print("Monte Carlo probabilities for 5 heads out of 8 flips:")
for i in range(5):
    print(monte_carlo_probability(5, 8))
'''