
user_input = input("")
reverse_string = user_input[::-1]

def is_symmetric(input_string):
  if reverse_string == input_string:
    print("{} is a palindrome".format(input_string))
  else:
    print("{} is not a palindrome".format(input_string))

is_symmetric(user_input)

print("testing is_symmetric on input '{}' ...".format(user_input))
assert user_input == reverse_string, "{} is not a palindrome".format(user_input)
print("PASSED")
