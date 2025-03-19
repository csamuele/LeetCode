class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if not s or len(s) != len(goal):
            return False
        needle = s
        haystack = goal + goal
        lps = [0] * len(needle)
        prevLPS, i = 0, 1
        while i < len(needle):
            if needle[i] == needle[prevLPS]:
                lps[i] = prevLPS + 1
                prevLPS += 1
                i += 1
            else:
                if prevLPS == 0:
                    lps[i] = 0
                    i += 1
                else:
                    prevLPS = lps[prevLPS - 1]
            hayStkPtr = 0
            needlePtr = 0
        while hayStkPtr < len(haystack):
            if haystack[hayStkPtr] == needle[needlePtr]:
                hayStkPtr += 1
                needlePtr += 1
            else:
                if needlePtr == 0:
                    hayStkPtr += 1
                else:
                    needlePtr = lps[needlePtr - 1]
            if needlePtr == len(needle):
                return True
        return False
    enu
        