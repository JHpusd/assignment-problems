sumFactorsList n = [factor | factor <- [1..n], n `mod` factor == 0]
sumFactors = sum . sumFactorsList

main = print(sumFactors 10)

