

def make_nested(input_dict):
    final_dict = {}

    for key in input_dict:
        key_split = key.split("_")
        if key_split[0] not in final_dict:
            final_dict[key_split[0]] = {}
        final_dict[key_split[0]][key_split[1]] = input_dict.get(key)

    print(final_dict)
    return final_dict


colors = {
  'animal_bumblebee': ['yellow', 'black'],
  'animal_elephant': ['gray'],
  'animal_fox': ['orange', 'white'],
  'food_apple': ['red', 'green', 'yellow'],
  'food_cheese': ['white', 'orange']
  }

print("Asserting that 'make_nested' works on the input 'colors'")
assert make_nested(colors) == {
  'animal': {
    'bumblebee': ['yellow', 'black'],
    'elephant': ['gray'],
    'fox': ['orange', 'white']
  },
  'food': {
    'apple': ['red', 'green', 'yellow'],
    'cheese': ['white', 'orange']
  }
}, "doesn't work"
print("PASSED")
