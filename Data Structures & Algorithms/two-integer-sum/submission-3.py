class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, n in enumerate(nums):
            num = target - n
            if num in map:
                return [map[num], i]
            map[n] = i
        