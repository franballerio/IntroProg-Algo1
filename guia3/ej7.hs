dist_manh :: (Float,Float,Float) -> (Float,Float,Float) -> Float
dist_manh (x1,x2,x3) (y1,y2,y3) = abs (x1-y1) + abs (x2-y2) + abs (x3-y3)

