-- 1) sumaAcumulada
{- lo que quiere hacer suma acumulada es:
dada una lista de numeros, con posiciones 1,2,..,n
nos devuelva una lista de numeros donde la posicion n
es la suma de las posiciones 1,...,n de la lista anterior
-}
sumaAcumulada :: (Num t,Eq t) => [t] -> [t]
sumaAcumulada [] = []
sumaAcumulada (x:[]) = [x]
sumaAcumulada (x:y:xs) = x : sumaAcumulada ((x+y):xs)


-- 2) split en primos
-- dada un alista de numeros nos pide que los hagamos como mult de primos

esPrimo :: Integer -> Bool
esPrimo 2 = True
esPrimo 3 = True
esPrimo 5 = True
esPrimo 7 = True
esPrimo x 
    | mod x 2 == 0 || mod x 3 == 0 || mod x 5 == 0 || mod x 7 == 0 = False
    | otherwise = True


{-}descomponerEnPrimos :: [Integer] -> [[Integer]] 
descomponerEnPrimos [] = [[]]
descomponerEnPrimos (x:[]) = [descomponer x]
descomponerEnPrimos (x:y:xs) = [descomponer x] : (descomponer y:xs)
-}
descomponer :: Integer -> [Integer]
descomponer x 
    | esPrimo x = [x]
    | otherwise = split x primeNumbers x x

split :: Integer -> [Integer] -> [Integer]
split 1 _ = []
split n (x:xs) 
    | mod n x == 0 = x : (split (div n x) (x:xs))
    | otherwise = split n xs

primeNumbers :: Integer -> Integer -> [Integer]
primeNumbers x y 
    | y == 0 = [0]
    | esPrimo x = [x] ++ primeNumbers (x - 1) (y - 1)
    | otherwise = primeNumbers (x - 1) y
