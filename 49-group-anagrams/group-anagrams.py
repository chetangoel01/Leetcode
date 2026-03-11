from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we can optimize by removing the counter and implementing manually
        output = defaultdict(list)
        base = ord('a')
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - base] += 1
            key = str(count)
            output[key].append(s)

        return list(output.values())
