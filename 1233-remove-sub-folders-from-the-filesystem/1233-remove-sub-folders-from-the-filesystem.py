class Filesystem:
    def __init__(self):
        self.folders = {}
        self.end = False
    
    def insert(self, path: List[str]):
        cur_node = self

        for f in path:
            if f not in cur_node.folders:
                cur_node.folders[f] = Filesystem()
            cur_node = cur_node.folders[f]
            if cur_node.end:
                return

        cur_node.end = True


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        def dfs(cur_node, path):
            if cur_node.end:
                output.append(path.copy())
                return
            
            for name, p in cur_node.folders.items():
                path.append(name)
                dfs(p, path)
                path.pop()
            
            return

        fs = Filesystem()

        for path in folder:
            p = path.split("/")
            fs.insert(p[1:])
        
        output = []
        dfs(fs, [])
        dirs = []

        for out in output:
            res = "/".join(out)
            res = "/" + res
            dirs.append(res)

        return dirs