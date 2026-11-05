class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        def solve(node, w):
            if not w:
                return node.endOfWord
            if w[0] != '.' and w[0] not in node.children:
                return False
            if w[0] == '.':
                for ch in node.children.keys():
                    if solve(node.children[ch], w[1:]):
                        return True
                return False
            else:
                return solve(node.children[w[0]], w[1:])

        return solve(self.root, word)
        
