prices = [7, 5, 3, 6, 3, 2]
index: int = 0
time: int = len(prices)
result = []
for i in range(time):
   index = index - 1
   time = time - 1
   minus: int = - 1
   previousindex: int = index - minus
   print(index, previousindex)
   if previousindex == -1*time:
     break
   else:
      for i in range(time):
          if previousindex == -1 * time:
            break
          else:
            previousindex = previousindex - minus
            result.append(prices[index] - prices[previousindex])
            print(index, previousindex)
if max(result) <= 0:
   print("0")
else:
   print(max(result))