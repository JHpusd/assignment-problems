merge (x:xs) (y:ys)
    | x<y = x:(merge xs (y:ys))
    | y<=x = y:(merge ys (x:xs))
merge [] y = y
merge x [] = x

main = print(merge [1,2,5,8] [3,4,6,7,10])