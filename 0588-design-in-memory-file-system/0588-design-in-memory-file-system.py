class Trie:
    def __init__(self, name: str):
        self.children = {}
        self.name = name
        self.is_file = False
        self.contents = None

    def insert(self, path: List[str], is_dir: bool):
        cur_node = self

        for node in path:
            if node not in cur_node.children:
                cur_node.children[node] = Trie(node)
            cur_node = cur_node.children[node]

        if not is_dir:
            cur_node.is_file = True

    def get_path(self, path: List[str]) -> List[str]:
        output = []
        cur_node = self
        
        for node in path:
            if node in cur_node.children:
                cur_node = cur_node.children[node]
            else:
                return output

        if cur_node.is_file:
            output.append(cur_node.name)
        else:
            for key in sorted(cur_node.children):
                output.append(key)

        return output

    def add_file_content(self, path: List[str], content: str):
        cur_node = self
                
        for node in path:
            if node in cur_node.children:
                cur_node = cur_node.children[node]
            else:
                return

        if cur_node.is_file:
            cur_node.contents = (cur_node.contents or "") + content

        return

    def read_file_contents(self, path: List[str]) -> str:
        cur_node = self
                        
        for node in path:
            if node in cur_node.children:
                cur_node = cur_node.children[node]
            else:
                return

        if cur_node.is_file:
            return cur_node.contents

        return ""
class FileSystem:
    def __init__(self):
        self.root = Trie("")
        
    def ls(self, path: str) -> List[str]:
        elems = [p for p in path.split("/") if p]

        output = self.root.get_path(elems)

        return output

    def mkdir(self, path: str) -> None:
        elems = [p for p in path.split("/") if p]

        self.root.insert(elems, True)
        return

    def addContentToFile(self, filePath: str, content: str) -> None:
        elems = [p for p in filePath.split("/") if p]

        self.root.insert(elems, False)
        self.root.add_file_content(elems, content)

    def readContentFromFile(self, filePath: str) -> str:
        elems = [p for p in filePath.split("/") if p]

        return self.root.read_file_contents(elems)


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)