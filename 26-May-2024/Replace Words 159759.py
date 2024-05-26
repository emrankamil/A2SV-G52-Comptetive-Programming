# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self):
        self.children = [None]* 26
        self.is_end = False

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        def insert(word):
            cur = trie
            for ch in word:
                idx = ord(ch) - ord('a')
                if not cur.children[idx]:
                    cur.children[idx] = TrieNode()
                cur = cur.children[idx]
            cur.is_end = True
        
        def find_root(word):
            cur = trie
            root = []
            for i in range(len(word)):
                idx = ord(word[i]) - ord('a')
                if cur.is_end:
                    return root
                if not cur.children[idx]:
                    root.append(word[i:])
                    return root
                cur = cur.children[idx]
                root.append(word[i])
            return root
        

        trie = TrieNode()
        for word in dictionary:
            insert(word)
        sentence = sentence.split(" ")
        output = []
        for word in sentence:
            root = find_root(word)
            if root: output.append(root)

        return " ".join("".join(word) for word in output)