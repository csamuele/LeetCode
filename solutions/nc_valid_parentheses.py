class Solution:
    def isValid(self, s: str) -> bool:
        bracketStack = []
        closeToOpen = { 
            ")" : "(", 
            "}" : "{",
            "]" :  '['}
        for char in s:
            if char in closeToOpen:
                if bracketStack and bracketStack[-1] == closeToOpen[char]:
                    bracketStack.pop()
                else:
                    return False
            else:
                bracketStack.append(char)
        if bracketStack:
            return False
        else:
            return True

test = Solution()
print(test.isValid("[]"))