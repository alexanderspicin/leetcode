"""
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
"""


def fizzBuzz(n):
    result = []
    for dig in range(1, n + 1):
        if dig % 3 == 0 and dig % 5 == 0:
            result.append('FizzBuzz')
        elif dig % 3 == 0:
            result.append('Fizz')
        elif dig % 5 == 0:
            result.append('Buzz')
        else:
            result.append(str(dig))
    return result