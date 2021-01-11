import math

def normal_distribution_function(x):
    return (1/math.sqrt(2*math.pi))*(math.exp((-x**2)/2))

def calc_standard_normal_distribution(a,b):
    r_sum = 0
    point = a
    while point <= b:
        r_sum += 0.001*normal_distribution_function(point)
        point += 0.001
    return r_sum

assert round(calc_standard_normal_distribution(-1,1), 2) == 0.68
assert round(calc_standard_normal_distribution(-2,2), 3) == 0.955
assert round(calc_standard_normal_distribution(-3,3), 3) == 0.997
