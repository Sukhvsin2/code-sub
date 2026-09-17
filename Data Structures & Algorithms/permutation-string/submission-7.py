class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        
        if n1 > n2: return False

        # find match
        s1Count, s2Count = [0] * 26, [0] * 26

        for i in range(n1):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # check if both arrays are equal 
        # if yes first len(s1) matches with substring of s2
        if s1Count == s2Count:
            return True


        # build window
        # start from n1 since we have added before n1 already
        # it will build window of len(s1) or n1 
        # and move 1 by 1
        for r in range(n1, n2):
            s2Count[ord(s2[r]) - ord('a')] += 1

            # move left pointer and decrease the freq.
            s2Count[ord(s2[r - n1]) - ord('a')] -= 1

            # check for match
            if s1Count == s2Count:
                return True

        # default response
        return False