

def count_characters(input_string):
    input_string = input_string.lower()
    input_list = list(input_string)
    user_dict = {}

    for char in input_list:
        user_dict[char] = input_list.count(char)

    print(user_dict)
    return user_dict

print("Asserting that 'count_characters' works on '5 White Cats!!!' ...")
assert count_characters("5 White Cats!!!") == {
    '5': 1, ' ': 2, 'w': 1, 'h': 1, 'i': 1, 't': 2,
    'e': 1, 'c': 1, 'a': 1, 's': 1, '!': 3}, "doesn't work"
print("PASSED")
