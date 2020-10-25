def sort(x, y):
    result_list = []
    while True:
        if len(x) == 0 or len(y) == 0:
            for term in x:
                result_list.append(term)
            for term in y:
                result_list.append(term)
            break
        x_term = x[0]
        y_term = y[0]
        if x_term < y_term:
            result_list.append(x_term)
            x.pop(0)
        elif y_term <= x_term:
            result_list.append(y_term)
            y.pop(0)
    return result_list


def merge_sort(input_list):
    first_half = []
    second_half = []
    for i in range(int(len(input_list) / 2)):
        first_half.append(input_list[i])
        input_list.pop(i)
    for j in input_list:
        second_half.append(j)
    if len(first_half) == 1 or len(second_half) == 1:
        return sort(first_half, second_half)
    elif len(first_half) != 1 or len(second_half) != 1:
        sorted_first_half = merge_sort(first_half)
        sorted_second_half = merge_sort(second_half)
        return sort(sorted_first_half, sorted_second_half)

print("Testing 'merge_sort'...")
assert merge_sort([4,8,7,7,4,2,3,1]) == [1, 2, 3, 4, 4, 7, 7, 8]
print("PASSED")
