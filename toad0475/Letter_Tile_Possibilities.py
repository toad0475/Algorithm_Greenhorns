# https://leetcode.com/problems/letter-tile-possibilities/submissions/

import itertools

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        tileMap=set()
        for i in range(1,len(tiles)+1):
            for t in itertools.permutations(tiles,i):
                tileMap.add(''.join(t))
        return len(tileMap)
