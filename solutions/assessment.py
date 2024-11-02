#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findFinalValues' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY coins as parameter.
#
from collections import defaultdict, deque
from heapq import heappush, heappop
def findFinalValues(coins):
    # Write your code here
    coinHash = defaultdict(deque)
    uniqueHeap = []
    finalLength = len(coins)
    for i, coin in enumerate(coins):
        if coin not in coinHash:
            heappush(uniqueHeap, coin)
        coinHash[coin].append(i)
    while uniqueHeap:
        currDenom = heappop(uniqueHeap)
        while len(coinHash[currDenom]) > 1:
            coinHash[currDenom].popleft()
            convertedCoinIndex = coinHash[currDenom].popleft()
            coinHash[currDenom]
            if currDenom * 2 not in coinHash:
                heappush(uniqueHeap, currDenom * 2)
            coinHash[currDenom * 2].appendleft(convertedCoinIndex)
            finalLength -= 1
    res = [0] * finalLength
    for key in coinHash:
        for index in coinHash[key]:
            res[index] = key
    return res
findFinalValues([1, 3, 1])