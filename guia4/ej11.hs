-- a) func eAprox que aproxima el valor de e a partir de una sumatoria dada

{- ESPECIFIC
e Aprox :: (x : N) : R {
    requiere {True}
    asegura {la aproximacion del numero e con x decimales}
}
-}

factorial :: Float -> Float
factorial x 
    | x == 0 = 1
    | otherwise = x * factorial (x - 1)



eAprox :: Float -> Float
eAprox n 
    | n == 0 = 1
    | otherwise = (1 / (factorial n)) + eAprox (n - 1)

-- b) definir e como eAprox 10

e :: Float
e = eAprox 10
