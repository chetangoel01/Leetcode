class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # this is a fixed length sliding window problem
        # keep a running count of the number of vowels in a window, return max vowels in a window
        def is_vowel(char):
            if re.match(r'[aeiouAEIOU]', char):
                return True
            return False

        vowel_count = 0
        left, right = 0, 0
        result = 0

        while right < len(s):
            if is_vowel(s[right]):
                vowel_count += 1
            if right - left + 1 > k:
                if is_vowel(s[left]):
                    vowel_count -= 1
                left += 1
            right += 1
            result = max(vowel_count, result)

        return result