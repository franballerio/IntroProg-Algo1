-- vamos a ver si todos los digitos de un numero son iguales
ult_dig :: Integer -> Integer
ult_dig x = mod x 10

del_ult :: Integer -> Integer
del_ult x = div x 10

tDI :: Integer -> Bool
tDI x
    | x < 10 = True
    | otherwise = (ult_dig x == ult_dig (del_ult x) && tDI (del_ult x))

