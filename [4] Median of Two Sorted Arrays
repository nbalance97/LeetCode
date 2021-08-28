class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        from collections import deque
        
        q1 = deque(nums1)
        q2 = deque(nums2)
        
        total_length = len(nums1) + len(nums2)
        even = False
        
        def next_pop(q1, q2):
            temp = 0
            if q1 and q2:
                if q1[0] > q2[0]:
                    temp = q2.popleft()
                else:
                    temp = q1.popleft()
            elif q1:
                temp = q1.popleft()
            elif q2:
                temp = q2.popleft()
            return temp
            
        
        if total_length % 2 == 0:
            even = True
            median_idx = total_length // 2 
        else:
            median_idx = total_length // 2 + 1
        
        for i in range(median_idx-1):
            next_pop(q1, q2)

        answer = 0
        if even:
            answer = next_pop(q1, q2) + next_pop(q1, q2)
            answer = answer / 2
        else:
            answer = next_pop(q1, q2)
        
        answer = answer * 1.0
        
        return answer
