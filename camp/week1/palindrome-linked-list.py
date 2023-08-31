# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid = self.middle(head)
        reversed = self.reverse(mid)
        while head or reversed:
            if head and reversed and head.val != reversed.val:
                return False
            head = head.next
            if reversed : reversed = reversed.next
        return True

    def middle(self,head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def reverse(self,head):
        prev = None
        current = head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        return prev