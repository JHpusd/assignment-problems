def merge(x, y):
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

print("Testing 'merge'...")
assert merge([-2,1,4,4,4,5,7],[-1,6,6]) == [
    -2, -1, 1, 4, 4, 4, 5, 6, 6, 7]
print("PASSED")
