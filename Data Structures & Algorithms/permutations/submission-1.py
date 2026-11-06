class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        
        res = []
        subset = []

        def dfs():
            # exit statement
            if len(subset) == len(nums): 
                res.append(subset[:])
                return


            for n in nums:
                if n not in subset:
                    subset.append(n)
                    dfs()
                    subset.pop()

        dfs()
        return res