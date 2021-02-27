getScore n
    | n == "A" = 4
    | n == "B" = 3
    | n == "C" = 2
    | n == "D" = 1
    | n == "F" = 0

gradeScores m = map (getScore) (m)

calcGpa i = fromIntegral (sum(gradeScores i)) / fromIntegral (length i)

main = print(calcGpa ["A", "B", "B", "C", "C", "C", "D", "F"])