class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        returnArr = []
        
        for word in words:
            tempWord = []
            for i in range(len(word)-1, -1, -1):
                tempWord.append(word[i])
            returnArr.append("".join(tempWord))
        
        returnStr = " ".join(returnArr)
        return returnStr