sacarBlancosRepe :: [Char] -> [Char]
sacarBlancosRepe [] = []
sacarBlancosRepe (x:[]) = [x]
sacarBlancosRepe (x:y:xs)
    | x == y && x == ' ' = sacarBlancosRepe (y:xs)
    | otherwise = x : (sacarBlancosRepe (y:xs))