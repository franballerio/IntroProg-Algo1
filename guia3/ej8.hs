-- comparamos si la suma de 
-- los dos ultimos digitos de los numeros que pasamos es mayor o menor

sum_ult2_dig :: Integer -> Integer
sum_ult2_dig x = (mod x 10) + (mod (abs (div x 10)) 10) 

comp :: Integer -> Integer -> Integer
comp x y 
    | ((sum_ult2_dig x) < (sum_ult2_dig y)) = 1
    | ((sum_ult2_dig x) > (sum_ult2_dig y)) = -1
    | ((sum_ult2_dig x) == (sum_ult2_dig y)) = 0

