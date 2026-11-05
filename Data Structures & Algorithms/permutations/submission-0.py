class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        
        res = []
        subset = []

        def backtrack():
            if len(subset) == len(nums):
                res.append(subset.copy())
                return

            for i, n in enumerate(nums):
                if n not in subset:
                    subset.append(n)
                    backtrack()
                    subset.pop()
        
        backtrack()
        return res