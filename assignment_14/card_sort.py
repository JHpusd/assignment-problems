def card_sort(num_list):
    sorted_list = []
    for num in num_list:
        if len(sorted_list) == 0:
            sorted_list.append(num)
            continue
        for i in range(len(sorted_list)):
            if num > sorted_list[i]:
                if i == len(sorted_list) - 1:
                    sorted_list.append(num)
                    break
                continue
            elif num <= sorted_list[i]:
                if i == 0:
                    sorted_list.insert(0, num)
                    break
                sorted_list.insert(i, num)
                break
    return sorted_list

print("Testing function 'card_sort'...")
assert card_sort([12, 11, 13, 5, 6]) == [5, 6, 11, 12, 13]
assert card_sort([5, 7, 3, 5, 1, 3, -1, 1, -3, -1, -3, -1]) == [
    -3, -3, -1, -1, -1, 1, 1, 3, 3, 5, 5, 7]
print("PASSED")
