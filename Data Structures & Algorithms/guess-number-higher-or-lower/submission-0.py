# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 0, n

        while l <= r:
            guess_val = (l + r) // 2

            if guess(guess_val) == 1: # lower
                l = guess_val + 1
            elif guess(guess_val) == -1: # higher
                r = guess_val - 1
            else:
                return guess_val
        
        return -1
        