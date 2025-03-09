class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        last = 0
        length = len(colors)
        perfect = 0
        i = 0
        while last < length:  
            
            if i - last == k - 1:  
                perfect += 1  
                last += 1 
                
            if colors[i % length] == colors[(i + 1) % length]: 
                last = i + 1  
            i += 1  
        return perfect