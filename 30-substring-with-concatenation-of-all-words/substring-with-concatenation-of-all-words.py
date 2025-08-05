class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        # base case
        if not s or not words:
            return []

        word_length = len(words[0])              
        total_length = word_length * len(words)  
        word_count = Counter(words)               
        n = len(s)
        result = []

        for start in range(word_length):
            left = start                          
            curr_count = Counter()                

            for right in range(start, n - word_length + 1, word_length):
                word = s[right:right + word_length]

                if word in word_count:
                    curr_count[word] += 1

                    while curr_count[word] > word_count[word]:
                        left_word = s[left:left + word_length]
                        curr_count[left_word] -= 1
                        left += word_length

                    if right - left + word_length == total_length:
                        result.append(left)

                else:
                    curr_count.clear()
                    left = right + word_length

        return result
