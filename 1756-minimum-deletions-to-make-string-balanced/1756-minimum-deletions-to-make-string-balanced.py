class Solution:
    def minimumDeletions(self, s: str) -> int:
        count_b = 0  
        deletions = 0  

        for ch in s:
            if ch == 'a':
                deletions = min(deletions + 1, count_b)
            else:
                count_b += 1  

        return deletions

