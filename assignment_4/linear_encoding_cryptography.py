alph_letters = " abcdefghijklmnopqrstuvwxyz"


def encode(string, a, b):
    temp_list = []

    for char in string:
        temp_list.append(alph_letters.index(char))

    result_list = []
    for num in temp_list:
        result_list.append((a*num) + b)

    return result_list

print("Asserting that 'encode' works on input ('a cat', 2, 3)...")
assert encode("a cat", 2, 3) == [5, 3, 9, 5, 43], "didn't work"
print("PASSED")
print("\n")


def decode(numbers, a, b):
    temp_list = []

    for num in numbers:
        if (num - b)/a < 0:
            print(False)  # turn this into a comment when doing part c
            return False
        if int((num - b)/a) != (num - b)/a:
            print(False)  # this one too
            return False
        temp_list.append(int((num - b)/a))

    result_string = ""
    for num in temp_list:
        result_string += alph_letters[num]

    return result_string

print("Asserting that 'decode' works...")
assert decode([5, 3, 9, 5, 43], 2, 3) == 'a cat', "didn't work"
assert not decode([1, 3, 9, 5, 43], 2, 3), "didn't work"
assert not decode([5, 3, 9, 5, 44], 2, 3), "didn't work"
print("ALL PASSED")
print("\n")


# Decoding the message:

decode_message = [
    377, 717, 71, 513, 105, 921, 581, 547, 547,
    105, 377, 717, 241, 71, 105, 547, 71, 377,
    547, 717, 751, 683, 785, 513, 241, 547, 751]

for n in range(0, 101):
    for m in range(0, 101):
        if n == 0:
            continue
        try:
            if decode(decode_message, n, m) is not False:
                print(n)
                print(m)
                print(decode(decode_message, n, m))
        except:
            pass

# a=34 and b=71 is the magical combination
