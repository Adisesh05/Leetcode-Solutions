class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = ['', '1']  
        prev = pattern[0]  
        for num, i in enumerate(pattern + 'S', 2): 
            if i != prev:  
                if prev == 'D':  
                    stack[-2] = stack[-2][:-1] + stack[-1][::-1]
                else:  
                    stack[-2] = stack[-2][:-1] + stack[-1]
                
                stack[-1] = stack[-2][-1] + str(num)
                prev = i
            else:  
                stack[-1] += str(num)
        
        return stack[0]  