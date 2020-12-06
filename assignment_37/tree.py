def get_children(target, tree):
    result_list = []
    for branch in tree:
        if branch[0] == target:
            result_list.append(branch[1])
    return result_list

def get_parents(target, tree):
    result_list = []
    for branch in tree:
        if branch[1] == target:
            result_list.append(branch[0])
    return result_list

def get_root(tree):
    for branch in tree:
        if get_parents(branch[0], tree) == []:
            return list(branch[0])
        else:
            continue

edges = [('a','c'), ('e','g'), ('e','i'), ('e','a'), ('d','b'), ('a','d'), ('d','f'), ('f','h'), ('d','j'), ('d','k')]

print("Testing tree methods...")
assert get_children('e', edges) == ['g', 'i', 'a']
assert get_children('c', edges) == []
assert get_children('f', edges) == ['h']
assert get_parents('e', edges) == []
assert get_parents('c', edges) == ['a']
assert get_parents('f', edges) == ['d']
assert get_root(edges) == ['e']
print("PASSED")
