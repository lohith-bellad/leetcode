class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """
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
        
        word_ind = 0
        abbr_ind = 0

        while abbr_ind < len(abbr) and word_ind < len(word):
            num = 0
            while abbr_ind < len(abbr) and abbr[abbr_ind].isdigit():
                num = (num * 10) + int(abbr[abbr_ind])
                abbr_ind += 1
                if num == 0:
                    return False

            if num > 0:
                word_ind += num
            else:
                if word[word_ind] != abbr[abbr_ind]:
                    return False
                word_ind += 1
                abbr_ind += 1

        return word_ind == len(word) and abbr_ind == len(abbr)
        """
        word_ptr = 0
        abbr_ptr = 0

        while word_ptr < len(word) and abbr_ptr < len(abbr):
            jump = 0
            while abbr_ptr < len(abbr) and abbr[abbr_ptr].isdigit():
                jump = (jump * 10) + int(abbr[abbr_ptr])
                abbr_ptr += 1
                if jump == 0:
                    return False
            
            if jump > 0:
                word_ptr += jump
            else:
                if word[word_ptr] != abbr[abbr_ptr]:
                    return False

                word_ptr += 1
                abbr_ptr += 1
        
        if word_ptr != len(word) or abbr_ptr != len(abbr):
            return False
        
        return True