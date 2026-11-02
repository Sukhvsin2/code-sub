class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # need to sort first so next element in nums is always greater
        nums.sort()

        res = []
        subset = []

        def dfs(i, curr_sum):
            
            # base case
            if i >= len(nums):
                return # invalid index

            # add current value to subset and curr_sum
            subset.append(nums[i])
            curr_sum += nums[i]

            # if we found the sum
            if curr_sum == target:
                res.append(subset.copy())
                subset.pop() # to explore other path
                return
            elif curr_sum > target:
                subset.pop() # abandon this path
                return

            # include in the path
            dfs(i, curr_sum)


            # excluding the same num
            curr_sum -= subset.pop()
            dfs(i+1, curr_sum) # explore path with next index value

        # keep track of sum so every subset's sum should be less then or equal to target
        # dfs(index, curr_sum)
        dfs(0, 0)
        return res