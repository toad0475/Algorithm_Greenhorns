class Solution:
    def frequencySort(self, s: str) -> str:
        dict = {}
        result = []

        for w in set(s):
            dict[w] = s.count(w)

        lst = sorted(dict.items(), key=lambda x:x[1], reverse=True)

        for i in range(len(lst)):
            for j in range(dict[lst[i][0]]):
                result.append(lst[i][0])

        return ''.join(result)
    
# Runtime: 40~56 ms, faster than 85.17%, Memory: 15.5 MB

# 아래는 Runtime: 20~32 ms, faster than 97.76%, Memory: 14.9MB
# class Solution:
#     def frequencySort(self, s: str) -> str:
#         cnt = sorted([(k, v) for k, v in Counter(s).items()], key=lambda x:x[1], reverse=True)
#         parts = [k * v for k, v in cnt]
#         return ''.join(parts)
