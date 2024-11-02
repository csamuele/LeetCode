class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #text1 will represent rows, and text2 will represent columns in dp matrix
        prevRow = [0] * len(text2)

        for row in reversed(range(len(text1))):
            currRow = [0] * len(text2)
            for column in reversed(range(len(text2))):
                if text1[row] == text2[column]:
                    
                    currRow[column] = prevRow[column + 1] + 1 if column + 1 < len(text2) else 1
                
                else:
                    currRow[column] = max(currRow[column + 1], prevRow[column]) if column + 1 < len(text2) else prevRow[column]
            prevRow = currRow
        return currRow[0]

solution = Solution()
solution.longestCommonSubsequence('abcba', 'abcbcba')