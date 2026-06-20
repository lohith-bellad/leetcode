class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """
        def justify(word: str, count: int, last_line: bool) -> str:
            w = word.split(' ')

            if len(w) == 1 or last_line:
                extra = count - len(word)
                output = word + ' ' * extra
                return output

            extra = count - len(word)
            space_cnt = [0 for i in range(len(w) - 1)]

            while extra > 0:
                for i in range(len(space_cnt)):
                    space_cnt[i] += 1
                    extra -= 1
                    
                    if extra == 0:
                        break
            
            output = []
            s_ind = 0
            for word in w:
                if s_ind < len(space_cnt):
                    output += word + ' ' * (space_cnt[s_ind] + 1)
                else:
                    output += word
                s_ind += 1

            return "".join(output)
        
        ind = 0
        output = []
        while ind < len(words):
            res = ""
            while ind < len(words) and (len(res) + len(words[ind])) <= maxWidth:
                res += words[ind] + " "
                ind += 1

            temp = res[:-1] if res.endswith(' ') else res
            if ind > len(words) - 1:
                output.append(justify(temp, maxWidth, True))
            else:
                output.append(justify(temp, maxWidth, False))

        return output
        """
        def formatLast(s: str):
            words = s.split(" ")
            res = ""

            for word in words:
                if word:
                    res += word + " "

            res = res[:len(res) - 1]
            
            while len(res) < maxWidth:
                res += " "
            
            return res

        def fill(words):
            res = ""
            if len(words) == 1:
                res = words[0]
            
                while len(res) < maxWidth:
                    res += " "
                
                return res

            s = 0
            spaces_needed = len(words) - 1
            for word in words:
                s += len(word)
            s += spaces_needed

            extra_spaces = maxWidth - s
            spaces = [1 for i in range(spaces_needed)]

            ind = 0
            while extra_spaces > 0:
                spaces[ind % len(spaces)] += 1
                extra_spaces -= 1
                ind += 1
            
            for i in range(len(words)):
                res += words[i]
                if i < len(spaces):
                    res += ' ' * spaces[i]
            
            return res
        
        ind = 0
        output = []
        
        while ind < len(words):
            cur_line = []
            cursor = 0

            while ind < len(words) and (len(words[ind]) + cursor) <= maxWidth:
                cursor += len(words[ind]) + 1
                cur_line.append(words[ind])
                ind += 1
            
            line = fill(cur_line)
            output.append(line)

        output.append(formatLast(output.pop()))

        return output     