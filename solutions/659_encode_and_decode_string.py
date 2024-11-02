class Solution:

    def encode(self, strs: list[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string)) + '#' + string
        return res

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            
        return res
    
solution = Solution()
encoded = solution.encode(["sam", "rocks"])
decoded = solution.decode(encoded)