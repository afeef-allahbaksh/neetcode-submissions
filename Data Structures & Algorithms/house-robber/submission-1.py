class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            # temp = max(2 + 0, 0) = 2
            # temp = max(9 + 0, 2) = 9
            # temp = max(8 + 2, 9) = 10
            # temp = max(3 + 9, 10) = 12
            # temp = max(6 + 10, 12) = 16
            rob1 = rob2
            # rob1 = rob2 = 0
            # rob1 = rob2 = 2
            # rob1 = rob2 = 9
            # rob1 = rob2 = 10
            # rob1 = rob2 = 12
            rob2 = temp
            # rob2 = 2
            # rob2 = 9
            # rob2 = 10
            # rob2 = 12
            # rob2 = 16
        return rob2
        # return 16