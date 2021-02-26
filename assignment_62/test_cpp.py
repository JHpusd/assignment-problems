def calcsum(m,n):
    ascend = []
    a_counter = 1
    for i in range(m):
        ascend.append([])
        for j in range(n):
            ascend[i].append(counter)
            counter += 1
    descend = []
    d_counter = m*n
    for i in range(n):
        descend.append([])
        for j in range(m):
            descend[i].append(counter)
            counter -= 1
    return (ascend, descend)

print(calcsum(2,3))