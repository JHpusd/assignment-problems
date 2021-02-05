fib 0 = 0
fib 1 = 1
fib n = fib (n-1) + fib (n-2)

sequenceTerms k = [fib(i) | i <- [0..k]]

partialSum k = sum(sequenceTerms k)

metaSumEntries n = [partialSum x | n <- sequenceTerms n]

metaSum n = sum (metaSumEntries n)

main = print(metaSum 6)
