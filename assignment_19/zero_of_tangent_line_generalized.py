def f(x):
    return x**3 + x - 1

def estimate_derivative(c, delta):
    return round(((f(c + 0.5 * delta) - f(c - 0.5 * delta)) / delta), 6)

def zero_of_tangent_line(c, delta):
    x = c
    y = f(c)
    slope = estimate_derivative(c, delta)
    y_int = y - (x * slope)
    x_int = (-1 * y_int) / slope
    return round(x_int, 6)

def estimate_solution(c, delta, precision):
    guess = c
    next_guess = 0
    while True:
        next_guess = zero_of_tangent_line(c, delta)
        if abs(c - next_guess) <= precision:
            return zero_of_tangent_line(next_guess, delta)
        else:
            c = next_guess

print("Testing generalized 'zero_of_tangent_line' and 'estimate_solution'...")
assert zero_of_tangent_line(0.5, 0.001) == 0.714286
assert estimate_solution(0.5, 0.001, 0.01) == 0.682328
print("PASSED")
