class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        count = 0
        length = len(flowerbed)
        i = 0
        while i < length:
            if flowerbed[i] == 0:
                left = (i == 0 or flowerbed[i-1] == 0)
                right = (i == length-1 or flowerbed[i+1] == 0)
                
                if left and right:
                    flowerbed[i] = 1  
                    count += 1
                    if count >= n:
                        return True
                    i += 1
            i += 1
        return count >= n