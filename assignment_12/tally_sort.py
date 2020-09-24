def min_value(num_list):
    smallest = num_list[0]
    for num in num_list:
        if num < smallest:
            smallest = num
    return smallest


def max_value(num_list):
    largest = num_list[0]
    for num in num_list:
        if num > largest:
            largest = num
    return largest


def tally_sort(num_list):
    smallest = min_value(num_list)
    for n in range(len(num_list)):
        num_list[n] -= smallest

    tally_list = []
    for n in range(max_value(num_list) + 1):
        tally_list.append(0)

    for num in num_list:
        tally_list[num] += 1

    result_list = []
    for n in range(len(tally_list)):
        for _ in range(tally_list[n]):
            result_list.append(n)

    for n in range(len(result_list)):
        result_list[n] += smallest
    return result_list

print("Asserting that 'tally_sort' works...")
assert tally_sort([2, 5, 2, 3, 8, 6, 3]) == [2, 2, 3, 3, 5, 6, 8]
print("PASSED")
