class Solution:
    def isAnagram(self, string1, string2):
        if len(string1) != len(string2):
            return False
        count1 = {}
        count2 = {}
        for i in range(len(string1)):
            count1[string1[i]] = count1.get(string1[i], 0) + 1
            count2[string2[i]] = count2.get(string2[i], 0) + 1
        return count1 == count2

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if not strs:
            return []
        foundAnagram = set()
        anagramGroups = []
        for mainPointer in range(len(strs)):
            if strs[mainPointer] not in foundAnagram:
                foundAnagram.add(strs[mainPointer])
                anagramGroup = [strs[mainPointer]]
                anagramGroups.append(anagramGroup)
                for secondPointer in range(mainPointer + 1, len(strs)):
                    if self.isAnagram(strs[mainPointer], strs[secondPointer]):
                        anagramGroup.append(strs[secondPointer])
                        foundAnagram.add(strs[secondPointer])
        return anagramGroups
                
