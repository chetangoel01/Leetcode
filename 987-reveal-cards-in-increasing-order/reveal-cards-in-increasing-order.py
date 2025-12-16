from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        sorted_deck = sorted(deck, reverse=True)
        result = deque()
        
        for card in sorted_deck:
            if result:
                result.appendleft(result.pop())  # move bottom to top
            result.appendleft(card)  # place current card on top
        
        return list(result)
