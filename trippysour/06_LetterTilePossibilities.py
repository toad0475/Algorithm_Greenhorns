class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        r = len(tiles)
        letters = set() # 중복결과 제거를 위해 set 생성
        import itertools # 순열 기능
        for i in range(r):
            letters.update(map(''.join, itertools.permutations(tiles, r))) # titles의 원소로 순열 만들기
            r = r - 1
        return(len(letters))