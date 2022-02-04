"""
Merge Two Sorted Lists
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

There are two ways to do this: Iteratively or recursively.
"""


class ListNode:
    def __init__(self, val, next=None):
        self.val = val


class Solution:
    def merge_two_sorted_lists(l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.merge_two_sorted_lists(l1.next, l2)
            return l1
        else:
            l2.next = self.merge_two_sorted_lists(l1, l2.next)
            return l2
