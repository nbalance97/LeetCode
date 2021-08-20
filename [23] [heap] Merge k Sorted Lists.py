# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        answer = []
        
        for l in lists:
            temp = l
            while temp != None:
                heapq.heappush(heap, temp.val)
                temp = temp.next
        
        root = ListNode()
        prev = root
        
        while heap:
            t = heapq.heappop(heap)
            temp = ListNode(val=t, next=None)
            prev.next = temp
            prev = temp
        
        root = root.next
        
        return root
