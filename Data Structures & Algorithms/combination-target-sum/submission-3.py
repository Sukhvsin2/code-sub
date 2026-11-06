class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        subset = []


        def dfs(i, curr_sum):

            if curr_sum == target:
                res.append(subset[:])
                return

            if i>=len(nums) or curr_sum > target: # out of bound
                return

            
            # include
            subset.append(nums[i])
            dfs(i, nums[i] + curr_sum)

            # exclude
            subset.pop()
            dfs(i+1, curr_sum)

        
        dfs(0,0)
        return res