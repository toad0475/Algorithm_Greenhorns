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
