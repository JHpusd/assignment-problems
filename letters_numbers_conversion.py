alph_list = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def letters_to_numbers(input_string):

    input_list = list(input_string)
    new_list = []

    for char in input_list:
        new_list.append(alph_list.index(char))

    return new_list

print("banana bread turns into:")
print(letters_to_numbers("banana bread"))

print("asserting letters_to_numbers works on 'banana bread' ...")
assert letters_to_numbers("banana bread") == [2, 1, 14, 1, 14, 1, 0, 2, 18, 5, 1, 4], "Wrong, wrong, wrong, try again"
print("PASSED")

print("\n")
def numbers_to_letters(input_list):

    new_string = ""

    for num in input_list:
        new_string += alph_list[num]

    return new_string

print("[13, 18, 0, 19, 11, 25, 3, 1, 11] turns into:")
print(numbers_to_letters([13, 18, 0, 19, 11, 25, 3, 1, 11]))

print("asserting numbers_to_letters works on [13, 18, 0, 19, 11, 25, 3, 1, 11] ...")
assert numbers_to_letters([13, 18, 0, 19, 11, 25, 3, 1, 11]) == "mr skycak", "Incorrect again. God, how many times do we have to do this."
print("PASSED")
