class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 27315/100, celsius * 9/5 + 320/10]