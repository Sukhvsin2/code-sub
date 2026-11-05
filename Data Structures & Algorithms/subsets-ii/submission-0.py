class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        ans = []
        def backtrack(i):
            

            if i >= len(nums):
                res.append(ans[:])
                return
            
            ans.append(nums[i])
            backtrack(i+1)

            ans.pop()
            
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+= 1

            backtrack(i+1)

        nums.sort()
        backtrack(0)
        return res