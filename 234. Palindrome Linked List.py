"""
Given the head of a singly linked list, return true if it is a palindrome.
"""
class Solution(object):
    def isPalindrome(self, head):
        slow = head
        fast = head
        middle_count = 0
        while fast is not None and fast.next is not None:
            middle_count += 1
            slow = slow.next
            fast = fast.next.next
        first_part = []
        second_part = []
        new_head = head
        count = 0
        while new_head is not None:
            count += 1
            if count <= middle_count:
                first_part.append(new_head.val)
            else:
                second_part.append(new_head.val)
            new_head = new_head.next
        if len(first_part) != len(second_part):
            second_part.pop(0)
            return first_part == second_part[::-1]
        return first_part == second_part[::-1]