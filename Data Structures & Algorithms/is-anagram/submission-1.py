class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapS = {}
        mapT = {}
        for c in s:
            mapS[c] = mapS.get(c,0) + 1
        for c in t:
            mapT[c] = mapT.get(c,0) + 1
        return mapS == mapT
        