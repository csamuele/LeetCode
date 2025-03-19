class Solution(object):
    def isCircularSentence(self, sentence: str):
        """
        :type sentence: str
        :rtype: bool
        """
        if sentence[0] != sentence[-1]:
            return False
        wordList = sentence.split(' ')
        for currWord in range(len(wordList) - 1):
            if wordList[currWord][-1] != wordList[currWord + 1][0]:
                return False
        return True