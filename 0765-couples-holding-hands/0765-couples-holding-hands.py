class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        posTable = {}

        for i in range(len(row)):
            posTable[row[i]] = i
        
        swaps = 0

        for i in range(0, len(row), 2):
            partner = row[i] ^ 1

            if row[i + 1] != partner:
                stranger = row[i + 1]
                partner_pos = posTable[partner]

                row[i + 1], row[partner_pos] = partner, stranger
                posTable[partner] = i + 1
                posTable[stranger] = partner_pos

                swaps += 1

        return swaps 