class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        snums = sorted((v, i) for i, v in enumerate(nums))
        groups = []
        group = [snums[0]]
        for i in range(1, n):
            if snums[i][0] - snums[i - 1][0] <= limit:
                group.append(snums[i])
            else:
                groups.append(group)
                group = [snums[i]]
        groups.append(group)
        result = [0] * n
        for g in groups:
            vals = [v for v, i in g]
            indices = sorted(i for v, i in g)
            for j in range(len(indices)):
                result[indices[j]] = vals[j]
        return result