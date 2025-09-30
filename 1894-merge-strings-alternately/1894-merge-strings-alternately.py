class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a = ""
        for i,j in zip(word1,word2):
            a += i + j
        return a + word1[len(word2):] + word2[len(word1):]