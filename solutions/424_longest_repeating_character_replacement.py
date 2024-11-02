class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res = 0
        count = {}
        lowerBound = 0
        maxFrequency = 0
        for upperBound in range(len(s)):
            count[s[upperBound]] = count.get(s[upperBound], 0) + 1
            maxFrequency = max(maxFrequency, count[s[upperBound]])
            while (upperBound - lowerBound + 1) - maxFrequency > k:
                count[s[lowerBound]] -= 1
                lowerBound += 1
            res = max(res, upperBound - lowerBound + 1)
        return res

