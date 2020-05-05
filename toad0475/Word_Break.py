# submission : https://leetcode.com/submissions/detail/334788933/
# 재귀로 풀었음

class Solution:
    def wordBreak(self, s, wordDict):
        cache = {}
        wordDict = set(wordDict)
        def finder(s):
            if not s: return True
            if s in cache: return cache[s]
            for word in wordDict:
                if s.startswith(word) and finder(s[len(word):]):
                    cache[s] = True
                    return True
            cache[s] = False
            return False
        return finder(s)