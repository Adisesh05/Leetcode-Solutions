class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        la = len(a)
        lb = len(b)
        tl = (len(b) // len(a)) + 2
        for i in range(1, tl +1):
            if b in (a*i):
                return i
        return -1