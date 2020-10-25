def sort(num_list):
    result_list = []
    while len(num_list) > 0:
        min_value = num_list[0]
        for num in num_list:
            if num < min_value:
                min_value = num
        result_list.append(min_value)
        num_list.remove(min_value)
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
        '''
        if first_half[0] < second_half[0]:
            merged_list.append(first_half[0])
            merged_list.append(second_half[0])
        elif second_half[0] <= first_half[0]:
            merged_list.append(second_half[0])
            merged_list.append(first_half[0])
        '''
        for i in second_half:
            first_half.append(i)
        merged_list = sort(first_half)
        return merged_list
    elif len(first_half) != 1 or len(second_half) != 1:
        sorted_first_half = merge_sort(first_half)
        sorted_second_half = merge_sort(second_half)
        for i in sorted_second_half:
            sorted_first_half.append(i)
        final_merged_list = sort(sorted_first_half)
        return final_merged_list

print("Testing 'merge_sort'...")
assert merge_sort([4,8,7,7,4,2,3,1]) == [1, 2, 3, 4, 4, 7, 7, 8]
print("PASSED")
