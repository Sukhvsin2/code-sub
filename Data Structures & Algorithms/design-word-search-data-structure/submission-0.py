class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}

    def __repr__(self):
        return f"word: {self.word} | children: {self.children.keys()} \n"

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.word = True # ending of a word

    def search(self, word: str) -> bool:

        def dfs(j, root):
            curr = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[word[i]]
            
            return curr.word # exit statement

        
        return dfs(0, self.root)
        