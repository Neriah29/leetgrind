from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l = 0
        m = 0
        for r in range(len(s)):
            count[s[r]] += 1
            if  r - l + 1 - max(count.values()) <= k:
                cur_max = r - l + 1
            else:
                count[s[l]] -= 1
                l += 1
            m = max(m, cur_max )
        return m
