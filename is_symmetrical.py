def is_symmetric(input_string):
  reverse_string = input_string[::-1]
  if reverse_string == input_string:
    return True
  else:
    return False

print("racecar: ")
print(is_symmetric("racecar"))
print("testing is_symmetric on input 'racecar'")
assert is_symmetric("racecar") == True, "Should be True"
print("PASSED")

print("batman: ") 
print(is_symmetric("batman"))
print("testing is_symmetric on input 'batman'")
assert is_symmetric("batman") == False, "Should be False"
print("PASSED")
