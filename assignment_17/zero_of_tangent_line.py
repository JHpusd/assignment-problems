def zero_of_tangent_line(c):
    x = c
    y = (x**3) + x - 1
    slope = 3*(x**2) + 1
    y_int = y - (x * slope)
    x_int = (-1 * y_int) / slope
    return round(x_int, 6)

print("Testing that 'zero_of_tangent_line' works...")
assert zero_of_tangent_line(0.5) == 0.714286
print("PASSED")


def estimate_solution(init_guess, precision):
    guess = init_guess
    next_guess = 0
    while True:
        next_guess = zero_of_tangent_line(guess)
        if abs(guess - next_guess) <= precision:
            return zero_of_tangent_line(next_guess)
        else:
            guess = next_guess

print("Testing that 'estimate_solution' works...")
assert estimate_solution(0.5, 0.01) == 0.682328
print("PASSED")
