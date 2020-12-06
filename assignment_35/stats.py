def function(k):
    return 1 / (k**5)
'''
result = 0
for i in range(25, 10001):
    result += function(i)

print(1 / result)

result = 0
for i in range(25, 31):
    result += function(i)
print(1443199.7832 * result)
'''
result = 0
for i in range(25, 1001):
    result += function(i)
    if result * 1443199.7832 >= 0.95:
        print("k (where loop stopped): " + str(i))
        print("sum: " + str(result))
        print("P(k): " + str(result * 1443199.7832))
        break
