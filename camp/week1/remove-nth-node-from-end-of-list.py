# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Intialising Iterative variables
        count = 0
        current1 = head
        current2 = head
        #Counting number of Nodes
        while(current1 != None):
            count +=1
            current1 = current1.next
        #Base check to change head
        if count == n:
            head = head.next
        #Single element edge case
        elif count == 1:
            return None
        #Iterating to reroute Nodes
        while(current2 != None):
            if count == n+1:
                current2.next = current2.next.next
            current2 = current2.next
            count -=1
        return head