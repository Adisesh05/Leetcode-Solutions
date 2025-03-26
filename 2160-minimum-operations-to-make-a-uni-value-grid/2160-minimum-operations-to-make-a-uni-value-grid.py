class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        l=[]
        for i in grid:
            l.extend(i)
        l.sort()
        c=0
        le=len(l)
        chk=l[le//2]
        for i in l:
            if abs(i-chk)%x==0:
                c+=abs(i-chk)//x
            else:
                return -1
        return c