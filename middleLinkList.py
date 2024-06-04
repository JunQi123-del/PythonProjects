"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
 
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        middle = head
        end = head
        while end!=None and end.next!=None:
            middle = middle.next
            end = end.next.next
        return middle