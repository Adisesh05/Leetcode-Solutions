class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        a = s.split()
        for i in range(len(a) - 1, -1, -1): 
            if a[i].isalpha():
                a.remove(a[i])
            else:
                a[i] = int(a[i])
        for i in range(len(a)-1):
            if a[i] >= a[i+1]:
                return False
        return True
