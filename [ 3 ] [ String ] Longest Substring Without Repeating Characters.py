from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        length = 1
        if len(s) == 0:
            return 0
        check = set([s[0]])
        queue = deque([s[0]])
        for i in range(1, len(s)):
            if s[i] not in check:
                length += 1
                check.add(s[i])
                queue.append(s[i])
            else:
                answer = max(length, answer)
                while queue:
                    p = queue.popleft()
                    check.remove(p)
                    if p == s[i]:
                        break
                queue.append(s[i])
                check.add(s[i])
                length = len(check)
    
        answer = max(length, answer)
        return answer
