-- vamos con otra sucesion 

-- esta vez esta definida de manera recursiva A1 = 2, An = 2 + 1/(An-1) 

{- raizDe2Aprox :: Int -> Float
raizDe2Aprox 1 = 2
raizDe2Aprox n = 2 + (1 / (raizDe2Aprox n - 1)) -}

raizDe2Aprox :: Int -> Float
raizDe2Aprox 1 = 1
raizDe2Aprox n = roundN ((sqrt 2) n)


roundN :: Float -> Int -> Float
roundN x y
    | x < 10 = x
    | otherwise = x / (10^(y - 1))
