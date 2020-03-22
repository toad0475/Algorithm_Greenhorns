# 최대공약수의 성질을 가지고 있다.

import math
def solution(w,h):
    return w*h - (w+h-math.gcd(w,h))
