findSmallestPositive :: (Num a, Ord a) => [a] -> a
findSmallestPositive [] = error "empty list"
findSmallestPositive [x] = x
findSmallestPositive (x:xs)
    | (0 < x) && (x < minimum) = x
    | (0 < minimum) && (minimum <= x) = minimum
    | (0 > minimum) && (0 < x) = x
    | (0 > x) && (0 < minimum) = minimum
    | otherwise = x
    where minimum = findSmallestPositive xs

main = print(findSmallestPositive [8, 3, -1, 2, -5, 7])