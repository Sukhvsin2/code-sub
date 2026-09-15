class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = set()
        count = 0
        l,r = 0,0
        # loop over the string
        while r < len(s):
            if s[r] in m:
                m.remove(s[l])
                l+=1
            else:
                m.add(s[r])
                r+=1
                count = max(count, len(m))

        return count