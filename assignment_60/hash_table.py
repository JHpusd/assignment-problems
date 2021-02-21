def hash_function(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result_sum = 0
    for char in string:
        result_sum += alphabet.index(char)
    return result_sum % 5

def insert(arr, key, val):
    arr[hash_function(key)].append((key, val))

def find(arr, key):
    for pair in arr[hash_function(key)]:
        if pair[0] == key:
            return pair[1]
    return False

arr = [[], [], [], [], []]

alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i, char in enumerate(alphabet):
    key = 'someletters'+char
    value = [i, i**2, i**3]
    insert(arr, key, value)

for i, char in enumerate(alphabet):
    key = 'someletters'+char
    output_value = find(arr, key)
    desired_value = [i, i**2, i**3]
    assert output_value == desired_value

