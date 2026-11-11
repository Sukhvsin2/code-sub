class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res, ans = [], []
        def dfs(i):
            # exit
            if i == len(digits):
                res.append("".join(ans))
                return

            for d in list(map[digits[i]]):
                ans.append(d)
                dfs(i+1)
                ans.pop()


        dfs(0)
        return res