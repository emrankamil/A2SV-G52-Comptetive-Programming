# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = TrieNode()
        for word in words:
            cur = trie
            for ch in word:
                idx = ord(ch) - ord('a')
                if not cur.children[idx]:
                    cur.children[idx] = TrieNode()
                cur = cur.children[idx]
            cur.is_end = True

        def dfs(cur):
            max_len = ""
            for i in range(26):
                if cur.children[i] and cur.children[i].is_end:
                    _next = chr(ord("a")+i) + dfs(cur.children[i])
                    if len(_next) > len(max_len):
                        max_len = _next
            return max_len
        
        return dfs(trie)