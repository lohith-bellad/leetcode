"""
244. Shortest Word Distance II
Medium

Design a data structure that will be initialized with a string array, and then it should
answer queries of the shortest distance between two different strings from the array.

Implement the WordDistance class:

    * WordDistance(String[] wordsDict) initializes the object with the strings array wordsDict.
    * int shortest(String word1, String word2) returns the shortest distance between word1 and
      word2 in the array wordsDict.


Example 1:
    Input
    ["WordDistance", "shortest", "shortest"]
    [[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]
    Output
    [null, 3, 1]

    Explanation
    WordDistance wordDistance = new WordDistance(["practice", "makes", "perfect", "coding", "makes"]);
    wordDistance.shortest("coding", "practice"); // return 3
    wordDistance.shortest("makes", "coding");    // return 1


Constraints:
    * 1 <= wordsDict.length <= 3 * 10^4
    * 1 <= wordsDict[i].length <= 10
    * wordsDict[i] consists of lowercase English letters.
    * word1 and word2 are in wordsDict.
    * word1 != word2
    * At most 5000 calls will be made to shortest.

"""


class WordDistance:
    def __init__(self, wordsDict: List[str]):
        self.index_table = defaultdict(list)

        for ind, word in enumerate(wordsDict):
            self.index_table[word].append(ind)

    def shortest(self, word1: str, word2: str) -> int:
        w1_list = self.index_table[word1]
        w2_list = self.index_table[word2]
        dist = int("inf")

        p1 = 0
        p2 = 0

        while p1 < len(w1_list) and p2 < len(w2_list):
            dist = min(dist, abs(w1_list[p1] - w2_list[p2]))

            if w1_list[p1] < w2_list[p2]:
                p1 += 1
            else:
                p2 += 1

        return dist


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
