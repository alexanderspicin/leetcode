"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransomNote_list = [let for let in ransomNote]
        magazine_list = [let for let in magazine]
        for let in ransomNote:
            try:
                magazine_list.remove(let)
            except:
                return False
        return True