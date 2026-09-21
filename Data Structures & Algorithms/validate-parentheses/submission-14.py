class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        charMap = {'}': '{', ')':'(',']':'['}
        for c in s:
            if stack and c in charMap:
                if stack[-1] == charMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return stack == []

        # stack = ["[", "("]
        # 