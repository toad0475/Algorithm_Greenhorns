def solution(a, b):
    weekDays = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    numOfDysForEachMon = [31,29,31,30,31,30,31,31,30,31,30,31]
    return weekDays[(sum(numOfDysForEachMon[:a-1])+b)%7-1]

'''
def solution2(a, b):
    weekDays = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    numOfDysForEachMon = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    numOfDay = 0
    for i in range(a):
        numOfDay += numOfDysForEachMon[i]
    return weekDays[((numOfDay+b)%7)-1]
'''
