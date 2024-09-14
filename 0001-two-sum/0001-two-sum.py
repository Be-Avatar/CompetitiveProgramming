class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = []
        for i in nums:
            if target - i in nums and nums.index(i) < nums.index(target - i) and target - i != i:
                store.append(nums.index(i))
                store.append(nums.index(target - i))
                break
            elif target - i in nums and nums.count(i) > 1 and target - i == i:
                store.append(nums.index(i))
                store.append(nums.index(i, nums.index(i) + 1))
                break
        return store