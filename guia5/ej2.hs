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