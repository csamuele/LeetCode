class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        lowerBound, upperBound = 0, 1
        res = 1
        prevSign = ""

        while upperBound < len(arr):
            if arr[upperBound] < arr[upperBound - 1] and prevSign != "<":
                res = max(upperBound - lowerBound + 1, res)
                upperBound += 1
                prevSign = "<"
            elif arr[upperBound] > arr[upperBound - 1] and prevSign != ">":
                res = max(upperBound -  lowerBound + 1, res)
                upperBound += 1
                prevSign = ">"
            else:
                if arr[upperBound] == arr[upperBound - 1]:
                    lowerBound = upperBound
                    upperBound += 1
                else:
                    lowerBound = upperBound - 1
                prevSign = ""
                
        return res




