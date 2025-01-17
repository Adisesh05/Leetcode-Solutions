class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        xsum=0
        for i in derived:
            xsum^=i
        return xsum==0