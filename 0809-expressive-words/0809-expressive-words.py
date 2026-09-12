class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def is_strechy(word1, word2):
            p1 = 0
            p2 = 0

            while p1 < len(word1) and p2 < len(word2):
                if word1[p1] != word2[p2]:
                    return False
                
                p1 += 1
                p2 += 1

                c1 = 1
                while p1 < len(word1) and word1[p1] == word1[p1 - 1]:
                    p1 += 1
                    c1 += 1

                c2 = 1
                while p2 < len(word2) and word2[p2] == word2[p2 - 1]:
                    p2 += 1
                    c2 += 1
        
                if c1 < 3:
                    if c1 != c2:
                        return False
                
                if c2 > c1:
                    return False
                    
            return p1 == len(word1) and p2 == len(word2)
                
        output = 0
        for word in words:
            if is_strechy(s, word):
                output += 1
        
        return output