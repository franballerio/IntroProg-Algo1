-- relacionesValidas 
relacionesValidas :: Eq t => [(t, t)] -> Bool
relacionesValidas [] = False
relacionesValidas ((x,y):[]) = relValida (x,y)
relacionesValidas ((x,y):xs) = noRepes xs && relValida (x,y) && relacionesValidas xs

relValida :: Eq t => (t,t) -> Bool
relValida (x,y) = x /= y 

noRepes :: Eq t => [(t, t)] -> Bool
noRepes [] = True
noRepes (x:[]) = True
noRepes ((a,b):xs)
    | elem (a,b) xs || elem (b,a) xs = False
    | otherwise = True

-- [("carla", "juan"),("juan", "pedro"),("maria","juan"),("pepe","fran"),("sofi","sofa")]

personasAux :: Eq t => [(t,t)] -> [t]
personasAux [] = []
personasAux ((x,y):[]) = [x,y]
personasAux ((x,y):xs) = [x,y] ++ personas xs  
-- pero hay q sacarle los repetidos, asiq le ponemos personasAux

noRepes2 :: Eq t => [t] -> [t]
noRepes2 [] = []
noRepes2 (x:[]) = [x]
noRepes2 (x:xs)
    | elem x xs = noRepes2 xs
    | otherwise = x: (noRepes2 xs)

personas :: Eq t => [(t,t)] -> [t]
personas xs = noRepes2 (personasAux xs)
-- ["carla","pedro","maria","juan","pepe","fran","sofi","sofa"]

amigosDe :: Eq t => t -> [(t,t)] -> [t]
amigosDe _ [] = []
amigosDe n ((x,y) : []) 
    | x == n = [y]
    | y == n = [x]
    | otherwise = []
amigosDe n ((x,y) : xs)
    | x == n = [y] ++ amigosDe n xs
    | y == n = [x] ++ amigosDe n xs
    | otherwise = amigosDe n xs





-- para el algo de persona con mas amigos agarramos la lista de personas
-- y se la damos a una funcion auxiliar que nos cuente la cant de amigos de cada uno
-- y con eso formamos una lista con tuplas del tipo (String, Int) siendo el nombre y la
-- cantidad de amigos que tiene, y a eso le buscamos el mayor numero

{-} Pensamos el algoritmo: 
con una funcion agarramos la lista q nos da personas y ahi vemos la cant d amigos de 
cada uno 

-}



personaConMasAmigosAux :: (Ord t, Eq t) => [(t,t)] -> (Int,[t])
personaConMasAmigosAux ((x,y):[]) = (1,[x])
personaConMasAmigosAux xs = maximum (listaAmigos (personas xs) xs)

listaAmigos :: Eq t => [t] -> [(t,t)] -> [(Int,[t])]
listaAmigos [] _ = [(0,[])]
listaAmigos _ [] = [(0,[])]
listaAmigos (p:[]) (t:[]) = [(length (amigosDe p (t:[])), [p])]
listaAmigos (p:ps) (t:ts) = [(length (amigosDe p (t:ts)), [p])] ++ listaAmigos ps (t:ts)

personaConMasAmigos :: (Ord t, Eq t) => [(t,t)] -> [t]
personaConMasAmigos ((x,y):[]) = [x]
personaConMasAmigos xs = slice (personaConMasAmigosAux xs)

slice :: Eq t => (Int,[t]) -> [t]
slice (_,[]) = []
slice (x,y) = y