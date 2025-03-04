class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        power = 14
        while power >= 0 and n > 0:
            num = pow(3, power)
            if n >= num:
                n -= num
            power -= 1
        return n == 0