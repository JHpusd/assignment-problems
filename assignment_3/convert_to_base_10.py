

def convert_to_base_10(input_binary):
    dec_num = 0
    power = len(str(input_binary)) - 1
    ref_binary = str(input_binary)

    for num in ref_binary:
        assert int(num) == 1 or int(num) == 0, "only 1's and 0's allowed"
        dec_num += int(num) * (2 ** power)
        power -= 1
        if power < 0:
            print(dec_num)
            return dec_num

print("Asserting that 'convert_to_base_10' works on input 10011")
assert convert_to_base_10(10011) == 19, "doesn't work"
print("PASSED")
