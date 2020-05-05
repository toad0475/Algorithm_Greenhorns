# 풀지는 못하고.. 아이디어가 비슷했던 코드 분석
# #https://leetcode.com/problems/word-break/discuss/428606/Python-Simple-Iterative-BFS-or-DFS-24ms

from collections import deque
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s or not wordDict: return False
        elif s in wordDict: return True

        else:
            visited = set()
            q = deque([s])
            # s 를 큐에 넣어놓고

            while q:
                word = q.popleft()
                for w in wordDict:
                    if word.startswith(w): # 팝한 단어가 w로 시작하면
                        new_word = word[len(w):] # word에서 그 단어만큼만 잘라내서 new_word로 지정
                        if new_word == "":
                            return True # 잘라냈는데 아무것도 없으면 True
                        if new_word not in visited:
                            q.append(new_word) # visited에 new_word가 없다면 q에 삽입
                            visited.add(new_word) # 체크를 위해 visited 에도 add

        return False # q에 아무것도 없을 때 까지 돌았는데 new_word가 공백이 아니면 False


