# 1- Optimizing box weight: you have 2 boxes A and B return subset A in increasing order where sum of A' weight > sum of B' weight. if More than one subset A exist, return the one with the maximal weight.
# Conditions:


# A & B intersection is null
# Union is equevilant to original array
# number of elements in A is minimal
# sum of A weights > sum of B weights

class Solution (object):
    def optimizeBoxWeight(self, arr: list[int]):
        if not arr:
            return []
        total = 0
        count: dict[list[int]] = {}
        possibleValues: list[int] = []
        for num in arr:
            total += num
            if num in count:
                count[num][0] += 1
                count[num][1] += num
            else:
                count[num] = [1, num]
                possibleValues.append(num)
        bestCombination = [[], 0, len(arr)]
        halfTotal = total // 2
        def dfs(values: list[int], total: int, numValues: int, index):
            nonlocal bestCombination
            if total > halfTotal:
                if numValues < bestCombination[2]:
                    bestCombination = [values[:], total, numValues]
                elif numValues == bestCombination[2]:
                    if total > bestCombination[1]:
                        bestCombination = [values[:], total, numValues]
                return
            if index >= len(possibleValues):
                return
            currentValue = possibleValues[index]
            values.append(currentValue)
            dfs(values, total + count[currentValue][1], numValues + count[currentValue][0], index + 1)
            values.pop()
            dfs(values, total, numValues, index + 1)
        dfs([], 0, 0, 0)
        bestCombination[0].sort()
        res = []
        for value in bestCombination[0]:
            res = res + [value for i in range(count[value][0])]
        return res
        
    
solution = Solution()
testArray = [1, 1, 1, 2, 2, 2, 2, 3, 3, 4]
print(solution.optimizeBoxWeight(testArray))
