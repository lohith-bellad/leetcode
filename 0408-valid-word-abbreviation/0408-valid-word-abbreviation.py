class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        abbr_ptr = 0
        word_ptr = 0

        """
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
        while word_ptr < len(word) and abbr_ptr < len(abbr):
            if abbr[abbr_ptr] == "0":
                return False

            if abbr[abbr_ptr].isdigit():
                num = 0
                while abbr_ptr < len(abbr) and abbr[abbr_ptr].isdigit():
                    num = num * 10 + int(abbr[abbr_ptr])
                    abbr_ptr += 1
            
                word_ptr += num
                if word_ptr >= len(word) and abbr_ptr < len(abbr):
                    return False
        
            else:
                if word[word_ptr] != abbr[abbr_ptr]:
                    return False
            
                word_ptr += 1
                abbr_ptr += 1

        return word_ptr == len(word) and abbr_ptr == len(abbr)