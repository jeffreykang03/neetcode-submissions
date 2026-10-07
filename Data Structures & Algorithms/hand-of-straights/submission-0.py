class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        freq = defaultdict(int)
        for i in hand:
            freq[i] += 1
        freq = dict(sorted(freq.items()))
        while freq:
            ind = list(freq)[0]
            for i in range(groupSize):
                cur = ind + i
                if cur not in freq.keys():
                    return False
                freq[cur] -= 1
                if freq[cur] == 0:
                    freq.pop(cur)
        return True


