def simple_sort(num_list):
    result_list = []
    while len(num_list) > 0:
        min_value = num_list[0]
        for num in num_list:
            if num < min_value:
                min_value = num
        result_list.append(min_value)
        num_list.remove(min_value)
    return result_list

print("Asserting that 'simple_sort' works...")
assert simple_sort([
    5, 8, 2, 2, 4, 3, 0, 2, -5, 3.14, 2]) == [
        -5, 0, 2, 2, 2, 2, 3, 3.14, 4, 5, 8]
print("PASSED")
print("\n")


def swap_sort(num_list):
    for n in num_list:
        for i in range(0, len(num_list) - 1):
            current_term = num_list[i]
            next_term = num_list[i + 1]
            if current_term > next_term:
                num_list[i] = next_term
                num_list[i + 1] = current_term
    return num_list

print("Asserting that 'swap_sort' works...")
assert swap_sort([
    5, 8, 2, 2, 4, 3, 0, 2, -5, 3.14, 2]) == [
        -5, 0, 2, 2, 2, 2, 3, 3.14, 4, 5, 8]
print("PASSED")
