class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        sSet = []

        def dfs(i):
            
            if i >= len(nums):
                res.append(sSet.copy())
                return

            sSet.append(nums[i])

            # include the value
            dfs(i+1)

            # no include the value
            sSet.pop()
            dfs(i+1)


        dfs(0)
        return res