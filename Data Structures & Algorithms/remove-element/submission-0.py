class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for r in range(0, len(nums)):
            if nums[r] != val:
                nums[count] = nums[r]
                count += 1
        return count

        