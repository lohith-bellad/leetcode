class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        w_ptr = 0
        a_ptr = 0

        while w_ptr < len(word):
            num = 0
            while a_ptr < len(abbr) and abbr[a_ptr].isdigit():
                num = (num * 10) + int(abbr[a_ptr])
                a_ptr += 1
        
            if num > 0:
                w_ptr += num
        
            if w_ptr >= len(word) and a_ptr >= len(abbr):
                return True
        
            if word[w_ptr] != abbr[a_ptr]:
                return False
        
            w_ptr += 1
            a_ptr += 1
    
        return True
        """
        abbr_ind = 0
        word_ind = 0

        while abbr_ind < len(abbr):
            if abbr[abbr_ind] == "0" or word_ind >= len(word):
                return False
            
            count = 0
            while abbr_ind < len(abbr) and abbr[abbr_ind].isdigit():
                count = count * 10 + int(abbr[abbr_ind])
                abbr_ind += 1

            if count > 0:
                word_ind += count
            else:
                if word[word_ind] != abbr[abbr_ind]:
                    return False
                word_ind += 1
                abbr_ind += 1
        
        return word_ind == len(word)
        """