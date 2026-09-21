class Solution:
    def hoursLeftOver(self, piles: List[int], h:int, k: int):
        if k == 0: return 1
        hrs = 0
        for p in piles:
            hrs += math.ceil(p / k)
        
        if hrs > h:
            return 1
        else:
            return -1
        
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, hi = 1, max(piles)
        res = hi

        while low <= hi:
            guess = (low + hi) // 2

            if self.hoursLeftOver(piles, h, guess) == 1: # too slow
                low = guess + 1
            else:
                res = guess
                hi = guess - 1
        
        return res