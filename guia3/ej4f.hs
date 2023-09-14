pos_primer_par :: (Integer,Integer,Integer) -> Integer
pos_primer_par (x,y,z) 
    | es_par x == True = 1
    | es_par y == True = 2
    | es_par z == True = 3 
    | otherwise = 4


es_par :: Integer -> Bool
es_par x = mod x 2 == 0
