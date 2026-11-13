class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits: return []

        phone = {
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
        def backtrack(i):
            # exit
            if i == len(digits):
                res.append("".join(ans))
                return

            for j in phone[digits[i]]:
                ans.append(j)
                backtrack(i+1)
                ans.pop()

        backtrack(0)
        return res
