-- sumamos los digitos de un numero x

del_ult :: Integer -> Integer
del_ult x = div x 10

ult_dig :: Integer -> Integer
ult_dig x = mod x 10

sumDig :: Integer -> Integer 
sumDig x 
    | x < 10 = x
    | otherwise = ult_dig x + sumDig (del_ult x)