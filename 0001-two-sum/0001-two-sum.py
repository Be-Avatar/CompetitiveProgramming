class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i < j:
                    store.append(i)
                    store.append(j)
        return store