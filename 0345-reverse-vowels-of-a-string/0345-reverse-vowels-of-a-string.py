class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        res = list(s)
        l, r = 0, len(res)-1
        
        while l < r:
            if res[l] in vowels and res[r] in vowels:
                res[l], res[r] = res[r], res[l]
                l += 1
                r -= 1
            elif res[l] in vowels:
                r -= 1
            elif res[r] in vowels:
                l += 1
            else:
                l += 1
                r -= 1
        
        return "".join(res)