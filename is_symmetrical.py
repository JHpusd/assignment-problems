def is_symmetric(input_string):
  if input_string == input_string[::-1]:
    return True
  else:
    return False

print("tacocat: ")
print(is_symmetric("tacocat"))
print("testing is_symmetric on input 'tacocat'")
assert is_symmetric("tacocat") == True, "Should be True"
print("PASSED")

print("banana: ") 
print(is_symmetric("banana"))
print("testing is_symmetric on input 'banana'")
assert is_symmetric("banana") == False, "Should be False"
print("PASSED")
