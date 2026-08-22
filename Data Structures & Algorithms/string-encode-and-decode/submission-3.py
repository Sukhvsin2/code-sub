class Solution:

    def encode(self, strs: List[str]) -> str:
        word = ""
        for s in strs:
            word += str(len(s)) + "#" + s
        return word

    def decode(self, s: str) -> List[str]:
        words, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = s[i:j]
            word = s[int(j+1) : j+1+int(length)]
            words.append(word)
            i = j+1+int(length)
        return words