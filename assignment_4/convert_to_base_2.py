import math


def convert_to_base_2(input_dec):
    number = input_dec
    result_list = []

    terms = math.floor(math.log(input_dec, 2)) + 1
    for i in range(0, terms):
        result_list.append(0)

    while number >= 1:
        replace_term = -math.floor(math.log(number, 2))
        number -= 2 ** math.floor(math.log(number, 2))
        result_list[replace_term] = 1

    result_string = ""
    for num in result_list[::-1]:
        result_string += str(num)
        result_integer = int(result_string)

    print(result_integer)
    return result_integer

print("Asserting that 'convert_to_base_2' works on input 19...")
assert convert_to_base_2(19) == 10011, "didn't work"
print("PASSED")
