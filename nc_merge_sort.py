
# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class Solution:
    
    #We're merging each array in place, so we can split the array here instead of taking 3 arrays
    def merge(self, arr:list[Pair], start: int, middle: int, end: int):

        #Our two arrays:
        leftArray = arr[start : middle + 1]
        rightArray = arr[middle + 1 : end + 1]

        #Pointers:
        leftPointer = 0
        rightPointer = 0
        arrPointer = start

        #Merge the arrays
        while (leftPointer < len(leftArray) and rightPointer < len(rightArray)):
            if leftArray[leftPointer].key <= rightArray[rightPointer].key:
                arr[arrPointer] = leftArray[leftPointer]
                leftPointer += 1
                arrPointer += 1
            else:
                arr[arrPointer] = rightArray[rightPointer]
                rightPointer += 1
                arrPointer += 1
        #One of the halfs has elements remaining:
        while leftPointer < len(leftArray):
            arr[arrPointer] = leftArray[leftPointer]
            leftPointer += 1
            arrPointer += 1
        while rightPointer < len(rightArray):
            arr[arrPointer] = rightArray[rightPointer]
            rightPointer += 1
            arrPointer += 1

    def mergeSortHelper(self, pairs: list[Pair], start: int, end: int):
        if end - start + 1 <= 1:
            return pairs
        
        middle = (start + end) // 2

        self.mergeSortHelper(pairs, start, middle)
        self.mergeSortHelper(pairs, middle + 1, end)

        self.merge(pairs, start, middle, end)

        return pairs

    def mergeSort(self, pairs: list[Pair]) -> list[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs) - 1)
    
solution = Solution()

solution.mergeSort([Pair(5, "apple"), Pair(2, "banana"), Pair(9, "cherry"), Pair(1, "date"), Pair(9, "elderberry")])

test = 0        
        
