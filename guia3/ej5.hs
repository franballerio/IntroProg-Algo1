g :: Integer -> Integer
g x 
    | mod x 2 == 0  = div x 2
    | otherwise = 3 * x + 1 

f :: Integer -> Integer 
f x 
    | x <= 7 = x ^ 2 
    | x > 7 = 2 * x - 1

todos_menores :: (Integer,Integer,Integer) -> Bool
todos_menores (x,y,z) = f x > g x && f y > g y && f z > g z

