class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1,n//2 + 1):
            sub=s[:i]
            if sub * (n//i) == s:
                return True
        return False