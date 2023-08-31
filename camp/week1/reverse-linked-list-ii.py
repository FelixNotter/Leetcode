# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
      
     # dummy = tail = ListNode()
        # 1->2->3->4->5
        # Now Get the left Node to perform The reversal on
        
        # <-----REVERSAL------->
        pre = None
        leftNode = head
        for _ in range(left - 1):
            pre = leftNode
            leftNode = leftNode.next
        #   1->2->3->4->5
        #   ^  ^
        # pre left
        # After Grabbing the left Node Let's perform reversal till right node
        previous = None
        current = leftNode
        for _ in range(right-left + 1 ):
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt
        # <-----REVERSAL END------->

    #  1  Null<-2<-3<-4        5
    #  ^              ^        ^
    # pre            previous current

            
        # Now we have reversed the section of the nodes we just need to add them together
        # If there was a previous node before left Then we make its next equal the reversed list's new head
            # then add it to the dummy's tail
        if pre:
    
            pre.next = previous
            # tail.next = head
        else:
            # if there was no node to the left that means the left was = 1 and  was the 
            # head of linked list so the tails next is just the reversed list's head 
            head = previous

        # Now we connect the joined linked list to the right part left
        leftNode.next = current

        # Return The Node That is The dummy's Next
        # return dummy.next
        return head
        
        




      


