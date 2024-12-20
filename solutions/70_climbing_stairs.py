class Solution:
    def climbStairs(self, n: int) -> int:
        if n in range(4):
            return n
        arr = [2, 3]
        for _ in range(3, n):
            tmp = arr[1]
            arr[1] = tmp + arr[0]
            arr[0] = tmp
        return arr[1]