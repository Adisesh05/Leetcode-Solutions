class ProductOfNumbers:
    def __init__(self):
        self.values = []  
        self.product = 1  

    def add(self, num: int) -> None:
        if num == 0:
            self.values.clear()
            self.product = 1
        else:
            self.product *= num  
            self.values.append(self.product) 

    def getProduct(self, k: int) -> int:
        if k > len(self.values):
            return 0 
        divisor = 1 if k == len(self.values) else self.values[-k-1]
        return self.values[-1] // divisor  


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)