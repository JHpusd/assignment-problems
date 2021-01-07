from random import random

def random_draw(distribution):
    cumulative_dist = []
    total = 0
    for val in distribution:
        total += val
        cumulative_dist.append(total)
    random_num = random()
    for val in cumulative_dist:
        if val > random_num:
            return cumulative_dist.index(val)

def expected_val(distribution):
    result = 0
    for i in range(len(distribution)):
        result += i * distribution[i]
    return result

print("Testing random_draw on distribution [0.5, 0.5]...")
distribution = [0.5, 0.5]
print("Expected value is " + str(expected_val(distribution)))
total_val = 0
for _ in range(1000):
    total_val += random_draw(distribution)
print("Average for 1000 samples is " + str(total_val/1000))
print(" ")
print("Testing random_draw on distribution [0.25, 0.25, 0.5]...")
distribution = [0.25, 0.25, 0.5]
print("Expected value is " + str(expected_val(distribution)))
total_val = 0
for _ in range(1000):
    total_val += random_draw(distribution)
print("Average for 1000 samples is " + str(total_val/1000))
print(" ")
print("Testing random_draw on distribution [0.05, 0.2, 0.15, 0.3, 0.1, 0.2]...")
distribution = [0.05, 0.2, 0.15, 0.3, 0.1, 0.2]
print("Expected value is " + str(expected_val(distribution)))
total_val = 0
for _ in range(1000):
    total_val += random_draw(distribution)
print("Average for 1000 samples is " + str(total_val/1000))
