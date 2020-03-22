# w와 h가 서로소가 될때 쪼갠 후 대각선을 그렸을 때 접힌 사각형의 개수를 구해야 한다.
# 이때 접힌 사각형의 개수는 최대공약수 만큼 발생하게 된다.

# 두수가 서로소일때 접힌 사각형 개수를 구하는 방법은
# x + y - 1 이다.

import math
def solution(w,h):
    return w*h - (w+h-math.gcd(w,h))
