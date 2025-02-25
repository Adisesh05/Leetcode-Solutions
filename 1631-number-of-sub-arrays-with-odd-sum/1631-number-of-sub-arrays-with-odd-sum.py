class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd=0
        cnt=[1, 0]
        ans=0
        for x in arr:
            odd^=(x&1)
            ans+=cnt[1-odd]
            cnt[odd]+=1
        return ans%(10**9+7)