class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        hash = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        myList = []
        for v in s:
            # push if it's a opening parantheses
            if v in hash:
                if len(myList) <= 0:
                    return False
                elif len(myList) > 0 and myList.pop() != hash[v]:
                    return False
            else: # need pop logic here
                myList.append(v)

        if len(myList) != 0:
            return False
        return True
                