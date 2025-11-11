class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def is_matching(word1: str, word2: str) -> bool:
            size = len(word1)
            diff = ord(word1[0]) - ord(word2[0])
            if diff < 0:
                diff += 26

            idx = 1
            while idx < size:
                cur_diff = ord(word1[idx]) - ord(word2[idx])
                if cur_diff < 0:
                    cur_diff += 26
                
                if cur_diff != diff:
                    return False
                idx += 1
            return True

        mappings = defaultdict(list)

        for word in strings:
            size = len(word)
            appended = False
            if size == 1:
                for key in mappings.keys():
                    if len(key) == 1:
                        mappings[key].append(word)
                        appended = True
                if appended == False:
                    mappings[word].append(word)
                continue
            for key in mappings.keys():
                if len(key) == len(word) and is_matching(key, word):
                    mappings[key].append(word)
                    appended = True
            if appended == False:
                mappings[word].append(word)

                
        output = []
        for key, vals in mappings.items():
            output.append(vals)
        
        return output
