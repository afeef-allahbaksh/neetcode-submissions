class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        res = None
        for d in digits:
            num += str(d)
        res = 1 + int(num)
        return [int(d) for d in str(res)]
        