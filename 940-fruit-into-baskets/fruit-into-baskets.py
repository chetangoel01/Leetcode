class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        i, j = 0, 0
        n = len(fruits)
        result = 0
        map_fruits = {}
        while j < n:
            if fruits[j] in map_fruits:
                map_fruits[fruits[j]] += 1
            else: map_fruits[fruits[j]] = 1
            
            if len(map_fruits) > 2:
                map_fruits[fruits[i]] = map_fruits[fruits[i]] - 1
                if map_fruits[fruits[i]] == 0:
                    map_fruits.pop(fruits[i])
                i = i + 1
            else:
                result = max(j-i+1, result)
            j = j + 1

        return result