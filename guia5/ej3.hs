-- 1)
sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x:[]) = 0
sumatoria (x:xs) = x + sumatoria xs

-- 2) 
productoria :: [Integer] -> Integer
productoria [] = 0
productoria (x:[]) = 1
productoria (x:xs) = x * productoria xs


-- 2) 
maximo :: [Integer] -> Integer
maximo (x:[]) = x
maximo (x:y:xs)
    | x > y = maximo (x:xs)
    | otherwise = maximo (y:xs)

-- 4) 
sumarN :: Integer -> [Integer] -> [Integer]
sumarN _ [] = []
sumarN n (x:[]) = [x+n]
sumarN n (x:xs) = x+n : (sumarN n xs)

-- 5) 
sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero [] = []
sumarElPrimero (x:[]) = [x+x]
sumarElPrimero (x:xs) = sumarN x (x:xs)

-- 6)
sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo [] = []
sumarElUltimo (x:[]) = [x+x]
sumarElUltimo x = sumarN (ultimo x) x

ultimo :: [t] -> t
ultimo (x:[]) = x
ultimo (x:xs) = ultimo (xs)

-- 7) 
pares :: [Integer] -> [Integer]
pares [] = []
pares (x:[]) 
    | mod x 2 == 0 = [x]
    | otherwise = []
pares (x:xs)
    | mod x 2 == 0 = x:(pares xs)
    | otherwise = pares xs

-- 8) 
multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN _ [] = []
multiplosDeN n (x:[]) 
    | mod x n == 0 = [x]
    | otherwise = []
multiplosDeN n (x:xs) 
    | mod x n == 0 = x:(multiplosDeN n xs)
    | otherwise = multiplosDeN n xs

-- 9)
ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar (x:[]) = [x]
ordenar x = menor x :(ordenar (eliminarOnce x (menor x)))


menor :: [Integer] -> Integer
menor (x:[]) = x
menor (x:y:xs)
    | x <= y = menor (x:xs)
    | otherwise = menor (y:xs)

eliminarOnce :: (Eq t) => [t] -> t -> [t]
eliminarOnce [] y = []
eliminarOnce (x:xs) y 
 | x == y = xs 
 | otherwise = x:(eliminarOnce xs y) 