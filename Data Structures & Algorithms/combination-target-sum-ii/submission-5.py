class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        used = set()
        subset = []

        candidates.sort()
        def dfs(i, curr_sum):



            # exit
            if curr_sum == target:
                res.append(subset[:])
                return

            if curr_sum > target or i >= len(candidates):
                return # invalid
            
            # since we can't have dups making sum to target
            # include
            subset.append(candidates[i])
            used.add(i)
            dfs(i+1, candidates[i] + curr_sum)

            # exclude
            subset.pop()
            used.remove(i)

            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i+=1

            dfs(i+1, curr_sum)

        dfs(0, 0)
        return res