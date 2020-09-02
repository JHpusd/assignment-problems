def update_bounds(bounds):
    guess = (bounds[0] + bounds[1]) / 2
    if guess ** 2 > 2:
        bounds[1] = guess
    if guess ** 2 < 2:
        bounds[0] = guess

    return bounds

print("Asserting that 'update_bounds' works on input [1, 2]...")
assert update_bounds([1, 2]) == [1, 1.5]
print("PASSED")

print("Asserting that 'update_bounds' works on input [1, 1.5]...")
assert update_bounds([1, 1.5]) == [1.25, 1.5]
print("PASSED")
print("\n")


def estimate_root(precision):
    bounds = [1, 2]
    while bounds[1] - bounds[0] > precision:
        update_bounds(bounds)
    return (bounds[0] + bounds[1]) / 2

print("Asserting that 'estimate_root' works on input 0.1...")
assert estimate_root(0.1) == 1.40625
print("PASSED")
