class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        upperBound, lowerBound = 1, 0
        currSum = arr[0]
        res = 0
        while upperBound < len(arr):
            while upperBound - lowerBound < k:
                currSum += arr[upperBound]
                upperBound += 1
            if currSum / k >= threshold:
                res += 1
            currSum -= arr[lowerBound]
            lowerBound += 1
        return res