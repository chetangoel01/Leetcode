from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # is this not just the combination lock problem ?
        def getNeighbors(s, wordset, seen):
            neighborArr = []
            for i in range(26):
                for j in range(len(s)):
                    new_word = s[:j] + chr(i+97) + s[j+1:]
                    if new_word not in seen and new_word in wordset:
                        neighborArr.append(new_word)
            return neighborArr
        
        wordset = set(wordList)
        if endWord not in wordset:
            return 0
    
        queue = deque([(beginWord, 1)])
        seen = {beginWord}

        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            neighbors = getNeighbors(word, wordset, seen)
            for nbr in neighbors:
                seen.add(nbr)
                queue.append((nbr, length + 1))

        return 0