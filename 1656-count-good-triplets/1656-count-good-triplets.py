class Solution:
    def countGoodTriplets(self, arr, a, b, c):
        n = len(arr)
        count = 0
        for j in range(1, n - 1):  
            for i in range(j):     
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j + 1, n):  
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            count += 1
        return(count)