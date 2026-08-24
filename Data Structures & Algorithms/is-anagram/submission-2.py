class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dictS = {}
        dictT = {}

        for c in s:
            dictS[c] = dictS.get(c, 0) + 1

        for c in t:
            dictT[c] = dictT.get(c, 0) + 1
        dictS = dict(sorted(dictS.items(),key=lambda item: item[1]))
        dictT = dict(sorted(dictT.items(), key=lambda item: item[1]))
        if dictS == dictT:
            return True

        return False