import copy

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        subsets = []
        currSet = []

        def dfs(i):
            # base: if (i) goes off bound
            if i >= len(nums):
                subsets.append(currSet.copy())
                return

            currSet.append(nums[i])

            dfs(i+1) # traverse next element
            currSet.pop() # 
            dfs(i+1) # include next element

        dfs(0)
        return subsets