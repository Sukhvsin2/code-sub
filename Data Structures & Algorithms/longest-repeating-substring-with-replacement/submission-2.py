class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        count = {}
        maxF = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0) # default to 0, increment everytime.
            maxF = max(maxF, count[s[r]])
            # check if the window is invalid before move to update result
            # while (r-l+1) - max(count.values()) > k:
            while (r-l+1) - maxF > k:
                count[s[l]] -= 1
                l+=1

            # add the max window size to the result
            res = max(res,r-l+1)

        return res

