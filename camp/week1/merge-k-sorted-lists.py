# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = None
        for cur in lists:
            res = self.merge(res,cur)
        return res


    def merge(self,head1,head2):
        cur1 = head1
        cur2 = head2
        dummy = tail = ListNode()
        while cur1 and cur2:
            if cur1.val < cur2.val:
                tail.next = cur1
                cur1 = cur1.next
            else:
                tail.next = cur2
                cur2 = cur2.next
            tail = tail.next
        if cur1:
            tail.next = cur1
        if cur2:
            tail.next = cur2
        return dummy.next

        