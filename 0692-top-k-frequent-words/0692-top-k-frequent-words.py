class RevStr:
    def __init__(self, s: str):
        self.s = s
    
    def __lt__(self, other: "RevStr") -> bool:
        return self.s > other.s

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordHeap = []
        wordMap = {}

        for word in words:
            wordMap[word] = wordMap.get(word , 0) + 1
        
        for word, count in wordMap.items():
            heapq.heappush(wordHeap, (count, RevStr(word)))

            if len(wordHeap) > k:
                heapq.heappop(wordHeap)

        output = []

        while wordHeap:
            _, word = heapq.heappop(wordHeap)
            output.append(word.s)
            
        output.reverse()
        return output

        
        