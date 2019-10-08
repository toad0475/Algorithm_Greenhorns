prices = [7, 5, 3, 6, 3, 2]
index: int = -1
time: int = len(prices)
result = []
for i in range(time):
   index = index + 1
   time = time - 1
   nextindex: int = index
   for i in range(time):
       nextindex = nextindex + 1
       result.append(prices[nextindex] - prices[index])
if max(result) <= 0:
    print(0)
else:
    print(max(result))