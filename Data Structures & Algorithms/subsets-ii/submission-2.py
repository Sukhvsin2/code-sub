class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        ans = []

        # so i can avoid picking similar path again
        nums.sort()

        def dfs(i):
            
            # exit
            if i >= len(nums):
                res.append(ans[:])
                return

            
            # include the first occurance
            ans.append(nums[i])
            dfs(i+1)

            # exclude same to explore further
            ans.pop()
            
            # skip dups
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i+=1

            dfs(i+1)


        dfs(0)
        return res