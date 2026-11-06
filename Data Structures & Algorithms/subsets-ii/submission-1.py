class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        used = set()
        ans = []

        nums.sort()

        def dfs(i):
            
            # exit statement
            if i >= len(nums):
                res.append(ans[:])
                return

            
            # include the item
            ans.append(nums[i])
            used.add(i) # storing index so we can generate subset for dups
            dfs(i+1)

            # exclude the item
            ans.pop()
            used.remove(i)

            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i+=1

            dfs(i+1)

        dfs(0)
        return res