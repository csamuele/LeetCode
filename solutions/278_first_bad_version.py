# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version: int) -> bool:
    if version >= 4:
        return True
    else:
        return False

class Solution(object):
    def firstBadVersion(self, n: int):
        """
        :type n: int
        :rtype: int
        """
        lowerBound = 1
        upperbound = n
        
        while (lowerBound != upperbound):
            mid = (upperbound + lowerBound) // 2
            if (isBadVersion(mid)):
                upperbound = mid - 1
            else:
                lowerBound = mid + 1 
        
        return mid
    
solution = Solution()

print(solution.firstBadVersion(5))
print(solution.firstBadVersion(10))
