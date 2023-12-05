class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words)):
            configured_word = ""
            for j in words[i]:
                configured_word += chr(ord("a")+order.index(j))
            words[i] = configured_word
        return words == sorted(words)