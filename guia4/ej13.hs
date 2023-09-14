-- es una sumatoria de otra sumatoria, y como lo planteamos creo que tomamos todos los casos
f2 :: Int -> Int -> Int
f2 x y
    | y == 1 = x
    | otherwise = x^y + f2 x (y - 1)

f3 :: Int -> Int -> Int
f3 x y
    | x == 0 = 0
    | otherwise = f2 x y + f3 (x - 1) y

