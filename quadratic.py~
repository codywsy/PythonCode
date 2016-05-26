# -*- coding: utf-8 -*-

import math
def quadratic(a,b,c):
    flag=math.pow(b,2)-4*a*c
    if flag<0:
        raise ValueError("no valid value")
    elif flag==0:
        return -b/(2*a)
    else:
        x1 = (-b+math.sqrt(flag))/(2*a)
        x2 = (-b-math.sqrt(flag))/(2*a)
        return x1,x2


