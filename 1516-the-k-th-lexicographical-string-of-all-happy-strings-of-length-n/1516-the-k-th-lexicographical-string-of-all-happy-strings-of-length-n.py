class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if k > 3 * (1 << (n-1)):
            return ""

        first, remaining = divmod(k-1, 1 << (n-1))
        s = "abc"[first]
        for i in range(n-2, -1, -1):
            idx = (remaining >> i) & 1
            s += "abc"[idx] if "abc"[idx] < s[-1] else "abc"[idx+1]

        return s