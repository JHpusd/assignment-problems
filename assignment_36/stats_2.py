def f(k):
    return 1 / (k**4)

result = 0
for i in range(68,1001):
    result += f(i)

c = 1 / result

result = 0
for i in range(68,1001):
    result += f(i)
    if result * c >= 0.95:
        print("k (where loop stopped): " + str(i))
        print("sum: " + str(result))
        print("P(k): " + str(result * c))
        break
