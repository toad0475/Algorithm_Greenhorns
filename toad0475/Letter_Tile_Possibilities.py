# https://leetcode.com/submissions/detail/275918575/

import itertools

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        output = 0
        for i in range(1,len(tiles)+1):     
            output += len(set(map(''.join,itertools.permutations(tiles,i))))
        return output
