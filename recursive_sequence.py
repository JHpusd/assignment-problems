

def first_n_terms(n):
    assert n > 0, "Number needs to be greater than zero"
    return_list = []

    for intg in range(1, n):
        if intg == 1:
            previous = 5
            return_list.append(5)
        return_list.append(3*previous - 4)
        previous = 3*previous - 4

    print(return_list)
    return return_list

print("Asserting that first_n_terms works on input n = 10 ...")
assert first_n_terms(10) == [
    5, 11, 29, 83, 245, 731,
    2189, 6563, 19685, 59051], "didn't work"
print("PASSED")

print("\n")


def nth_term(n):
    if n == 1:
        return 5
    return 3*nth_term(n-1) - 4

print("Asserting that nth_term works on the input n = 10")
assert nth_term(10) == 59051, "doesn't work"
print(nth_term(10))
print("PASSED")
