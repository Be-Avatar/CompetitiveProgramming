class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        store = []
        while l < r:
            while l < r:
                if nums[l] + nums[r] == target:
                    store.append(l)
                    store.append(r)
                r -= 1
            l += 1
            r = len(nums) - 1
        return store