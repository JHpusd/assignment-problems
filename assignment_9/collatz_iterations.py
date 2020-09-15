
def collatz_iterations(number):
    if number <= 1:
        return 0
    counter = 0
    while number != 1:
        if number % 2 == 0:
            number /= 2
            counter += 1
        if number == 1:
            return counter
        if number % 2 == 1:
            number = 3*number + 1
            counter += 1

print("Testing that 'collatz_iterations' works...")
assert collatz_iterations(13) == 9
print("PASSED")


ref_num = 0
for i in range(1, 1001):
    if collatz_iterations(i) > ref_num:
        ref_num = collatz_iterations(i)
        print(i)
print("most collatz_iterations: {}".format(ref_num))
'''
# From 1-1000, 871 has the highest amount of 
collatz iterations with 178 iterations. 
'''


'''
x_coords = []
y_coords = []
for num in range(1, 1001):
    x_coords.append(num)
for x in x_coords:
    y_coords.append(collatz_iterations(x))

import matplotlib.pyplot as plt
plt.style.use('bmh')
plt.plot(x_coords, y_coords)
plt.xlabel("Number")
plt.ylabel("Number of collatz iterations")
plt.title("Collatz iterations of numbers 1-1000")
plt.savefig("plot.png")
'''