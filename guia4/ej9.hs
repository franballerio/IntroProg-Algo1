-- Ejercicio 9. Especificar e implementar una 
-- funcion esCapicua :: Integer ->Bool que dado n ∈ N≥0 determina si n es
-- un numero capicua.

{- 1. Especific
esCapicua (x : N) : Bool {
    requiere {True}
    asegura {res = de derecha a izquierda que de izquierda a derecha}
}
-}

{- 2. Algoritmo
queremos saber si el numero puede leerse de der a izq y de izq a der
para esto el primer y ultimo num deben ser iguales (y ya tenemos funciones que nos
devuelvan el primer y ultimo)
entonces usamos la recursion para el mismo numero pero sin el ult ni el prim 
-}

cant_dig :: Integer -> Integer
cant_dig x
    | x < 10 = 1
    | otherwise = 1 + cant_dig (del_ult x)

del_ult :: Integer -> Integer
del_ult x = div x 10

ult_dig :: Integer -> Integer
ult_dig x = mod x 10

prim_dig :: Integer -> Integer
prim_dig x = div x (10 ^ ((cant_dig x)-1))

del_prim :: Integer -> Integer
del_prim x
    | x < 10 = x
    | otherwise = mod x (10 ^ ((cant_dig x)-1))



es_capi :: Integer -> Bool
es_capi x 
    | x < 10 = True
    | prim_dig x == ult_dig x = es_capi (del_ult(del_prim x))
    | otherwise = False
