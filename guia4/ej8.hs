-- funcion iesimo, que nos da segun un x e i el valor que tiene x en la posicion i

cantDig :: Integer -> Integer
cantDig x
    | x < 10 = 1
    | otherwise = 1 + cantDig (del_ult x)

del_ult :: Integer -> Integer
del_ult x = div x 10


iesimo :: Integer -> Integer -> Integer 
iesimo x i
    | x == 0 = 1
    | i == cantDig x = ultDig x
    | otherwise = iesimo (sacarUlt x) i 
    where sacarUlt n = div n 10
          ultDig n = mod n 10

-- basicamente lo que hace es recursivamente cortar el numero hasta que i sea igual a
-- el largo del numero, entonces asi el iesimo digito sera el ultimo
-- brilliant

