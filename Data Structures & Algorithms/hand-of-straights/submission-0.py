from collections import defaultdict
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        numGroups = int(len(hand) / groupSize)
        if len(hand) % groupSize != 0:
            return False

        # hash map of num and count
        cardCount = dict()
        for card in hand:
            cardCount[card] = cardCount.get(card, 0) + 1
        
        for _ in range(numGroups):
            curr = min(cardCount)
            countCards = 0
            while curr in cardCount and countCards < groupSize:
                cardCount[curr] -= 1
                if cardCount[curr] == 0:
                    cardCount.pop(curr)
                curr += 1
                countCards += 1
            if countCards != groupSize:
                return False
        return True



