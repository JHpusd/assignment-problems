alph_list = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def number_to_letter(input_list):
    
    new_string = ""

    for num in input_list:
        new_string += alph_list[num]

    print(new_string)
    return new_string

number_to_letter([0, 1, 2, 3])