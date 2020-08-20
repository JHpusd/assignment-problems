alph_list = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def convert_to_numbers(input_string):

    input_list = list(input_string)
    new_list = []

    for char in input_list:
        new_list.append(alph_list.index(char))

    return new_list

print(convert_to_numbers("mr skycak"))

print("asserting convert_to_numbers works on 'mr skycak'")
assert convert_to_numbers("mr skycak") == [13, 18, 0, 19, 11, 25, 3, 1, 11], "Wrong, wrong, wrong, try again"
print("PASSED")


