class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        # First, hone in on the row
        bot, top = 0, (m - 1)
        
        while bot <= top:
            mid = (bot + top) // 2
            if target > matrix[mid][-1]:
                bot = mid + 1
            elif target < matrix[mid][0]:
                top = mid - 1
            else:
                break
        
        if bot > top:
            return False
        
        row = (bot + top) // 2

        l, r = 0, (n - 1)

        while l <= r:
            mid = (l + r) // 2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True
        
        return False


