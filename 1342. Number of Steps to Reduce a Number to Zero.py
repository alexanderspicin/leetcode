"""
Given an integer num, return the number of steps to reduce it to zero.
In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
"""

class Solution(object):
    def numberOfSteps(self,num):
        steps = 0
        number = num
        while number != 0:
            if number % 2 == 0:
                number = number / 2
                steps += 1
            elif number == 1:
                number -= 1
                steps += 1
            else:
                number = (number - 1) / 2
                steps += 2
        return steps