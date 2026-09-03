class WordDictionary:
    """
    def __init__(self):
        self.end = False
        self.children = [None for i in range(26)]

    def addWord(self, word: str) -> None:
        elem = self
        for c in word:
            ind = ord(c) - ord('a')
            if elem.children[ind] == None:
                elem.children[ind] = WordDictionary()
            elem = elem.children[ind]
        
        elem.end = True
        return

    def search(self, word: str) -> bool:
        elem = self
        for i in range(len(word)):
            c = word[i]
            if c == ".":
                for child in range(26):
                    if elem.children[child] != None and elem.children[child].search(word[i+1:]):
                        return True
                return False
            else:
                ind = ord(c) - ord('a')
                if elem.children[ind] == None:
                    return False
                elem = elem.children[ind]

        return elem.end 
    """
    def __init__(self):
        self.children = {}
        self.end = False

    def addWord(self, word: str):
        cur_node = self

        for c in word:
            if c not in cur_node.children:
                cur_node.children[c] = WordDictionary()
            cur_node = cur_node.children[c]

        cur_node.end = True

    def search(self, word: str) -> bool:
        cur_node = self

        for i in range(len(word)):
            if word[i] == ".":
                for v in cur_node.children.values():
                    if v.search(word[i+1:]):
                        return True
                return False
            elif word[i] in cur_node.children:
                cur_node = cur_node.children[word[i]]
            else:
                return False

        return cur_node.end

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)