class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        courses = {}
        def isLoop(course: int, prereqs: list[int]):
            if not prereqs:
                return False
            if course in prereqs:
                return True
            for prereq in prereqs:
                return isLoop(course, courses[prereq])
        
        for course, prereq in prerequisites:
            if prereq not in courses:
                courses[prereq] = []
            if course in courses:
                courses[course].append(prereq)
                if isLoop(course, [prereq]):
                    return False
                
            else:
                courses[course] = [prereq]
        return True

test = [[0, 2], [2,1], [1, 0]]
solution = Solution()
solution.canFinish(3, test)
