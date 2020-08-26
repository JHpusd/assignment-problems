def flatten(input_dict):
    final_dict = {}

    for dict_name in input_dict:
        for key in colors[dict_name]:
            final_dict[dict_name + "_" + key] = input_dict[dict_name][key]

    print(final_dict)
    return final_dict

colors = {
  'animal': {
    'bumblebee': ['yellow', 'black'],
    'elephant': ['gray'],
    'fox': ['orange', 'white']
  },
  'food': {
    'apple': ['red', 'green', 'yellow'],
    'cheese': ['white', 'orange']
  }
}

print("Asserting that 'flatten' works on 'colors'...")
assert flatten(colors) == {
  'animal_bumblebee': ['yellow', 'black'],
  'animal_elephant': ['gray'],
  'animal_fox': ['orange', 'white'],
  'food_apple': ['red', 'green', 'yellow'],
  'food_cheese': ['white', 'orange']
}, "didn't work"
print("PASSED")
