class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for i in words:
            wordChars = set(i)
            if all(chars in allowed for chars in wordChars):
                count += 1
        return count