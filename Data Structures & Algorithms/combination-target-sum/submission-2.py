class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        subset = []

        def dfs(i, curr_sum):
            
            if curr_sum == target:
                res.append(subset.copy())
                # subset.pop()
                return

            if i >= len(nums) or curr_sum > target:
                return # out of bound or sum greater than target

            # explore paths

            # include
            subset.append(nums[i])
            dfs(i, curr_sum + nums[i])

            subset.pop()
            # exclude
            dfs(i+1, curr_sum)


        dfs(0, 0)
        return res