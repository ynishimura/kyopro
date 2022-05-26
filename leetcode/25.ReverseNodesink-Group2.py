# https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/718457/python3-easy-recursion-solution

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
