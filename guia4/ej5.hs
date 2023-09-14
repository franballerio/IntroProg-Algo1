-- buscamos el factorial pero de 2 en 2
-- ej medioFac 10 = 10*8*6*4*2

medioFac :: Integer -> Integer
medioFac x 
    | x == 0 = 1
    | x == 1 = 1
    | otherwise = x * medioFac (x-2)
