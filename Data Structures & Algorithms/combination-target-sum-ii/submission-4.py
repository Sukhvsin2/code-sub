class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # sort nums
        candidates.sort()

        res = []
        subset = []

        def dfs(i, curr_sum):
            
            # base cases
            if curr_sum == target:
                res.append([candidates[i] for i in subset])
                return
            
            if i >= len(candidates) or curr_sum > target:
                return # out of bound, sum not valid

            # include
            subset.append(i)
            dfs(i+1, curr_sum + candidates[i])

            subset.pop()
            # exclude
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1, curr_sum)

        dfs(0,0)
        return res