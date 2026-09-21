class Solution:
    def isValid(self, s: str) -> bool:
        parens = []
        parens_map = {'(' : ')', '{' : '}', '[' : ']'}

        for char in s:
            if char in parens_map:
                parens.append(parens_map[char])
            else:
                # We are seeing a right parenthesis

                # What if we see a right paren when the stack is empty?
                # That means we never saw a corresponding left paren
                if not parens:
                    return False

                # In the event the stack is full, make sure the character
                # We expect to see matches the right paren we are seeing
                if parens.pop() != char:
                    return False
        
        return not parens
            