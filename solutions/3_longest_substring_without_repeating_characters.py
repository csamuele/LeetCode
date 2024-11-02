class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        lowerBound, upperBound = 0, 0
        res = 0

        while upperBound < len(s):
            if s[upperBound] not in window:
                window.add(s[upperBound]) 
                upperBound += 1
                res = max(res, upperBound - lowerBound)

            else:
                window.remove(s[lowerBound])
                lowerBound += 1
        return res
