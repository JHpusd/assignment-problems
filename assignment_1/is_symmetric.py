def is_symmetric(input_string):
    if input_string == input_string[::-1]:
        return True
    else:
        return False

print("asserting is_symmetric works on input 'tacocat'")
assert is_symmetric("tacocat"), "Should be True"
print("PASSED")
print(is_symmetric("tacocat"))

print("\n")

print("asserting is_symmetric works on input 'banana'")
assert not is_symmetric("banana"), "Should be False"
print("PASSED")
print(is_symmetric("banana"))
