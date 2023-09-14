dist_pts :: (Float,Float) -> (Float,Float) -> Float
dist_pts (x1,y1) (x2,y2) = sqrt ((x1-x2)**2 + (y1-y2)**2)
