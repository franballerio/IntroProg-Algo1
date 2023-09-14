-- especificamos las sig funciones, pensamos el algo y codeamos

{- 1. sumatoria de 2i, desde i=0 hasta n, con n natural mas el cero

especific
f1 (n : Natural) : Natural {
    requiere {numero natural o cero}
    asegura {res = sumatoria de potencias 2i}
}


2. algoritmo 
buscamos hacer una sumatoria asiq posiblemente usemos recursion
yo creo q seria algo asi

f1 n
si n == 0 = 1
sino = 2^n + f^(n - 1)
-}

f1 :: Integer -> Integer
f1 x
    | x == 0 = 1
    | otherwise = 2^x + f1 (x- 1)

{- f2 es igual que f1 solo que cambiamos el 2 por un argumento 
y ese argumento es un numero real
-}

f2 :: Integer -> Float -> Float
f2 x y
    | x == 0 = 0
    | otherwise = y^x + f2 (x - 1) y

{- f3 es igual a f2 solo que en la sumatoria, el indice superior, en vez de ser n (osea que el i
va de 1 a n, ahora es 2n, osea que va hasta el doble del numero que le pasamos) -}

f3 :: Integer -> Float -> Float
f3 x y = (f2 (2*x) y)

-- f4 es literalmente igual a f3 pero el i va de n a 2n, para eso reversionamos f2

f4 :: Integer -> Float -> Float
f4 x y = (f22 (2 * x) y x)

f22 :: Integer -> Float -> Integer -> Float
f22 x y z
    | x == z = y^x
    | otherwise = y^x + f5 (x - 1) y z


{- aca lo que hicimos fue reversionar f2 para que tome 3 valores, el doble del x que le pasamos, 
el y y el x inicial, 
porque la sumatoria tiene que parar cuando i vale lo mismo que el x original-} 
