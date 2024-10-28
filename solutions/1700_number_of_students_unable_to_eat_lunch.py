from collections import Counter

class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        count = Counter(students)
        res = len(students)
        for s in sandwiches:
            if count[s] > 0:
                count[s] -= 1
                res -= 1
            else:
                return res
        return res

    
solution = Solution()
solution.countStudents([1,1,0,0], [0,1,0,1])
solution.countStudents([1,1,1,0,0,1], [1,0,0,0,1,1])

        