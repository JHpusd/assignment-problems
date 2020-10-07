
def count_compression(string):
    current_term = string[0]
    new_list = []
    for char in string:
        if char != current_term:
            current_term = char
            new_list.append(" ")
            new_list.append(char)
        else:
            new_list.append(char)
    splitting_string = ""
    for element in new_list:
        splitting_string += element
    split_list = splitting_string.split(" ")
    tuples_list = []
    for group in split_list:
        tuples_list.append((group[0], len(group)))
    return tuples_list

print("Testing 'count_compression'...")
assert count_compression('aaabbcaaaa') == [
    ('a', 3), ('b', 2), ('c', 1), ('a', 4)]
assert count_compression('22344444') == [
    ('2', 2), ('3', 1), ('4', 5)]
print("PASSED")


def count_decompression(compressed_string):
    result_string = ""
    for pair in compressed_string:
        for _ in range(pair[1]):
            result_string += pair[0]
    return result_string

print("Testing 'count_decompression'...")
assert count_decompression(
    [('a', 3), ('b', 2), ('c', 1), ('a', 4)]) == 'aaabbcaaaa'
assert count_decompression([
    ('2', 2), ('3', 1), ('4', 5)]) == '22344444'
print("PASSED")
