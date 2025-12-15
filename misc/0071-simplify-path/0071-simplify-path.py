class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split("/")
        my_stack = []

        for item in path_list:
            if item == "" or item == ".":
                continue

            if item == "..":
                if len(my_stack) > 0:
                    my_stack.pop()
            else:
                my_stack.append(item)

        return "/" + "/".join(my_stack)
