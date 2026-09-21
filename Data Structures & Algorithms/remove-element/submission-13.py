class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        curr, look_ahead = 0, 0

        while (look_ahead < len(nums)):
            if (nums[look_ahead] == val):
                look_ahead += 1
            else:
                nums[curr] = nums[look_ahead]
                look_ahead += 1
                curr += 1
    
        return curr

        