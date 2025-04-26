class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        tri = [[1]]
        
        for i in range(1, numRows):
            prev = tri[-1]
            nextt = [1]
            for j in range(1, len(prev)):
                nextt.append(prev[j-1] + prev[j])
            
            nextt.append(1)
            tri.append(nextt)
        return tri