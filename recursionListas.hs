-- lista estrictamente decreciente de enteros de 1 a -100

listaDec :: Int -> Int -> [Int] 
listaDec x y 
    | x < y = []
    | otherwise = x : listaDec (x - 1) y

listaCrec :: Int -> Int -> [Int] 
listaCrec x y 
    | x > y = []
    | mod x 4 == 1 = x : listaCrec (x + 1) y
    | otherwise = listaCrec (x + 1) y


long :: [a] -> Int
long [] = 0
long (_:xs) = 1 + long xs

sumatoria :: [Float] -> Float
sumatoria [] = 0
sumatoria (x:xs) = sumatoria xs + x

{- lo que hace esta parte de la funcion (_:xs) o (x:xs) es buscar el head,
en el caso de _ solo lo ve y en el caso de x la x toma ese valor
y la recursion que es sumatoria xs o long xs lo que hacen es llamar denuevo a la 
funcion pero con lo que queda de la lista, y asi sucesivamente -}

pertenece :: (Eq a) => a -> [a] -> Bool
pertenece _ [] = False
pertenece y (x:xs) = x == y || pertenece y xs
