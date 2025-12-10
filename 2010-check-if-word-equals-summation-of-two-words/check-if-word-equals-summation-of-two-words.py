class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def sumWord(word):
            multiplier = 1
            wordSum = 0
            for i in range(len(word)-1, -1, -1):
                wordSum += multiplier * (ord(word[i]) - 97)
                multiplier *= 10
            return wordSum
        
        firstWordSum = sumWord(firstWord)
        secondWordSum = sumWord(secondWord)
        targetWordSum = sumWord(targetWord)

        print(firstWordSum, secondWordSum, targetWordSum)

        return firstWordSum + secondWordSum == targetWordSum