def convert_to_numbers(input_string):

  alph_list = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

  input_list = list(input_string)
  new_list = []
  for char in input_list:
    new_list.append(alph_list.index(char))
  
  print(new_list)

convert_to_numbers("hello")