def cartesian_product(arrays):
    points = [[]]
    for arr in arrays:
        for i in range(len(points)):
            for element in arr:
                temp_point = list(points[0])
                temp_point.append(element)
                points.append(temp_point)
            points.remove(points[0])
    return points
'''
print("Testing function 'cartesian_product'...")
assert cartesian_product([['a'], [1,2,3], ['Y','Z']]) == [
    ['a',1,'Y'], ['a',1,'Z'], ['a',2,'Y'], ['a',2,'Z'], [
        'a',3,'Y'], ['a',3,'Z']]
print("PASSED")
'''
