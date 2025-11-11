class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_ptr = 0
        abbr_ptr = 0
    
        while abbr_ptr < len(abbr):
            if abbr[abbr_ptr] == "0" or word_ptr >= len(word):
                return False
                
            if abbr[abbr_ptr].isdigit():
                num = 0
                while abbr_ptr < len(abbr) and abbr[abbr_ptr].isdigit():
                    num = num * 10 + int(abbr[abbr_ptr])
                    abbr_ptr += 1            
                word_ptr += num
            else:
                if word[word_ptr] != abbr[abbr_ptr]:
                    return False
                
                word_ptr += 1
                abbr_ptr += 1
    
        return word_ptr == len(word)