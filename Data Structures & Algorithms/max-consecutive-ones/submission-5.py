class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_counter = 0
        current_streak = 0

        for i, current_num in enumerate(nums):
            if current_num == 1:
                current_streak +=1
            else:
                # We don't see a one, meaning our current streak is over

                # Check if it is better,
                if current_streak > max_counter:
                    max_counter = current_streak
                
                #Then reset
                current_streak = 0

        if current_streak > max_counter:
            max_counter = current_streak

        return max_counter