nat2bin2 :: (Integral t,Eq t) => t -> [t]
nat2bin2 0 = [0]
nat2bin2 1 = [1] 
nat2bin2 x 
    | x < 2 = [(mod x 2)]
    | otherwise = (mod x 2): (nat2bin2 (div (x-mod x 2) 2))

nat2bin :: (Integral t, Eq t) => t -> [t]
nat2bin x = reverso (nat2bin2 x)


reverso :: Eq t => [t] -> [t]
reverso [] = []
reverso (x:[]) = [x]
reverso (x:xs) = reverso xs ++ [x]

