class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        xint = [(sx, ex) for sx, _, ex, _ in rectangles]
        yint = [(sy, ey) for _, sy, _, ey in rectangles]
        xint.sort()
        yint.sort()
        maxx, maxy = xint[0][1], yint[0][1]

        sepx, sepy = 1, 1  

        for i in range(1, len(xint)):
            if xint[i][0] >= maxx:
                sepx += 1  

            if yint[i][0] >= maxy:
                sepy += 1  

            if sepx >= 3 or sepy >= 3:
                return True

            maxx = max(maxx, xint[i][1])
            maxy = max(maxy, yint[i][1])

        return False