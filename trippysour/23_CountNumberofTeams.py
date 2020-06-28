# 푸는 중

def numTeams(soldiers):
    if len(soldiers) < 3:
        return 0

    result = 0



    def maketeams(rate1, rate2):
        left = []
        right = []

        teams = 0

        for i in range(len(soldiers)-3):
            print(anchor)
            print(soldiers[i])
            if anchor < soldiers[i]:
                right.append(soldiers[i])

        print(right)
        if len(left) == 3:
            teams += 1
        elif len(right) == 3:
            teams += 1
        return teams
    
    index = 0
    for soldier in soldiers:
        maketeams(soldiers[index], soldiers[index+1])

    if soldiers[1] > soldiers[0] and soldiers[1] < soldiers[2]: result += 1
    elif soldiers[1] < soldiers[0] and soldiers[1] > soldiers[2]: result += 1

    return result

numTeams([2,5,3,4,1])
