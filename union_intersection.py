

def intersection(list_1, list_2):
    intersection = list(set(list_1) & set(list_2))

    print(intersection)
    return intersection

print('''Asserting that 'intersection' works on
[1, 2, 'a', 'b'] and [2, 3, 'a'] ...''')
assert intersection([1, 2, "a", "b"], [2, 3, "a"])
print("PASSED")

print("\n")


def union(list_1, list_2):
    union = list(set(list_1) | set(list_2))

    print(union)
    return union

print("Asserting that 'union' works on [1, 2, 'a', 'b'] and [2, 3, 'a'] ...")
assert union([1, 2, "a", "b"], [2, 3, "a"])
print("PASSED")
