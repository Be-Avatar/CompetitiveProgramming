class Solution:
    def countKeyChanges(self, s: str) -> int:
        new_s = s.lower()
        count = 0
        for i in range(len(s)-1):
            if new_s[i] != new_s[i+1]:
                count += 1
        return count