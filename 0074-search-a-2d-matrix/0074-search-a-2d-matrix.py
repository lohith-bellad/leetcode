class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        start = 0
        end = (len(matrix) * len(matrix[0])) - 1

        while start <= end:
            mid = start + (end - start) // 2

            row = mid // len(matrix[0])
            col = mid % len(matrix[0])

            if matrix[row][col] == target:
                return True
            
            if matrix[row][col] > target:
                end = mid - 1
            else:
                start = mid + 1
        
        return False
        """
        def search_row(nums, target):
            start = 0
            end = len(nums) - 1

            while start <= end:
                mid = start + (end - start) // 2

                if nums[mid] == target:
                    return True

                if nums[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1

            return False

        start = 0
        end = len(matrix) - 1

        while start < end:
            mid = start + (end - start + 1) // 2

            if matrix[mid][0] <= target:
                start = mid
            else:
                end = mid - 1

        return search_row(matrix[start], target)
