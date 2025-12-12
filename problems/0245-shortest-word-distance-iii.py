"""
245. Shortest Word Distance III
Medium

Given an array of strings wordsDict and two strings word1 and word2, return the
shortest distance between these two words in the array.

Note that word1 and word2 may be the same. It is guaranteed that they represent
two individual words in the list.


Example 1:
    Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"],
           word1 = "makes", word2 = "coding"
    Output: 1

Example 2:
    Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"],
           word1 = "makes", word2 = "makes"
    Output: 3


Constraints:
    * 1 <= wordsDict.length <= 10^5
    * 1 <= wordsDict[i].length <= 10
    * wordsDict[i] consists of lowercase English letters.
    * word1 and word2 are in wordsDict.

"""

from typing import List
from collections import defaultdict


class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        htable = defaultdict(list)

        for ind, word in enumerate(wordsDict):
            htable[word].append(ind)

        if word1 == word2:
            indices = htable[word1]

            min_dist = float("inf")
            for j in range(1, len(indices)):
                min_dist = min(min_dist, indices[j] - indices[j - 1])

            return min_dist

        arr1 = htable[word1]
        arr2 = htable[word2]

        i = 0
        j = 0

        min_dist = float("inf")
        while i < len(arr1) and j < len(arr2):
            min_dist = min(min_dist, abs(arr1[i] - arr2[j]))

            if arr1[i] < arr2[j]:
                i += 1
            else:
                j += 1

        return min_dist
