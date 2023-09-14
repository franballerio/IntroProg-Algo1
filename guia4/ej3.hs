es_div :: Float -> Float -> Bool
es_div x 0 = False
es_div x y = x == (abs (fromIntegral (truncate (x / y))) * y)