fibonacci :: Integer -> Integer
fibonacci x 
    | x == 0 = 0
    | x == 1 = 1
    | x > 1 = fibonacci (x-1) + fibonacci (x-2)

    