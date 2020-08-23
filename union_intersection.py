

def intersection(list_1, list_2):
    intersection_set = set.intersection(set(list_1), set(list_2))
    intersection_list = list(intersection_set)

    print(intersection_list)
    return intersection_list

print('''Asserting that 'intersection' works on
[1, 2, 'a', 'b'] and [2, 3, 'a'] ...''')
assert intersection([1, 2, "a", "b"], [2, 3, "a"])
print("PASSED")

print("\n")


def union(list_1, list_2):
    union_set = set.union(set(list_1), set(list_2))
    union_list = list(union_set)

    print(union_list)
    return union_list

print("Asserting that 'union' works on [1, 2, 'a', 'b'] and [2, 3, 'a'] ...")
assert union([1, 2, "a", "b"], [2, 3, "a"])
print("PASSED")