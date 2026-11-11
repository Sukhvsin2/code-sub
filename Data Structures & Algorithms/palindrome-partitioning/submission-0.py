class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        ans = []
        def dfs(i):

            # exit
            if i==len(s): 
                res.append(ans[:])
                return

            for j in range(i, len(s)):
                # print(f"i : {i} | j : {j} | ans : {ans}")
                if s[i:j+1] == s[i:j+1][::-1]:
                    ans.append(s[i:j+1])
                    # print(f"append ans: {ans}")
                    dfs(j+1)
                    ans.pop()
                    # print(f"pop ans: {ans}")

        dfs(0)
        return res