recommendClothing :: (RealFloat a) => a -> String
recommendClothing degreeCelsius
    | degreeFahrenheit >= 80 = "Wear a shortsleeve shirt"
    | degreeFahrenheit > 65 = "Wear a longsleeve shirt"
    | degreeFahrenheit > 50 = "Wear a sweater"
    | degreeFahrenheit <= 50 = "Wear a jacket"
    where degreeFahrenheit = (degreeCelsius * 9/5) + 32

main = print(recommendClothing 0)