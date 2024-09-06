class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        arr = sentence.split()
        new_arr = []
        for i in range(len(arr)):
            if arr[i][0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                arr[i] = arr[i] + 'maa' + i*'a'
            else:
                arr[i] = arr[i][1:] + arr[i][0] + 'maa' + i*'a'
        return ' '.join(arr)