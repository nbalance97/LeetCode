# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = 0
        idx = 1
        temp = l1
        while temp:
            a += temp.val * idx
            idx *= 10
            temp = temp.next
            
        b = 0
        idx = 1
        temp = l2
        while temp:
            b += temp.val * idx
            idx *= 10
            temp = temp.next
        
        print(a, b)
        c = str(a + b)[::-1]
        
        head = None
        last = None
        for i in c:
            node = ListNode(val=int(i))
            if head is None:
                head = node
                
            if last is not None:
                last.next = node
                last = node
            else:
                last = node
        
        return head
