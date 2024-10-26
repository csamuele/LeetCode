# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class Solution:

    def __quickSortHelper(self, arr: list[Pair], start: int, end: int):

        if end - start <= 0:
            return arr
        
        pivot = arr[end]
        insertionPtr = start
        testPtr = start

        while(testPtr < end):
            if arr[testPtr].key >= pivot.key:
                testPtr += 1
            else:
                tmp = arr[insertionPtr]
                arr[insertionPtr] = arr[testPtr]
                arr[testPtr] = tmp
                insertionPtr += 1
                testPtr += 1
        arr[end] = arr[insertionPtr]
        arr[insertionPtr] = pivot
        self.__quickSortHelper(arr, start, insertionPtr - 1)
        self.__quickSortHelper(arr, insertionPtr + 1, end)
        return arr






    def quickSort(self, pairs: list[Pair]) -> list[Pair]:
        return self.__quickSortHelper(pairs, 0, len(pairs) - 1)
    
solution = Solution()
def convertTuplesToPairs(tuples: list[tuple]):
    return list(map(lambda tuple: Pair(tuple[0], tuple[1]), tuples))

testCase = convertTuplesToPairs([(6, "apple"), (2, "banana"), (4, "cherry"), (1, "date"), (3, "elderberry")])
test_1 = solution.quickSort(testCase)
test = 0