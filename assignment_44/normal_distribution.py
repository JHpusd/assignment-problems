import math
import matplotlib.pyplot as plt

def ndf(x):
    # normal distribution function
    return (1/math.sqrt(2*math.pi))*(math.exp((-x**2)/2))

def calc_snd(a,b,n,rule):
    # calc_standard_normal_distribution
    step_size = (b-a)/n
    x_point = a
    x_list = []
    r_sum = 0
    for _ in range(n + 1):
        x_list.append(x_point)
        x_point += step_size
    if rule == "left endpoint":
        for i in range(len(x_list) - 1):
            r_sum += ndf(x_list[i])
        return step_size * r_sum
    elif rule == "right endpoint":
        for x in x_list[1:]:
            r_sum += ndf(x)
        return step_size * r_sum
    elif rule == "midpoint":
        for i in range(len(x_list) - 1):
            r_sum += ndf((x_list[i] + x_list[i+1])/2)
        return step_size * r_sum
    elif rule == "trapezoidal":
        for i in range(len(x_list)):
            if i == 0 or i == len(x_list) - 1:
                r_sum += 0.5 * ndf(x_list[i])
                continue 
                # if there is an error for trapezoidal, check here
            r_sum += ndf(x_list[i])
        return step_size * r_sum
    elif rule == "simpson":
        for i in range(len(x_list)):
            if i == 0 or i == len(x_list) - 1:
                r_sum += ndf(x_list[i])
                continue
            if i % 2 == 1:
                r_sum += 4*ndf(x_list[i])
                continue
            elif i % 2 == 0:
                r_sum += 2*ndf(x_list[i])
                continue
        return (step_size/3) * r_sum

'''
assert round(calc_snd(-1,1), 2) == 0.68
assert round(calc_snd(-2,2), 3) == 0.955
assert round(calc_snd(-3,3), 3) == 0.997
'''

n_list = []
for i in range(2, 101):
    if i % 2 == 0:
        n_list.append(i)
    else:
        continue

plt.style.use('bmh')

left_end_list = []
for n in n_list:
    left_end_list.append(calc_snd(0,1,n,"left endpoint"))
plt.plot(n_list, left_end_list, label="left")

right_end_list = []
for n in n_list:
    right_end_list.append(calc_snd(0,1,n,"right endpoint"))
plt.plot(n_list, right_end_list, label="right")

midpoint_list = []
for n in n_list:
    midpoint_list.append(calc_snd(0,1,n,"midpoint"))
plt.plot(n_list, midpoint_list, label="midpoint")

trapezoid_list = []
for n in n_list:
    trapezoid_list.append(calc_snd(0,1,n,"trapezoidal"))
plt.plot(n_list, trapezoid_list, label="trapezoidal")

simpson_list = []
for n in n_list:
    simpson_list.append(calc_snd(0,1,n,"simpson"))
plt.plot(n_list, simpson_list, label="simpson")

plt.xlabel("n")
plt.ylabel("Estimated value between 0 and 1")
plt.legend(loc="upper right")
plt.savefig('plot.png')

