class Solution(object):
    
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        closeOpen = { ")":"(","}":"{","]":"["}
        for char in s:
            if char in closeOpen:
                if stack and stack[-1] == closeOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False
s = "()"
solution_instance = Solution()
print(solution_instance.isValid(s))
