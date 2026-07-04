class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        output = []
        n = len(image)

        for r in range(n):
            image[r].reverse()
            output.append(image[r])
            for c in range(n):
                output[r][c] = output[r][c] ^ 1
        
        return output