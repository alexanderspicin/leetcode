"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        index = 0
        while True:
            if len(word1)> index:
                result.append(word1[index])
            if len(word2) > index:
                result.append(word2[index])
            if len(word1) < index and len(word2) < index:
                break
            index += 1
        return ''.join(result)


sol= Solution()
print(sol.mergeAlternately(word1 = "ab", word2 = "pqr"))