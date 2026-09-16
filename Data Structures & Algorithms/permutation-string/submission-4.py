class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        count1 = {} #hash map for S1

        for c in s1:
            count1[c] = 1 + count1.get(c, 0)

        
        need = len(count1) # we only need to match len(s1) chars in s2.
        for i in range(len(s2)):
            count2, curr = {}, 0

            for j in range(i, len(s2)):
                count2[s2[j]] = 1 + count2.get(s2[j], 0)
                # check if the current [j] value is in s1's hash map
                if count1.get(s2[j], 0) < count2[s2[j]]: 
                    break

                if count1.get(s2[j], 0) == count2[s2[j]]: 
                    curr += 1
                
                if need == curr: 
                    return True

        return False