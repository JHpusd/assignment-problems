def skip_factorial_nonrecursive(n):
    assert int(n) == n, "input needs to be an integer"
    next_term = n
    result_num = 1
    while next_term >= 1:
        result_num *= next_term
        next_term -= 2
    return result_num

print("Asserting that 'skip_factorial_nonrecursive' works...")
assert skip_factorial_nonrecursive(6) == 48
assert skip_factorial_nonrecursive(7) == 105
print("PASSED")
print("\n")


def skip_factorial_recursive(n):
    if n <= 2:
        if n % 2 == 0:
            return 2
        else:
            return 1
    return n * skip_factorial_recursive(n-2)

print("Asserting that 'skip_factorial_recursive' works...")
assert skip_factorial_recursive(6) == 48
assert skip_factorial_recursive(7) == 105
print("PASSED")
