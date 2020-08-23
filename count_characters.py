

def count_characters(input_string):
    input_string = input_string.lower()
    input_list = list(input_string)
    user_dict = {}

    for char in input_list:
        user_dict[char] = input_list.count(char)

    print(user_dict)
    return user_dict

print("Asserting that 'count_characters' works on 'Electric Eel!!!' ...")
assert count_characters("Electric Eel!!!") == {
    'e': 4, 'l': 2, 'c': 2, 't': 1, 
    'r': 1, 'i': 1, ' ': 1, '!': 3}, "doesn't work"
print("PASSED")
