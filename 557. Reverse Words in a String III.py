"""Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace
    and initial word order.
"""


class Solution(object):
    def reverseWords(self, s):
        reverse_text = ""
        for word in s.split(" "):
            reverse_text += word[::-1] + " "
        return reverse_text[:-1]
