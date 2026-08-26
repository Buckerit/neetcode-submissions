class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapper = {"]": "[", ")": "(", "}": "{"}
        for char in s:
            if char in mapper:
                if len(stack) > 0 and mapper[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        if len(stack) != 0:
            return False
        return True