# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode],prev = None) -> Optional[ListNode]:
        # #Empty list base case
        # if head == None:
        #     return None
        # #initialising iterating variables
        # current = head
        # prev = None
        # next1 = current.next
        # #Visiting and rerouting Nodes
        # while(next1 != None):
        #     current.next = prev
        #     prev = current
        #     current = next1
        #     next1 = next1.next
        # #Rerouting New head node and returning it
        # current.next = prev
        # return current
        if not head:return prev
        current = head.next
        head.next = prev
        prev = head
        return self.reverseList(current,prev)