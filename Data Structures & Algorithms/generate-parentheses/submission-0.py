class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        
        res = []
        ans = []

        def backtrack(openP, closeP):
            # exit
            if openP == closeP == n:
                res.append("".join(ans))
                return

            # conditions
            if openP < n: # can only open n number of PN.
                ans.append("(")
                backtrack(openP+1, closeP)
                ans.pop()
            
            if closeP < openP: # since we can't close less then opened PN
                ans.append(")")
                backtrack(openP, closeP+1)
                ans.pop()

        backtrack(0,0)

        return res