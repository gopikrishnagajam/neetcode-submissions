# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:   
        def rev(node):
            current =node
            new =None
            while current:
                temp = current
                current = current.next
                temp.next = new
                new = temp
            return new
        
        reverse  = rev(head)

        prev = None
        current = reverse
        it =1
        while current and it<n:
            prev =current
            current = current.next
            it+=1
        if not prev:
            temp = reverse
            reverse = reverse.next
            temp.next = None
        else:
            prev.next = current.next
            current.next =None

        return rev(reverse)

