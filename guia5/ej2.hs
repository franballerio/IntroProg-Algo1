-- 1)
pertenece :: Eq t => t -> [t] -> Bool
pertenece _ [] = False
pertenece y (x:[]) | y == x = True
                   | otherwise = False
pertenece y (x:xs)  | y == x = True
                    | otherwise = pertenece y xs


-- 2)
todosIg :: Eq t => [t] -> Bool
todosIg [] = True
todosIg (x:[]) = True
todosIg (x:y:xs) | x == y = todosIg (y:xs) 
                 | otherwise = False

-- 3)
todosDis :: Eq t => [t] -> Bool
todosDis [] = True
todosDis (x:[]) = True
todosDis (x:xs) | pertenece x xs = False
                | otherwise = todosDis xs 

-- 4) 
hayRepes :: Eq t => [t] -> Bool
hayRepes [] = False
hayRepes (x:[]) = False
hayRepes (x:xs) | pertenece x xs = True
                | otherwise = hayRepes xs 


-- 5) 
quitar :: Eq t => [t] -> t -> [t]
quitar [] _ = []
quitar (x:[]) y 
 | y == x = []
 | otherwise = [x] 
quitar (x:xs) y
 | pertenece y (x:xs) = eliminarOnce (x:xs) y
 | x == y = eliminarOnce (x:xs) y
 | otherwise = (x:xs)

eliminarOnce :: (Eq t) => [t] -> t -> [t]
eliminarOnce [] y = []
eliminarOnce (x:xs) y 
 | x == y = xs 
 | otherwise = x:(eliminarOnce xs y) 

 -- 6) 
quitarTodos :: (Eq t) => [t] -> t -> [t]
quitarTodos [] y = []
quitarTodos (x:xs) y 
 | x == y = quitarTodos xs y 
 | otherwise = x:(quitarTodos xs y) 

-- 7) 
eliminarRepetidos :: Eq t => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x:[]) = [x]
eliminarRepetidos (x:xs) 
 | elem x xs = eliminarRepetidos xs
 | otherwise = x:(eliminarRepetidos xs) 


-- 8) 
mismosElementos :: Eq t => [t] -> [t] -> Bool
mismosElementos [] [] = True
mismosElementos (x:[]) [] = False
mismosElementos [] (y:[]) = False
mismosElementos (x:xs) [] = False
mismosElementos [] (y:ys) = False
mismosElementos (x:[]) (y:[]) 
 | x == y = True
 | otherwise = False
mismosElementos (x:xs) (y:[]) = False
mismosElementos (x:[]) (y:ys) = False
mismosElementos (x:xs) (y:ys)
 | x == y = mismosElementos xs ys
 | otherwise = False

capicua :: Eq t => [t] -> Bool
capicua x = x == reverso x

reverso :: Eq t => [t] -> [t]
reverso [] = []
reverso (x:[]) = [x]
reverso (x:xs) = reverso xs ++ [x]

ultimo :: [t] -> t
ultimo (x:[]) = x
ultimo (x:xs) = ultimo (xs)

eliminarElem :: (Eq t) => [t] -> t -> [t]
eliminarElem [] y = []
eliminarElem (x:xs) y 
 | x == y = eliminarElem xs y 
 | otherwise = x:(eliminarElem xs y) 

