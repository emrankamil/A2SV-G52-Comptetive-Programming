# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if not cur.children[idx]:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        cur.is_end = True

    def new_search(self, word, root):
        cur = root
        for i, ch in enumerate(word):
            if ch == '.':
                for child in cur.children:
                    if child:
                        rst = self.new_search(word[i+1:], child)
                        if rst: return rst
                return False
            idx = ord(ch) - ord('a')
            if not cur.children[idx]:
                return False
            cur = cur.children[idx]
        return cur.is_end

    def search(self, word: str) -> bool:
        return self.new_search(word, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)