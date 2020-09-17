def unlist_nonrecursive(x):
    while True:
        try:
            for i in x:
                if list(i) != i:
                    return x
            x = i
        except:
            if len(x) == 1:
                return x[0]
            else:
                return x

print("Asserting that 'unlist_nonrecursive' works...")
assert unlist_nonrecursive([[[[1], [2,3], 4]]]) == [[1], [2,3], 4]
assert unlist_nonrecursive([[[[1]]]]) == 1
print("PASSED")

def unlist_recursive(x):
    try:
        for i in x:
            if list(i) != i:
                return x
        return unlist_recursive(i)
    except:
        if len(x) == 1:
            return x[0]
        else:
            return x

print("Asserting that 'unlist_recursive' works...")
assert unlist_recursive([[[[1], [2,3], 4]]]) == [[1], [2,3], 4]
assert unlist_recursive([[[[1]]]]) == 1
print("PASSED")