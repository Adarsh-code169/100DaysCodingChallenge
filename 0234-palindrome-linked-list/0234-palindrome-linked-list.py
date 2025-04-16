# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ptr=head
        s1=""
        while ptr is not None:
            s1=s1+str(ptr.val)
            ptr=ptr.next
        return s1==s1[::-1]
        