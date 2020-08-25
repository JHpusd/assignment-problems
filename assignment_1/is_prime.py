def is_prime(input_num):
    assert input_num > 1, "Your number is too small"

    for num in range(2, input_num):
        if input_num % num == 0:
            return False

    return True

print("testing if is_prime works on the number 13 ...")
assert is_prime(13), "Should be True"
print("PASSED")
print(is_prime(13))

print("\n")

print("testing if is_prime works on the number 99 ...")
assert not is_prime(99), "Should be False"
print("PASSED")
print(is_prime(99))
