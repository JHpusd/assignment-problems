

def count_characters(input_string):
    input_string = input_string.lower()
    input_list = list(input_string)
    user_dict = {}

    for char in input_list:
        user_dict[char] = input_list.count(char)

    print(user_dict)
    return user_dict

print("Asserting that 'count_characters' works on 'A Catl!!!' ...")
assert count_characters("A Cat!!!") == {
    'a': 2, ' ': 1, 'c': 1, 't': 1, '!': 3}, "doesn't work"
print("PASSED")
