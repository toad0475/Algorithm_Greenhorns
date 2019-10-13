def solution(a, b):
    if a == 1: a = 0
    elif a == 2: a = 31
    elif a == 3: a = 60
    elif a == 4: a = 91
    elif a == 5: a = 121
    elif a == 6: a = 152
    elif a == 7: a = 182
    elif a == 8: a = 213
    elif a == 9: a = 244
    elif a == 10: a = 274
    elif a == 11: a = 305
    elif a == 12: a = 335
    day = (a + b) % 7
    if day == 0: answer = 'THU'
    elif day == 1: answer = 'FRI'
    elif day == 2: answer = 'SAT'
    elif day == 3: answer = 'SUN'
    elif day == 4: answer = 'MON'
    elif day == 5: answer = 'TUE'
    elif day == 6: answer = 'WED'
    return answer