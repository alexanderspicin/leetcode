"""
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the  customer has in the bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.
"""
class Solution(object):
    def maximumWealth(self, accounts):
        accounts_sum = []
        for account in accounts:
            accounts_sum.append(sum(account))
        return max(accounts_sum)