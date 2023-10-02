-- 1) 
sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos (x:[]) = [x]
sacarBlancosRepetidos (x:y:xs) 
    | x == ' ' && y == ' ' = sacarBlancosRepetidos (y:xs)
    | otherwise = x :(sacarBlancosRepetidos (y:xs))

-- 2) 
contarPalabras :: [Char] -> Integer
contarPalabras [] = 0
contarPalabras (x:y:xs) = contarPalabrasAux(sacarBlancosRepetidos (x:y:xs))

contarPalabrasAux :: [Char] -> Integer
contarPalabrasAux [] = 0
contarPalabrasAux (x:[]) = 1
contarPalabrasAux (x:y:xs) 
    | x == ' ' = 1+ contarPalabrasAux xs
    | otherwise = contarPalabrasAux (y:xs)


-- 3) 
palabras :: [Char] -> [[Char]]
palabras x = palabrasAux x []

palabrasAux :: [Char] -> [Char] -> [[Char]]
palabrasAux [] y = [y]
palabrasAux (x:xs) y 
    | x /= ' ' = (palabrasAux xs (y ++ [x]))
    | x == ' ' = [y] ++ (palabrasAux xs [])


palabrasCulo :: [Char] -> [[Char]]
palabrasCulo x = palabrasAux x ['a']


{- esta funcion lo que hace es separar la primer lista de Char que le pasamos y hace 
una lista con palabras. Por cada caracter que lee lo mete en una lista
y si el caracter es ' ' agarra la lista que creo antes y se la suma a una nueva
donde estara la nueva palabra -}


-- 4) 
palabraMasLarga :: [Char] -> [Char] 
palabraMasLarga [] = []
palabraMasLarga (x:[]) = []
palabraMasLarga (x:xs) = palabraMasLarga2 (palabras (x:xs)) 

palabraMasLarga2 :: Eq t => [[t]] -> [t]
palabraMasLarga2 [] = []
palabraMasLarga2 (x:[]) = x
palabraMasLarga2 (x:y:[])
    | length x > length y = x
    | otherwise = y
palabraMasLarga2 (x:y:xs)
    | length x > length y = palabraMasLarga2 (x:xs)
    | otherwise = palabraMasLarga2 (y:xs)


-- 5) 
aplanar :: [[Char]] -> [Char]
aplanar [] = []
aplanar [x] = x
aplanar (x:xs) = x ++ aplanar xs

{-} lo que queremos hacer es agarrar una lista con listas de Char 
[[caca], [culo], [pis]] 
y en base a esta lista queremos hacer otra lista pero con las palabras sueltas
"caca culo pis" -}

-- 6) 
aplanarConBlancos :: [[Char]] -> [Char]
aplanarConBlancos [] = []
aplanarConBlancos [x] = x
aplanarConBlancos (x:xs) = x ++ " " ++ aplanarConBlancos xs
-- para recordar [[Char]] = ["Hola", "Chau", "Maniana"]

-- 7) 
aplanarConNBlancos :: Integer -> [[Char]] -> [Char]
aplanarConNBlancos _ [] = []
aplanarConNBlancos _ [x] = x
aplanarConNBlancos n (x:xs) = x ++ nSpaces n ++ aplanarConNBlancos n xs

nSpaces :: Integer -> [Char]
nSpaces 0 = []
nSpaces n = [' '] ++ nSpaces (n - 1)


