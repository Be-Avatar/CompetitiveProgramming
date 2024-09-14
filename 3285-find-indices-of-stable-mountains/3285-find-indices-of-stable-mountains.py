class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        store = []
        for i in range(len(height) - 1):
            if height[i] > threshold:
                store.append(i + 1)
        return store