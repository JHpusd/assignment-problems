def diags(arr):
    diag_1 = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i == j:
                diag_1.append(arr[i][j])
    diag_2 = []
    j = len(arr[0]) - 1
    for i in range(len(arr)):
        diag_2.append(arr[i][j])
        j -= 1
    return [diag_1, diag_2]

def rows(arr):
    return arr

def cols(arr):
    col_list = []
    for j in range(len(arr[0])):
        col = [arr[i][j] for i in range(len(arr))]
        col_list.append(col)
    return col_list

def is_valid(arr):
    for diag in diags(arr):
        if None in diag:
            continue
        if sum(diag) != 15:
            return False
    for row in rows(arr):
        if None in row:
            continue
        if sum(row) != 15:
            return False
    for col in cols(arr):
        if None in col:
            continue
        if sum(col) != 15:
            return False
    return True

def all_elem(arr):
    result = [arr[i][j] for j in range(len(arr[0])) for i in range(len(arr))]
    return result
'''
arr1 = [[1,2,None],[None,3,None],[None,None,None]]
assert is_valid(arr1)

arr2 = [[1,2,None],[None,3,None],[None,None,4]] 
assert not is_valid(arr2)

arr3 = [[1,2,None],[None,3,None],[5,6,4]]
assert not is_valid(arr3)

arr4 = [[None,None,None],[None,3,None],[5,6,4]] 
assert is_valid(arr4)
'''

arr = [[None,None,None],[None,None,None],[None,None,None]]
for num1 in range(1,10):
    if None not in all_elem(arr) and is_valid(arr):
        break
    arr = [[num1,None,None],[None,None,None],[None,None,None]]
    if not is_valid(arr):
        continue
    for num2 in range(1,10):
        if None not in all_elem(arr) and is_valid(arr):
            break
        if num2 not in [num1]:
            arr = [[num1,num2,None],[None,None,None],[None,None,None]]
        else:
            continue
        if not is_valid(arr):
            continue
        for num3 in range(1,10):
            if None not in all_elem(arr) and is_valid(arr):
                break
            if num3 not in [num1,num2]:
                arr = [[num1,num2,num3],[None,None,None],[None,None,None]]
            else:
                continue
            if not is_valid(arr):
                continue
            for num4 in range(1,10):
                if None not in all_elem(arr) and is_valid(arr):
                    break
                if num4 not in [num1,num2,num3]:
                    arr = [[num1,num2,num3],[num4,None,None],[None,None,None]]
                else:
                    continue
                if not is_valid(arr):
                    continue
                for num5 in range(1,10):
                    if None not in all_elem(arr) and is_valid(arr):
                        break
                    if num5 not in [num1,num2,num3,num4]:
                        arr = [[num1,num2,num3],[num4,num5,None],[None,None,None]]
                    else:
                        continue
                    if not is_valid(arr):
                        continue
                    for num6 in range(1,10):
                        if None not in all_elem(arr) and is_valid(arr):
                            break
                        if num6 not in [num1,num2,num3,num4,num5]:
                            arr = [[num1,num2,num3],[num4,num5,num6],[None,None,None]]
                        else:
                            continue
                        if not is_valid(arr):
                            continue
                        for num7 in range(1,10):
                            if None not in all_elem(arr) and is_valid(arr):
                                break
                            if num7 not in [num1,num2,num3,num4,num5,num6]:
                                arr = [[num1,num2,num3],[num4,num5,num6],[num7,None,None]]
                            else:
                                continue
                            if not is_valid(arr):
                                continue
                            for num8 in range(1,10):
                                if None not in all_elem(arr) and is_valid(arr):
                                    break
                                if num8 not in [num1,num2,num3,num4,num5,num6,num7]:
                                    arr = [[num1,num2,num3],[num4,num5,num6],[num7,num8,None]]
                                else:
                                    continue
                                if not is_valid(arr):
                                    continue
                                for num9 in range(1,10):
                                    if None not in all_elem(arr) and is_valid(arr):
                                        break
                                    if num9 not in [num1,num2,num3,num4,num5,num6,num7,num8]:
                                        arr = [[num1,num2,num3],[num4,num5,num6],[num7,num8,num9]]
                                    else:
                                        continue
                                    if not is_valid(arr):
                                        continue
print(arr)

