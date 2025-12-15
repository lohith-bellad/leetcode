class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        output = []
        queue = deque()

        phoneBook = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}

        for d in digits:
            num = int(d)

            key = phoneBook[num]
            if len(queue) == 0:
                for i in range(len(key)):
                    if len(digits) == 1:
                        output.append(key[i])
                    else:
                        queue.append(key[i])
                continue

            size = len(queue)
            while size > 0:
                old = queue.popleft()
                for k in key:
                    new = old + k
                    if len(new) == len(digits):
                        output.append(new)
                    else:
                        queue.append(new)
                size -= 1

        return output
        """
        phoneBook = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }

        def traverse(ind: int, cur_word: str):
            if len(cur_word) == len(digits):
                output.append(cur_word)
                return

            for c in phoneBook[int(digits[ind])]:
                traverse(ind + 1, cur_word + c)

            return

        output = []

        if len(digits) > 0:
            traverse(0, "")

        return output
