class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        bools = []
        m = max(candies)
        for i in range(len(candies)):
            bools.append(candies[i] + extraCandies >= m)
        return bools