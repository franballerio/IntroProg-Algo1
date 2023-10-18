-- Ejercicio 1
votosEnBlanco :: [(String, String)] -> [Int] -> Int  ->  
votosEnBlanco formulas (v:vs) totalVotos 
    | totalVotos > (cantVotos (v:vs)) = totalVotos - (cantVotos (v:vs))
    | otherwise = 0

-- Ejercicio 2
formulasValidas :: [(String, String)] -> Bool
formulasValidas [] = True
formulasValidas ((x,y):[]) = x /= y
formulasValidas ((x,y):xs) = noRepes ((x,y):xs) && cases (x,y) xs && cases2 (x,y) && formulasValidas xs

noRepes :: (Eq t) => [t] -> Bool 
noRepes [] = True
noRepes (x:[]) = True
noRepes (x:xs) 
    | elem x xs = False
    | otherwise = noRepes xs

cases2 :: (Eq t) => (t,t) -> Bool 
cases2 (x,y) = x /= y

cases :: (Eq t) => (t,t) -> [(t,t)] -> Bool
cases _ [] = True
cases (x,y) ((a,b):[]) 
    | a == x || b == x || a == y || b == y || a == y || b == x = False
    | otherwise = True
cases (x,y) ((a,b):xs) 
    | a == x || b == x || a == y || b == y || a == y || b == x = False
    | otherwise = cases (x,y) xs


-- Ejercicio 3
division :: Int -> Int -> Float
division a b = (fromIntegral a) / (fromIntegral b)

porcentajeDeVotos :: String -> [(String, String)] -> [Int] -> Float
porcentajeDeVotos presi ((x,y):[]) (v:[])
    | x == presi = (division (v * 100) (cantVotos (v:[])))
    | otherwise = 0.0
porcentajeDeVotos presi ((x,y):xs) (v:vs) 
    | presi == x = (division (v * 100) (cantVotos (v:vs)))
    | otherwise = porcentajeDeVotos presi xs (vs ++ [v])

cantVotos :: [Int] -> Int
cantVotos [] = 0
cantVotos (x:[]) = x
cantVotos (x:xs) = x + cantVotos xs

-- Ejercicio 4
proximoPresidente :: [(String, String)] -> [Int] -> String
proximoPresidente ((x,y):[]) _ = x
proximoPresidente ((w,x):(y,z):xs) (a:b:votos)
    | a > b = proximoPresidente ((w,x):xs) (a:votos)
    | otherwise = proximoPresidente ((y,z):xs) (b:votos)
