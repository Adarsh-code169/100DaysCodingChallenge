# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # Dummy node to start the result list
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0  # Get value from l1, or 0 if None
            val2 = l2.val if l2 else 0  # Get value from l2, or 0 if None

            total = val1 + val2 + carry  # Total sum at this digit
            carry = total // 10  # Update carry
            current.next = ListNode(total % 10)  # Add new node to result
            current = current.next

            # Move to next node in input lists
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next  # Return the next of dummy as head of the result
            
            