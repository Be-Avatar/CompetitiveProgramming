class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        dictionary = {}
        for i in range(26):
            dictionary[letters[i]] = morse[i]
        
        arr = []
        for j in words:
            a = ''
            for k in j:
                a += dictionary[k]
            arr.append(a)
        return len(set(arr))