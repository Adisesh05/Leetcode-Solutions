class NumberContainers:
    def __init__(self):
        self.val = {}  
        self.res = {}  
    def change(self, index: int, number: int) -> None:
        if index in self.val:
            prevNum = self.val[index]
            if prevNum == number:
                return

        self.val[index] = number
        
        if number not in self.res:
            self.res[number] = []
        heapq.heappush(self.res[number], index)

    def find(self, number: int) -> int:
        if number not in self.res:
            return -1
        
        while self.res[number] and self.val[self.res[number][0]] != number:
            heapq.heappop(self.res[number])

        return self.res[number][0] if self.res[number] else -1

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)