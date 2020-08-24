

def first_n_terms(n):
    return_list = []

    for int in range(1, n):
        if int == 1:
            previous = 5
            return_list.append(5)
        return_list.append(3*previous - 4)
        previous = 3*previous - 4
    
    print(return_list)
    return return_list

print("Asserting that first_n_terms works on input n = 10 ...")
assert first_n_terms(10) == [
    5, 11, 29, 83, 245, 731, 
    2189, 6563, 19685, 59051], "didn't work"
print("PASSED")

