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

            currSet.append(nums[i]) # add value

            dfs(i+1) # traverse left
            currSet.pop() # pop the value
            dfs(i+1) # travese right 

        dfs(0)
        return subsets