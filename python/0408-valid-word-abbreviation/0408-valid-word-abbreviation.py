class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
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
