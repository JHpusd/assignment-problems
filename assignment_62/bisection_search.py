def bisection_search(entry, sorted_list):
    low = 0
    high = len(sorted_list) - 1
    while True:
        midpoint = int(round((low+high)/2, 0))
        if sorted_list[midpoint] == entry:
            return midpoint
        if sorted_list[midpoint] < entry:
            low = midpoint + 1
            continue
        if sorted_list[midpoint] > entry:
            high = midpoint - 1
            continue

assert bisection_search(14, [2, 3, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16]) == 9

# the most amount of iterations it would take to find an element in an array of 16 elements would be 4 (split into 8, then 4, then 2, then there is 1 left)

