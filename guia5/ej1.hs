-- 1)
longitud :: [t] -> Integer
longitud [] = 0
longitud (x:[]) = 1
longitud (x:xs) = 1 + longitud xs 

-- 2)
ultimo :: [t] -> t
ultimo (x:[]) = x
ultimo (x:xs) = ultimo (xs)

sacarPrimero :: [t] -> [t]
sacarPrimero [] = []
sacarPrimero (x:[]) = []
sacarPrimero (x:xs) = xs

-- 3) la especificacion es poner toda la lista menos el ultimo elemento

principio :: (Eq t) => [t] -> [t]
principio (x:[]) = [x]
principio xs = eliminarElem xs (ultimo xs)


eliminarElem :: (Eq t) => [t] -> t -> [t]
eliminarElem [] y = []
eliminarElem (x:xs) y 
 | x == y = eliminarElem xs y 
 | otherwise = x:(eliminarElem xs y) 


-- 4) 
reverso :: Eq t => [t] -> [t]
reverso [] = []
reverso xs = ultimo xs : (reverso (eliminarElem xs (ultimo xs)))
