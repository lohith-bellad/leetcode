"""
126. Word Ladder II
Hard

A transformation sequence from word beginWord to word endWord using a dictionary
wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
    * Every adjacent pair of words differs by a single letter.
    * Every si for 1 <= i <= k is in wordList. Note that beginWord does not need
      to be in wordList.
    * sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return all
the shortest transformation sequences from beginWord to endWord, or an empty
list if no such sequence exists. Each sequence should be returned as a list of
the words [beginWord, s1, s2, ..., sk].


Example 1:
    Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
    Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
    Explanation: There are 2 shortest transformation sequences:
        "hit" -> "hot" -> "dot" -> "dog" -> "cog"
        "hit" -> "hot" -> "lot" -> "log" -> "cog"

Example 2:
    Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
    Output: []
    Explanation: The endWord "cog" is not in wordList, therefore there is no
        valid transformation sequence.


Constraints:
    * 1 <= beginWord.length <= 5
    * endWord.length == beginWord.length
    * 1 <= wordList.length <= 500
    * wordList[i].length == beginWord.length
    * beginWord, endWord, and wordList[i] consist of lowercase English letters.
    * beginWord != endWord
    * All the words in wordList are unique.
    * The sum of all shortest transformation sequences does not exceed 10^5.

"""

from typing import List
from collections import deque


class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        def dfs(word, path):
            if word == beginWord:
                new_path = path.copy()
                new_path.reverse()
                self.output.append(new_path)
                return

            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + c + word[i + 1 :]
                    if (
                        new_word in word_levels
                        and word_levels[new_word] + 1 == word_levels[word]
                    ):
                        path.append(new_word)
                        dfs(new_word, path)
                        path.pop()

        queue = deque()
        queue.append((beginWord, 1))
        word_levels = {beginWord: 1}
        wordSet = set(wordList)

        while queue:
            cur_word, steps = queue.popleft()

            if cur_word == endWord:
                break

            for i in range(len(cur_word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    new_word = cur_word[:i] + c + cur_word[i + 1 :]
                    if new_word in wordSet and new_word not in word_levels:
                        queue.append((new_word, steps + 1))
                        word_levels[new_word] = steps + 1

        if endWord not in word_levels:
            return []

        self.output = []
        dfs(endWord, [endWord])
        return self.output
