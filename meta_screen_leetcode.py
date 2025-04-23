#==============================================================================
# 1. Given a string s of '(' , ')' and lowercase English characters.
# 
# Your task is to remove the minimum number of parentheses ( '(' or ')', 
# in any positions ) so that the resulting parentheses string is valid and 
# return any valid string.
# 
# Formally, a parentheses string is valid if and only if:
# 
# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid 
# strings, or It can be written as (A), where A is a valid string.
# 
# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
#
def minimum_remove(s: str) -> str:
    if s == "":
        return s
    
    pstack = []
    output = []
    s_list = list(s)
    ind = 0

    for c in s_list:
        if c == "(":
            pstack.append(ind)
            output.append(c)
        elif c == ")":
            if not pstack:
                continue    
            pstack.pop()
            output.append(c)
        else:
            output.append(c)
        ind += 1
        
    for ind in pstack:
        output[ind] = ""
    
    return "".join(output)

#==============================================================================
# 2. Given an integer array nums and an integer k, return the kth largest 
# element in the array.
# 
# Note that it is the kth largest element in the sorted order, not the kth 
# distinct element.
# Can you solve it without sorting?
#
def find_kth_largest(nums: [int], k: int) -> int:
    heap = []
    heapq.heapify(heap)


    for num in nums:
        heapq.heappush(num)

        if len(heap) > k:
            heapq.heappop(heap)
    
    return heapq.heappop(heap)

#==============================================================================
# 3. A string can be abbreviated by replacing any number of non-adjacent, 
# non-empty substrings with their lengths. The lengths should not have leading 
# zeros. Given a string word and an abbreviation abbr, return whether the string 
# matches the given abbreviation.
# 
# A substring is a contiguous non-empty sequence of characters within a string.
# 
# For example, a string such as "substitution" could be abbreviated as 
# (but not limited to):
# "s10n" ("s ubstitutio n")
# "sub4u4" ("sub stit u tion")
# "12" ("substitution")
# "su3i1u2on" ("su bst i t u ti on")
# "substitution" (no substrings replaced)
# 
# Input: word = "internationalization", abbr = "i12iz4n"
# Output: true

def word_check(word: str, abbr: str) -> bool:
    word_ptr = 0
    abbr_ptr = 0

    while abbr_ptr < len(abbr):
        if abbr[abbr_ptr] == "0" or word_ptr >= len(word):
            return False
            
        if abbr[abbr_ptr].isdigit():
            num = 0
            while abbr_ptr < len(abbr) and abbr[abbr_ptr].isdigit():
                num = num * 10 + int(abbr[abbr_ptr])
                abbr_ptr += 1            
            word_ptr += num
        else:
            if word[word_ptr] != abbr[abbr_ptr]:
                return False
            
            word_ptr += 1
            abbr_ptr += 1

    return word_ptr == len(word)

#==============================================================================
# 4. Given a string s, return true if the s can be palindrome after deleting at 
# most one character from it.
# 
# Example 1:
# 
# Input: s = "kayadk"
# Output: true
# 
def palin_check(s: str, left: int, right: int, flag: bool) -> bool:

    if left < right:
        return palin_check(s, left + 1, right - 1, flag)
    elif flag:
        return (palin_check(s, left + 1, right, False) or 
                palin_check(s, left, right + 1, False))
    else:
        return False
    
    return True

def is_palindrome(s: str) -> bool:
    return palin_check(s, 0, len(s) -1, True)

#==============================================================================
# 5. Given the root of a binary tree, return the vertical order traversal of 
# its nodes values. (i.e., from top to bottom, column by column).
# 
# If two nodes are in the same row and column, the order should be from left 
# to right.
# 
# Input: root = [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]
# 
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def vertical_traversal(root: TreeNode) -> []:
    column_map = defaultdict(list)
    queue = deque()
    queue.append((root, 0))

    while len(queue) > 0:
        node, ind = queue.popleft()

        column_map[ind].append(node.val)

        if node.left != None:
            queue.append((node.left, ind - 1))
        
        if node.right != None:
            queue.append((node.right, ind + 1))
    
    output = []
    cols = sorted(column_map.keys())

    for col in cols:
        output.append(column_map[col])
    
    return output

#==============================================================================
# 6. There are n buildings in a line. You are given an integer array heights 
# of size n that represents the heights of the buildings in the line.
# 
# The ocean is to the right of the buildings. A building has an ocean view if 
# the building can see the ocean without obstructions. Formally, a building has 
# an ocean view if all the buildings to its right have a smaller height.
# 
# Return a list of indices (0-indexed) of buildings that have an ocean view, 
# sorted in increasing order.
# 
# Input: heights = [4,2,3,1]
# Output: [0,2,3]

def ocean_view(heights: []) -> []:
    obs_height = 0
    ind = len(heights) - 1
    good_view = []

    while ind >= 0:
        if heights[ind] > obs_height:
            good_view.append(ind)
            obs_height = heights[ind]
        ind -= 1
    
    return good_view.reverse()

def ocean_view(heights: []) -> []:
    if len(heights) == 1:
        return [0]

    left = 0
    right = len(heights) - 1
    left_max = 0
    right_max = 0
    left_view = []
    right_view = []

    while left < right:
        if heights[left] > left_max:
            left_view.append(left)
            left_max = max(left_max, heights[left])
        
        if heights[right] > right_max:
            right_view.append(right)
            right_max = max(right_max, heights[right])
        
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    right_view.reverse()
    return left_view + right_view

#==============================================================================
# 7. Given the root of a binary tree, imagine yourself standing on the right 
# side of it, return the values of the nodes you can see ordered from top 
# to bottom.
# 
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
# 
def traverse(root: TreeNode, ind: int, levels: {}):
    if root == None:
        return

    if ind == len(levels):
        levels.append(root.val)
        
    levels[ind] = root.val

    traverse(root.left, ind + 1, levels)
    traverse(root.right, ind + 1, levels)

    return

def right_view(root: TreeNode) -> []:
    levels = []
    traverse(root, 0, levels)
    return levels

#==============================================================================
# 8. You are given two integer arrays nums1 and nums2, sorted in non-decreasing 
# order, and two integers m and n, representing the number of elements in nums1 
# and nums2 respectively.
# 
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# 
def merge_array(nums1: [], nums2: [], m: int, n: int) -> []:
    p1 = m - 1
    p2 = n - 1

    for i in range(m + n - 1, -1 , -1):
        if p2 < 0:
            break

        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[i] = nums1[p1]
            p1 -= 1
        else:
            nums1[i] = nums2[p2]
            p2 -= 1
    
    return nums1

#==============================================================================
# 9. Given two nodes of a binary tree p and q, return their lowest common 
# ancestor (LCA).
# 
# Each node will have a reference to its parent node. The definition for Node 
# is below:
# 
# class Node {
#     public int val;
#     public Node left;
#     public Node right;
#     public Node parent;
# }
# According to the definition of LCA on Wikipedia: "The lowest common ancestor 
# of two nodes p and q in a tree T is the lowest node that has both p and q as 
# descendants (where we allow a node to be a
# descendant of itself)."
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# 
def find_lca(p: Node, q: Node) -> Node:
    if not p or not q:
        return None
    
    path_array = []

    while p.parent != None:
        path_array.append(p.parent.val)
        p = p.parent
    
    while q.parent != None:
        if q.parent.val in path_array:
            return q.parent
        q = q.parent
    
    return None

#==============================================================================
# 10. Given the root of a binary tree, return the length of the diameter of the 
# tree.
# 
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
# 
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def get_diameter(root: TreeNode) -> int:
    diameter = 0
    def traverse(root: TreeNode) -> int:
        if root == None:
            return 0
        
        left = traverse(root.left)
        right = traverse(root.right)

        diameter = max(diameter, left + right)

        return max(left, right) + 1
    
    traverse(root)
    return diameter

#==============================================================================
# 11. Given a string s which represents an expression, evaluate this expression 
# and return its value. The integer division should truncate toward zero.
# You may assume that the given expression is always valid. All intermediate 
# results will be in the range of [-231, 231 - 1].
# 
# Input: s = "3+2*2"
# Output: 7
# 
def calculate(s: str) -> int:
    if s == "":
        return 0
    
    cal_stack = []
    s = s + "+"
    num = 0
    res = 0
    op = "+"

    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        elif c in "+/*-":
            if op == "+":
                cal_stack.append(num)
            elif op == "-":
                cal_stack.append(-num)
            elif op == "*":
                cal_stack.append(cal_stack.pop() * num)
            else:
                cal_stack.append(int(cal_stack.pop() / num))
            num = 0
            op = c
    
    return sum(cal_stack)

#==============================================================================
# 12. You are given a nested list of integers nestedList. Each element is 
# either an integer or a listwhose elements may also be integers or other 
# lists.
# 
# The depth of an integer is the number of lists that it is inside of. For 
# example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to 
# its depth.
# 
# Return the sum of each integer in nestedList multiplied by its depth.
# 
# Input: nestedList = [[1,1],2,[1,1]]
# Output: 10
#         
# nestedList = [3, [1, 2], 4, [[5], 6]]
# queue = [1, 2, [5], 6]
# depth = 1, 2, 3
# 
# total_sum = 3 + 4
# 
# BFS
def nested_sum(nestedList: []) -> int:
    queue = deque(nestedList)
    depth = 1
    total_sum = 0

    while len(queue) > 0:
        for i in range(len(queue)):
            elem = queue.popleft()

            if elem.isInteger():
                total_sum += depth * elem.getInteger()
            else:
                for i in elem.getList():
                    queue.append(i)
        
        depth += 1
    
    return total_sum

#DFS
def traverse(elem: [], depth: int) -> int:
    cur_sum = 0

    for val in elem:
        if val.isInteger():
            cur_sum += depth * val.getInteger()
        else:
            cur_sum += traverse(val.getList(), depth + 1)
    
    return cur_sum

def nested_sum_dfs(nestedList: []) -> int:
    return traverse(nestedList, 1)

#==============================================================================
# 13. Given an array of integers nums and an integer k, return the total number 
# of subarrays whose sum equals to k.
# 
# A subarray is a contiguous non-empty sequence of elements within an array.
# 
# Input: nums = [1,1,1], k = 2
# Output: 2
# 
# #Brute force way, O(n*n)
def subarray_count(nums: [], k: int) -> int:
    count = 0    
    size = 1

    while size <= len(nums):
        start = 0
        end = size
        cur_sum = sum(nums[:size])
        
        while end < len(nums):
            cur_sum -= nums[start]
            cur_sum += nums[end]

            if cur_sum == k:
                count += 1
            
            end += 1
            start += 1
        
        size += 1
    
    return count

def subarray_count(nums: [], k: int) -> int:
    count = 0
    prefix_map = {0: 1}
    cur_sum = 0

    for i in range(len(nums)):
        cur_sum += nums[i]
        search = cur_sum - k

        if search in prefix_map:
            count += prefix_map[search]
        
        prefix_map[cur_sum] = prefix_map.get(cur_sum, 0) + 1

    return count

#==============================================================================
# 14.  Given an array of intervals where intervals[i] = [starti, endi], merge 
# all overlapping intervals, and return an array of the non-overlapping 
# intervals that cover all the intervals in the input.
# 
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# 
def merge_intervals(intervals: []) -> []:
    if len(intervals) == 0:
        return intervals

    #sort the input list based on start time
    intervals.sort(key = lambda x: x[0])

    interval_stack = [intervals[0]]

    for i in range(1, len(intervals)):
        # get the prev interval
        prev_start, prev_end = interval_stack.pop()

        #get current interval
        cur_start, cur_end = intervals[i]
        
        # 1. merge if overlap
        if prev_start <= cur_start <= prev_end:
            new_start = min(prev_start, cur_start)
            new_end = max(cur_end, prev_end)
            interval_stack.append([new_start, new_end])
        # 2. add as new interval if no overlap
        else:
            interval_stack.append([prev_start, prev_end])
            interval_stack.append([cur_start, cur_end])
    
    return interval_stack

#==============================================================================
# 15. Given a binary tree, find the lowest common ancestor (LCA) of two given 
# nodes in the tree.
# 
# According to the definition of LCA on Wikipedia: “The lowest common ancestor 
# is defined between two nodes p and q as the lowest node in T that has both p 
# and q as descendants (where we allow a
# node to be a descendant of itself).”
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# 
def find_lca(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if root == None or root == p or root == q:
        return root

    left = find_lca(root.left, p, q)
    right = find_lca(root.right, p, q)

    if left != None and right != None:
        return root
    
    if left:
        return left

    return right

#==============================================================================
# 16. A phrase is a palindrome if, after converting all uppercase letters into 
# lowercase letters and removing all non-alphanumeric characters, it reads the 
# same forward and backward. Alphanumeric characters include letters and 
# numbers.
# 
# Given a string s, return true if it is a palindrome, or false otherwise.
# 
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# 
def is_plindrome(s: str) -> bool:
    if s == "":
        return True
    
    left = 0
    right = len(s) - 1

    while left < right:
        while left < len(s) - 1 and not s[left].isalnum():
            left += 1
        
        while right >= 0 and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1
    
    return True

#==============================================================================
# 17. Given an n x n binary matrix grid, return the length of the shortest 
# clear path in the matrix. If there is no clear path, return -1.
# 
# A clear path in a binary matrix is a path from the top-left cell 
# (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
# 
# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they 
# are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.
# 
# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4
# 
def find_path(grid: []) -> int:
    size = len(grid)

    dirs = [[-1,-1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    queue = deque()
    path_count = 0

    queue.append((0, 0, 1))
    grid[0][0] = 1

    while len(queue) > 0:
        r, c, pc = queue.popleft()

        if r == size - 1 and c == size - 1:
            return pc

        for d in range(size(dirs)):
            nr = r + d[0]
            nc = c + d[1]

            if 0 <= nr < size and 0 <= nc < size and grid[nr][nc] == 0:
                queue.append((nr, nc, pc + 1))
                grid[nr][nc] = 1

    return -1

#==============================================================================
# 18. You are given a 0-indexed array of positive integers w where w[i] 
# describes the weight of the ith index.
# 
# You need to implement the function pickIndex(), which randomly picks an index 
# in the range [0, w.length - 1] (inclusive) and returns it. The probability of 
# picking an index i is w[i] / sum(w).
# 
# Example:
# weights = [1, 3, 4, 2]
# total = 10
# 
# probs = [1/10, 3/10, 4/10, 2/10]
# 
# prefix_sum = [1, 4, 8, 10]
# rand_num = 7
# 
# mid = 1, 4 < 7
#
class weight_index:
    def __init__(self, w: []):
        self.weights = w
        self.prefix_sum = []
        total = 0

        for i in range(len(self.weights)):
            total += self.weights[i]
            self.prefix_sum.append(total)
    
    def pickIndex(self) -> int:
        rand_num = self.prefix_sum[-1] * random.random()

        start = 0
        end = len(self.weights) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if rand_num < self.prefix_sum[mid]:
                end = mid - 1
            else:
                start = mid + 1
        
        return start
    
#==============================================================================
# 19. Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
# 
# Input: x = 2.00000, n = 10
# Output: 1024.00000
# 
# Input: x = 2.00000, n = -2
# Output: 0.25000
# 
def pow(x: float, n: int) -> float:
    if n == 0:
        return x
    
    if n < 0:
        num = 1.0 / x
        n = -n
    else:
        num = x

    res = 1.0
    while n > 0:
        if n % 2 == 1:
            res *= num
            n = n - 1
        num *= num
        n = n // 2
    
    return res

#==============================================================================
# 20. Given a stream of integers and a window size, calculate the moving 
# average of all integers in the sliding window.
# Implement the MovingAverage class:
#
#  MovingAverage(int size) Initializes the object with the size of the window 
#  size.
#  double next(int val) Returns the moving average of the last size values of 
#  the stream.

# Input
# ["MovingAverage", "next", "next", "next", "next"]
# [[3], [1], [10], [3], [5]]
# Output
# [null, 1.0, 5.5, 4.66667, 6.0]

class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.nums = []

    def next(self, val: int) -> float:
        self.nums.append(val)

        if len(self.nums) > self.size:
            self.nums = self.nums[1:]

        return (1.0 * sum(self.nums))/len(self.nums)

#==============================================================================
# 21. Given an integer array nums and an integer k, return the k most frequent 
# elements. You may return the answer in any order.
# 
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# 
def get_frequent(nums: [], k: int) -> []:
    count_map = {}

    for num in nums:
        count_map[num] = count_map.get(num, 0) + 1
    
    top_elems = sorted(count_map.values(), reverse = True)
    top_elems = top_elems[:k]

    output = []
    for k, val in count_map.items():
        if val in top_elems:
            output.append(k)
    
    return output

#==============================================================================
# 22. Given an array of integers nums and an integer target, return indices of 
# the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may 
# not use the same element twice.
# You can return the answer in any order.

# example: nums = [2, 4, 1, 5, 6] target = 11
# {2: 0, 4: 1, 1: 2, 5: 3}

def two_sum(nums: [], target: int) -> []:
    index_map = {}

    for i in range(len(nums)):
        key = target - nums[i]
        if key in index_map:
            return [inder_map[key], i]
        index_map[nums[i]] = i
    
    return []

#==============================================================================
# 23. Design a data structure that follows the constraints of a Least Recently 
# Used (LRU) cache.
# 
# Implement the LRUCache class:
# 
#     LRUCache(int capacity) Initialize the LRU cache with positive size 
#     capacity.
#     int get(int key) Return the value of the key if the key exists, otherwise 
#     return -1.
#     void put(int key, int value) Update the value of the key if the key exists. 
#     Otherwise, add the key-value pair to the cache. If the number of keys 
#     exceeds the capacity from this operation, evict the least recently used 
#     key.
# The functions get and put must each run in O(1) average time complexity.
# 
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]
# 
class Node:
    def __init__(self, val: int, key: int):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.hashmap = {}
        self.head.next = self.tail
        self.tail.prev = self.head 
    
    def remove_node(self, node: Node):
        cur_prev = node.prev
        cur_next = node.next
        cur_prev.next = cur_next
        cur_next.prev = cur_prev

    def add_node(self, node: Node):
        head_next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = head_next
        head.next.prev = node

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.remove_node(self.hashmap[key][1])
            self.add_node(self.hashmap[key][1])
            return self.hashmap[key][0]
        
        return -1

    def put(self, key: int, value: int):
        if key in self.hashmap:
            self.remove_node(self.hashmap[key][1])
        
        new_node = Node(val, key)
        self.hashmap[key] = (value, new_node)
        self.add_node(new_node)

        if len(self.hashmap) > self.capacity:
            to_be_deleted_node = self.tail.prev
            self.remove_node(to_be_deleted_node)
            del self.hashmap[to_be_deleted_node.key]

#==============================================================================
# 24. Given an array of integers nums sorted in non-decreasing order, find the 
# starting and ending position of a given target value.
# 
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.
# 
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# 
def binary_search(nums: [], target: int, start: int, end: int, find_first) -> int:
    idx = -1

    while start <= end:
        mid = start + (end - start) // 2

        if nums[mid] == target:
            idx = mid
            if find_first:
                end = mid - 1
            else:
                start = mid + 1
        
        if nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    
    return idx

def get_indices(nums: [], target: int) -> []:
    
    start = binary_search(nums, target, 0, len(nums) - 1, True)
    end = binary_search(nums, target, 0, len(nums) - 1, False)

    return [start, end]

#==============================================================================
# 25. You are given the root of a binary tree containing digits from 0 to 9
# only.Each root-to-leaf path in the tree represents a number.
# Return the total sum of all root-to-leaf numbers. Test cases are generated so 
# that the answer will fit in a 32-bit integer.
# A leaf node is a node with no children.
#
# Input: root = [1,2,3]
# Output: 25
#
#        1
#    2       3
#
def sum_root_leaf(root: TreeNode) -> int:
    def dfs(root: TreeNode, num: int):
        if root == None:
            return
    
        num = (num * 10) + root.val

        if root.left == None and root.right == None:
            total += num

        if root.left != None:
            dfs(root, num, total)
    
        if root.right != None:
            dfs(root, num, total)
    
        return

    total = 0
    dfs(root, 0)
    return total

#==============================================================================
# 26.  A linked list of length n is given such that each node contains an 
# additional random pointer,  which could point to any node in the list, or 
# null.
# 
# Construct a deep copy of the list. The deep copy should consist of exactly n 
# brand new nodes, where each new node has its value set to the value of its 
# corresponding original node. Both the next and random pointer of the new nodes 
# should point to new nodes in the copied list such that the pointers in the 
# original list and copied list represent the same list state. None of the 
# pointers in the new list should point to nodes in the original list.
# 
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
# 
# 7 --> 13 --> 11 --> 10 --> 1
# N     7      1      11     7
# 
class ListNode:
    def __init__(self, val: int, n = None, random = None):
        self.val = val
        self.next = n
        self.random = random

    def deep_copy(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        
        node_map = {}
        dummy = ListNode(-1)
        prev = dummy

        cur_node = head
        while cur_node != None:
            new_node = ListNode(cur_node.val, cur_node.next)
            prev.next = new_node
            node_map[cur_node] = new_node

            cur_node = cur_node.next
            prev = new_node
        
        cur_old_node = head
        cur_new_node = dummy.next

        while cur_old_node != None:
            if cur_old_node.random != None:
                cur_new_node.random = node_map[cur_old_node.random]
            
            cur_old_node = cur_old_node.next
            new_old_node = new_old_node.next
        
        return dummy.next
    
#==============================================================================
# 27. Given two sparse vectors, compute their dot product.
# 
# Implement class SparseVector:
# 
#     SparseVector(nums) Initializes the object with the vector nums
#     dotProduct(vec) Compute the dot product between the instance of 
#     SparseVector and vec
# 
# A sparse vector is a vector that has mostly zero values, you should store the 
# sparse vector efficiently and compute the dot product between two SparseVector.
# 
# Follow up: What if only one of the vectors is sparse?
# 
# Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
# Output: 8
# Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
# v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8
# 
# nums1 = 0, 3, 4
# nums2 = 1, 3
# 
# nums1:
# [(0, 1), (3, 2), (4, 3)]
# nums2:
# [(1, 3), (3, 4)]
# 
class SparseVector:
    def __init__(self, nums: []):
        self.nums = []

        for i, val in enumerate(nums):
            if val != 0:
                self.nums.append((i, val))
    
    def binary_find(nums_arr: [], target: int) -> int:
        left = 0
        right = len(nums_arr) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums_arr[mid][0] == target:
                return nums_arr[mid][1]
            
            elif nums_arr[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return 0 

    def dotProduct(self, sv: 'SparseVector') -> int:
        res = 0

        if len(self.nums) < len(sv.nums):
            for i in range(len(self.nums)):
                res += self.nums[i][1] * binary_find(sv.nums, self.nums[i][0])
        else:
            for i in range(len(sv.nums)):
                res += sv.nums[i][1] * binary_find(self.nums, sv.nums[i][0])

        return res

#==============================================================================
# 28.  Given the root of a binary tree, the value of a target node target, and 
# an integer k, return  an array of the values of all nodes that have a distance 
# k from the target node.
# 
# You can return the answer in any order.

# target = 3, k = 2
#           2
#         3   4
#       1  5
#     7  8
# output = [4, 7, 8]
# 
# 1 - 3, 7, 8 
# 2 - 3, 4
# 3 - 2, 1, 5
# 4 - 1
# 5 - 3
# 7 - 1
# 8 - 1
#
def tree_nodes(root: TreeNode, target: int, k: int) -> []:
    def dfs(node: int, visited: {}, depth: int):
        if node in visited:
            return

        if depth == k:
            self.output.append(node)
        
        visited.add(node)

        for neighbor in adj_map[node]:
            dfs(neighbor, visited, depth + 1)
        
        return
    
    self.output = []
    adj_map = defaultdict(list)
    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()

        if node.left != None:
            adj_map[node.val].append(node.left.val)
            adj_map[node.left.val].append(node.val)
            queue.append(node.left)
        
        if node.right != None:
            adj_map[node.val].append(node.right.val)
            adj_map[node.right.val].append(node.val)
            queue.append(node.right)
        
    depth = 0
    visited = set()
    visited.add(target)

    if k == depth:
        return [target]

    for neighbor in adj_map[target]:
        dfs(neighbor, visited, depth)
    
    return self.output

#==============================================================================
# 29.The next permutation of an array of integers is the next lexicographically 
# greater permutation of its integer. More formally, if all the permutations of 
# the array are sorted in one container according to their lexicographical 
# order, then the next permutation of that array is the permutation that 
# follows it in the sorted container. If such arrangement is not possible, the 
# array must be rearranged as the lowest possible order (i.e., sorted in 
# ascending order).
# 
# Input: nums = [1,2,3]
# Output: [1,3,2]
# 
# Example:
# nums = [4, 3, 5, 1, 3, 3, 2]
# [4, 3, 5, 2, 3, 3, 1]
# [4, 3, 5, 2, 1, 3, 3]
# 
# [4, 3, 5, 1, 3, 2, 3]
# 
def next_permutation(nums: int):
    pivot = -1

    for i in range(len(nums) - 2, -1 , -1):
        cur_num = nums[i]
        next_num = nums[i+1]

        if cur_num < next_num:
            pivot = i
            break
    
    if pivot == -1:
        nums.reverse()
        return
    
    i = len(nums) - 1
    while i > pivot and nums[i] <= nums[pivot]:
        i -= 1
    
    nums[pivot], nums[i] = nums[i], nums[pivot]

    nums[pivot+1:] = reversed(nums[pivot+1:])

    return

#==============================================================================
# 30. You are given an absolute path for a Unix-style file system, which always 
# begins with a slash '/'. Your task is to transform this absolute path into its 
# simplified canonical path.
# 
# The path must start with a single slash '/'.
# Directories within the path must be separated by exactly one slash '/'.
# The path must not end with a slash '/', unless it is the root directory.
# The path must not have any single or double periods ('.' and '..') used to 
# denote current or parent directories.
# Return the simplified canonical path.
# 
# Input: path = "/home/"
# 
# Output: "/home"
# 
# Explanation:
# 
# The trailing slash should be removed.
# 
# entries: ".", ".."
# 
def reduce_path(path: str) -> str:
    input_list = path.split("/")
    path_stack = []

    for entry in input_list:
        if entry == ".":
            continue
        if entry == "..":
            if len(path_stack) > 0:
                path_stack.pop()
            continue
        path_stack.append(entry)
    
    output = "/"
    for i in range(len(path_stack) - 1):
        output += path_stack[i] + "/"
    
    if path_stack:
        output += path_stack[-1]

    return output

#==============================================================================
# 31. Given an array arr of positive integers sorted in a strictly increasing 
# order, and an integer k.
# Return the kth positive integer that is missing from this array.

# example:
# Input: arr = [2,3,4,7,11], k = 5
# Output: 9

def missing(nums: [], k: int) -> int:
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if nums[mid] - mid - 1 > k:
            end = mid - 1
        else:
            start = mid + 1
    
    return start + k

#==============================================================================
# 32. You are given an array prices where prices[i] is the price of a given 
# stock on the ith day. You want to maximize your profit by choosing a single 
# day to buy one stock and choosing a different day in the future to sell that 
# stock.
# 
# Return the maximum profit you can achieve from this transaction. If you cannot 
# achieve any profit, return 0.
#
# Input: prices = [7,1,5,3,6,4]
# Output: 5
#
def min_price(prices: []) -> int:
    max_profit = 0

    buy_price = prices[0]
    for i in range(1, len(prices)):
        if prices[i] < buy_price:
           buy_price = prices[i]
        max_profit = max(max_profit, prices[i] - buy_price)
    
    return max_profit

#==============================================================================
# 33. A peak element is an element that is strictly greater than its neighbors.
# 
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index 
# number 2.
# 
def find_peak(nums: [int]) -> int:
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if ((mid == 0 or nums[mid] > nums[mid - 1]) and 
            (mid == len(nums) - 1 or nums[mid] > nums[mid + 1])):
            return mid
        
        if nums[mid] < nums[mid - 1]:
            end = mid - 1
        
        if nums[mid] < nums[mid + 1]:
            start = mid + 1

#==============================================================================
# 34. A parentheses string is valid if and only if:
# 
#     It is the empty string,
#     It can be written as AB (A concatenated with B), where A and B are valid 
#     strings, or
#     It can be written as (A), where A is a valid string.
# You are given a parentheses string s. In one move, you can insert a 
# parenthesis at any position of the string.
# 
# Return the minimum number of moves required to make s valid.
#
def valid_parentheses(s: str) -> int:
    p_stack = []
    result = 0

    for i in range(len(s)):
        if s[i] in "(":
            p_stack.append("(")
        else:
            if p_stack:
                p_stack.pop()
            else:
                result += 1
    
    result += len(p_stack)

    return result

#==============================================================================
# 35. Given the root node of a binary search tree and two integers low and high, 
# return the sum of values of all nodes with a value in the inclusive range 
# [low, high].
# 
# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
# 
def range_sum(root: TreeNode, low: int, high: int) -> int:
    if root == None:
        return 0
    
    if low <= root.val <= high:
        return (root.val + 
                range_sum(root.left, low, high) + 
                range_sum(root.right, low, high))
    
    if root.val < low:
        return range_sum(root.right, low, high)
    
    if root.val > high:
        return range_sum(root.left, low, high)
    
#==============================================================================
# 36.  Given an array of points where points[i] = [xi, yi] represents a point 
# on the X-Y plane and an integer k, return the k closest points to the origin 
# (0, 0).
# 
# The distance between two points on the X-Y plane is the Euclidean distance 
# (i.e., √(x1 - x2)2 + (y1 - y2)2).
# 
# You may return the answer in any order. The answer is guaranteed to be unique 
# (except for the order that it is in).
# 
# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
# 
def closest_origin(points: [], k: int) -> []:
    if k > len(points):
        return []
    
    dist_heap = []

    for point in points:
        x, y = point
        dist = (x**2 + y**2)**0.5

        if len(heap) == k:
            heapq.heappushpop(dist_heap, (-dist, x, y))
        else:
            heapq.heappush(dist_heap, (-dist, x, y))

    output = []
    idx = 0

    while idx < k:
        dist, x, y = heapq.heappop(dist_heap)
        output.append([x, y])
        idx += 1
    
    return output

#==============================================================================
# 37. You are given two strings order and s. All the characters of order are 
# unique and were sorted in some custom order previously.
# 
# Permute the characters of s so that they match the order that order was sorted. 
# More specifically, if a character x occurs before a character y in order, then 
# x should occur before y in the permuted string.
# 
# Return any permutation of s that satisfies this property.
# 
# Input: order = "cba", s = "abcd"
# Output: "cbad"
# Explanation: "a", "b", "c" appear in order, so the order of "a", "b", "c" 
# should be "c", "b", and "a".
# 
def customSortString(self, order: str, s: str) -> str:
    bitmap = [0 for i in range(26)]

    for c in s:
         bitmap[ord(c) - ord('a')] += 1
        
    output = ""
    for c in order:
        offset = ord(c) - ord('a')
        if bitmap[offset] > 0:
            output += c * bitmap[offset]
            bitmap[offset] = 0
        
    for i in range(26):
        if bitmap[i] > 0:
            output += chr(i + ord('a')) * bitmap[i]
        
    return output

#==============================================================================
# 38. You are given two lists of closed intervals, firstList and secondList, 
# where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each 
# list of intervals is pairwise disjoint and in sorted order.
# 
# Return the intersection of these two interval lists.
# 
# first_list = [[1,3], [5,6], [10,12]]
# second_list = [[2, 4], [6,7], [8,9]]
# 
def interval_intersection(first_list: [], second_list: []) -> []:
    output = []
    p1 = 0
    p2 = 0

    while p1 < len(first_list) and p2 < len(second_list):
        new_x = max(first_list[p1][0], second_list[p2][0])
        new_y = min(first_list[p1][1], second_list[p2][1])

        if new_x <= new_y:
            output.append([new_x, new_y])
        
        if new_y < second_list[p2][1]:
            p1 += 1
        else:
            p2 += 1

    return output

#==============================================================================
# 39. Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
    
def clone(node: Node) -> Node:
    if not node:
        return None
    
    queue = deque()
    node_map = {}
    queue.append(node)
    neighbor_map = defaultdict(list)

    while len(queue) > 0:
        old_node = queue.popleft()

        new_node = Node(old_node.val)
        node_map[old_node.val] = new_node

        for neighbor in old_node.neighbors:
            if neighbor.val not in node_map:
                queue.append(neighbor)

            neighbor_map[old_node.val].append(neighbor.val)
    
    for key, val in node_map.items():
        new_node = val
        new_node.neighbors = neighbor_map[key]
    
    return node_map[1]

#==============================================================================
# 40. Given an m x n matrix mat, return an array of all the elements of the 
# array in a diagonal order.
# 
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,4,7,5,3,6,8,9]
# 
# [[1,2,3],
#  [4,5,6],
#  [7,8,9]]
# 
# indices: (0, 0) -> (0, 1), (1, 0) -> (2, 0), (1, 1) (0, 2) -> (1, 2), (2, 1) -> 
# (2, 2)
# 
#  0,0 0,1 0,2 1,0 1,1 1,2 2,0 2,1 2,2
# 
def diagonal_traverse(mat: []) -> []:
   mat_map = defaultdict(list)
   row_max = len(mat)
   col_max = len(mat[0])
   for row in range(row_max):
       for col in range(col_max):
           mat_map[row + col].append(mat[row][col])
   
   indices = sorted(mat_map.keys())
   output = []
   for ind in indices:
       if ind % 2 == 0:
           mat_map[ind].reverse()
       output += mat_map[ind]
   
   return output

#==============================================================================
# 41. Given a binary array nums and an integer k, return the maximum number of 
# consecutive 1's in the array if you can flip at most k 0's.
# 
# Example:
# Input: nums: [1,1,0,0,1,0,0,1,1,0,0,0,1], k=3

def consecutive_ones(nums: [], k: int) -> int:
    max_seen = 0
    start = 0
    skip = k

    for idx in range(len(nums)):
        if nums[idx] == 0:
            skip += 1
        
        while skip > k:
            if nums[start] == 0:
                skip -= 1
            start += 1

        max_seen = max(max_seen, idx - start + 1)
    
    return max_seen

#==============================================================================
# 42. You are given an integer num. You can swap two digits at most once to get 
# the maximum valued number.
# 
# Return the maximum valued number you can get.
# 
# Input: num = 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
# 
def swap_digits(num: int) -> int:
    if num == 0:
        return num

    num_list = list(str(num))
    num_list = [int(c) for c in num_list]
    pivot = 0


    while pivot < len(num_list) - 1 and num_list[pivot] >= max(num_list[pivot + 1:]):
        pivot += 1
    
    if pivot < len(num_list) - 1:
        
        max_num =  max(num_list[pivot + 1:])
    
        swap_ind = 0
        for i in range(len(num_list)):
            if num_list[i] == max_num:
                swap_ind = i

        num_list[pivot], num_list[swap_ind] = num_list[swap_ind], num_list[pivot]

    output = 0

    for n in num_list:
        output = (output * 10) + n 
    
    return output

#==============================================================================
# 43. There are a total of numCourses courses you have to take, labeled from 0 
# to numCourses - 1. You are given an array prerequisites where 
# prerequisites[i] = [ai, bi] indicates that you must take course bi first if 
# you want to take course ai.
# 
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.
#
# Input: numCourses = 4, prerequisites = [[1,0], [2,0] [3,1]]
# Output: true
#
# 1: 0
# 2: 0
# 3: 1
#
# bi -> ai

def dfs(course: int, adj_map: {}, visited: set) -> bool:
    if not adj_map[course]:
        return True
    
    if course in visited:
        return False
    
    visited.add(course)

    for pre in adj_map[course]:
        if not dfs(pre, adj_map, visited):
            return False
    
    adj_map[course] = []
    return True


def course_schedule(numCourses: int, prerequisties: []) -> bool:
    adj_map = defaultdict(list)

    for course, prereq in prerequisites:
        adj_map[course].append(prereq)

    for i in range(numCourses):
        visited = set()
        if not dfs(i, adj_map, visited):
            return False
    
    return True

#==============================================================================
# 44.  You are given an array of strings strings, group together all strings[i] 
# that belong to the shifting sequence. You may return the answer in any order.
# 
#Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
#Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]

def is_shifted(word1: str, word2: str) -> bool:
    size = len(word1)
    diff = ord(word1[0]) - ord(word2[0])
    if diff < 0:
        diff += 26

    ind = 1
    while idx < size:
        cur_diff = ord(word1[idx]) - ord(word2[idx])

        if cur_diff != diff:
            return False
        
        idx += 1
    return True

def group_strings(strings: List[str]) -> List[List[str]]:
    hash_map = defaultdict(list)

    for word in strings:
        word_size = len(word)

        inserted = False
        for key in hash_map.keys():
            if len(key) == word_size and is_shifted(word, key):
                hash_map[key].append(word)
                inserted = True
                break

        if not inserted:
            hash_map[word].append(word)        

    output = []
    for key, val in hash_map.items():
        output.append(val)
    
    return output

#==============================================================================
# 45. Given the head of a linked list, remove the nth node from the end of the 
# list and return its head.
# 
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
#
# 1 -> 2 -> 3 -> 4 -> 5
# n = 2
# 0 <= n <= 5
# 
def remove_nth_node(head: ListNode, n: int) -> ListNode:
    total_nodes = 0
    cur_node = head

    while cur_node != None:
        cur_node = cur_node.next
        total_nodes += 1
    
    if total_nodes == 1 or n > total_nodes:
        return head
    
    cutoff_ind = total_nodes - n
    dummy = ListNode(-1)
    dummy.next = head
    cur_node = dummy

    while cutoff_ind > 0:
        cur_node = cur_node.next
        curoff_ind -= 1

    cur_node.next = cur_node.next.next

    return dummy.next

#==============================================================================
# 46.  You are given a list logs, where logs[i] represents the ith log message 
# formatted as a string "{function_id}:{"start" | "end"}:{timestamp}". For 
# example, "0:start:3" means a function call with function ID 0 started at the 
# beginning of timestamp 3, and "1:end:2" means a function call with function 
# ID 1 ended at the end of timestamp 2. Note that a function can be called 
# multiple times, possibly recursively.
# 
# Return the exclusive time of each function in an array, where the value at 
# the ith index represents the exclusive time for the function with ID i.

Example: n = 2 
logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]

def exclusive_time(n: int, logs: []) -> []:
    t_stack = []
    output = [0 for i in range(n)]

    for log in logs:
        tid, action, ttime = log
        tid = int(tid)
        ttime = int(ttime)

        if action == "start":
            t_stack.append((tid, ttime, 0))
        else:
            _, start_time, other_time = t_stack.pop()
            duration = ttime - start_time + 1 - other_time
            output[tid] = duration
            if t_stack:
                t_stack[-1][2] += duration + other_time
    
    return output

#==============================================================================
# 47. Given a string s containing just the characters '(', ')', '{', '}', 
# '[' and ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

def valid_parentheses(s: str) -> bool:
    if not s:
        return True
    
    p_stack = []

    for b in s:
        if b in "([{":
            p_stack.append()
        elif b in ")]}":
            if not p_stack:
                return False
            pair = p_stack.pop()
            if ((b == ")" and pair == "(") or 
                (b == "]" and pair == "[") or 
                (b == "}" and pair == "{")):
                continue
            return False

    if p_stack:
        return False

    return True

#==============================================================================
# 48.  Given the root of a binary tree, each node in the tree has a distinct 
# value.
# 
# After deleting all nodes with a value in to_delete, we are left with a 
# forest (a disjoint union of trees).
# 
# Return the roots of the trees in the remaining forest. You may return the 
# result in any order.
#
def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        def traverse(root: TreeNode, to_delete: []) -> TreeNode:
            if root == None:
                return None

            root.left = traverse(root.left, to_delete)
            root.right = traverse(root.right, to_delete)

            if root.val in to_delete:
                if root.left:
                    forest.append(root.left)
                if root.right:
                    forest.append(root.right)
                return None
                
            return root

        forest = []
        root = traverse(root, to_delete)
        if root:
            forest.append(root)

        return forest

#==============================================================================
# 49. Given an integer array nums and an integer k, return true if there are two 
# distinct indices i and j in the array such that nums[i] == nums[j] and 
# abs(i - j) <= k.
# 
def contains_duplicate(nums: [], k: int) -> bool:
    index_map = {}

    for i in range(len(nums)):
        if nums[i] in index_map and abs(index_map[nums[i]] - i) <= k:
                return True
        index_map[nums[i]] = i

    return False

#==============================================================================
# 50. Given a Circular Linked List node, which is sorted in non-descending 
# order, write a function to insert a value insertVal into the list such that it 
# remains a sorted circular list. The given node can be a reference to any 
# single node in the list and may not necessarily be the smallest value in the 
# circular list.
# 
# Example: [2, 3, 4] insert = 1
#
# 2 -> 3 -> 4
# |_________|
#
def list_insert(head: ListNode, val: int) -> ListNode:
    new_node = ListNode(val)

    if head == None:
        return new_node
    
    if head.next == head:
        head.next = new_node
        new_node.next = head
        return head
    
    cur_head = head
    while cur_head.next != head:
        if cur_head.val <= val <= cur_head.next.val:
            break
        
        if (cur_head.val > cur_head.next.val and 
            (cur_head.val <= val or cur_head.next.val >= val)):
            break

        cur_head = cur_head.next

    new_node.next = cur_head.next
    cur_head.next = new_node

    return head

#==============================================================================
# 51.  You are given two non-empty linked lists representing two non-negative 
# integers. The digits are stored in reverse order, and each of their nodes 
# contains a single digit. Add the two numbers and return the sum as a linked 
# list.
# 
# You may assume the two numbers do not contain any leading zero, except the 
# number 0 itself.
# 
# Example:
# l1 = 3 -> 4 -> 5
# l2 = 7 -> 1 -> 8
# c  = 0
# r  = 0 -> 6 -> 3 -> 1
# 
class ListNode:
    def __init__(self, num: int):
        self.val = val
        self.next = None

def add_lists(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = Listnode(-1)
    prev = dummy
    carry = 0

    while l1 != None or l2 != None:
        n1 = 0
        n2 = 0
        if l1 != None:
            n1 = l1.val
        if l2 != None:
            n2 = l2.val

        tot = n1 + n2 + carry
        carry = tot // 10
        tot = tot % 10
        

        prev.next = ListNode(tot)
        prev = prev.next

        if l1 != None:
            l1 = l1.next
        if l2 != None:
            l2 = l2.next
    
    if carry > 0:
        prev.next = ListNode(carry)
    
    return dummy.next

#==============================================================================
# 52. Given an integer array nums and an integer k, return true if nums has a 
# good subarray or false otherwise.
# 
# A good subarray is a subarray where:
# 
#     its length is at least two, and
#     the sum of the elements of the subarray is a multiple of k.
# 
# Note that:
# 
#     A subarray is a contiguous part of the array.
#     An integer x is a multiple of k if there exists an integer n such that 
# x = n * k. 0 is
#     always a multiple of k.
# 
# Input: nums = [23,2,4,6,7], k = 6
# Output: true
# Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
# 
# (prefix-j - prefix-i) % k = 0
# ((q1 * k + r1) - (q2 * k + r2)) % k = 0
# q1 * k - q2 * k  + r1 - r2 
# (k(q1 - q2) + (r1 - r2)) % k = 0
# q1 - q2 = 0
# (r1 - r2) % k = 0
# => r1 = r2
# 
def subarray_sum(nums: [], k: int) -> bool:
    index_map = {0: -1}
    prefix_sum = 0

    for i in range(len(nums)):
        prefix_sum += nums[i]
        prefix_mod = prefix_sum % k

        if prefix_mod not in index_map:
            index_map[prefix_mod] = i
        else:
            if i - index_map[prefix_mod] >= 2:
                return True
    
    return False

#==============================================================================
#53. Given the root of a binary search tree and a target value, return the 
#value in the BST that is closest to the target. If there are multiple answers,
#print the smallest.
#
# Example:
# input = [4, 2, 5, 1, 3] target = 3.71
#
#            4
#        2       5
#    1       3
#
def closest_search(root: TreeNode, target: float) -> int:
    closet_seen = float('inf')
    res = 0

    while root:
        diff = abs(root.val - target)
        if diff < closet_seen or (diff == closet_seen and root.val < result):
            closet_seen = diff
            res = root.val
        
        if root.val > target:
            root = root.left
        else:
            root = root.right
    
    return res

#==============================================================================
# 54. Given two non-negative integers, num1 and num2 represented as string, 
# return the sum of num1 and num2 as a string.
#
# You must solve the problem without using any built-in library for handling large integers 
# (such as BigInteger). You must also not convert the inputs to integers directly.
#
# num1 = "128"
# num2 = "56"
#
# 8 + 6 = 4 carry = 1
# 2 + 5 + 1 = 8 carry = 0
#
def add_strings(num1: str, num2: str) -> (str, int):
    p1 = len(num1) - 1
    p2 = len(num2) - 1
    res = []
    carry = 0

    while p1 >= 0 or p2 >= 0:
        n1 = 0
        n2 = 0
        if p1 >= 0:
            n1 = int(num1[p1])
        if p2 >= 0:
            n2 = int(num2[p2])

        total = n1 + n2 + carry
        carry = total // 10
        total = total % 10

        res.append(str(total))
        p1 -= 1
        p2 -= 1
    
    if carry > 0:
        c = carry
    else:
        c = "0"
    
    res.reverse()
    return ("".join(res), c)

# Variant:
# --------
# num1 = 123.45
# num2 = 23

def add_strings_dec(num1: str, num2: str) -> str:
    dpart1 = "0"
    dpart2 = "0"
    parts = num1.split(".")
    ipart1 = parts[0]
    if len(parts) == 2 and parts[1] != "":
        dpart1 = parts[1]
    
    parts = num2.split(".")
    ipart2 = parts[0]
    if len(parts) == 2 and parts[1] != "":
        dpart2 = parts[1]
    
    ires, c_part = add_strings(ipart1, ipart2)
    if c_part > 0:
        ires = str(c_part) + ires

    dres, c_part = add_strings(dpart1, dpart2)
    if c_part > 0:
        ires, c_part = add_strings(ires, str(c_part))
        if c_part > 0:
              ires = str(c_part) + ires

    if dres == "0":
        return ires
    else:
        return ires + "." + dres
#==============================================================================
# 55. Given the root of a binary tree, determine if it is a complete binary 
# tree.
# 
# In a complete binary tree, every level, except possibly the last, is 
# completely filled, and all nodes in the last level are as far left as 
# possible. It can have between 1 and 2h nodes inclusive at the last level h.
# 
# example:
#           2
#       3       5
#     4   7   8
# 
class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

def check_tree(root: TreeNode) -> bool:
    if not root:
        return True
    
    queue = deque([root])

    while queue and queue[0]:
        node = queue.popleft()
        queue.append(node.left)
        queue.append(node.right)
    
    while queue and not queue[0]:
        queue.popleft()
    
    return len(queue) == 0

#==============================================================================
# 56. Implement the myAtoi(string s) function, which converts a string to a 
# 32-bit signed integer.
# 
# The algorithm for myAtoi(string s) is as follows:
# 
# 1. Whitespace: Ignore any leading whitespace (" ").
# 2. Signedness: Determine the sign by checking if the next character is '-' 
# or '+', assuming positivity if neither present.
# 3. Conversion: Read the integer by skipping leading zeros until a non-digit 
# character is encountered or the end of the string is reached. If no digits 
# were read, then the result is 0.
# 4. Rounding: If the integer is out of the 32-bit signed integer range 
# [-231, 231 - 1], then round the integer to remain in the range. Specifically, 
# integers less than -231 should be rounded to -231, and integers greater than 
# 231 - 1 should be rounded to 231 - 1.
# 
# Return the integer as the final result.
#
def myAtoi(self, s: str) -> int:
        num = 0
        is_neg = False

        idx = 0
        while idx < len(s) and s[idx] == " ":
            idx += 1

        if idx < len(s) and s[idx] in "+-":
            if s[idx] == "-":
                is_neg = True
            idx += 1

        while idx < len(s):
            if s[idx].isdigit():
                n = int(s[idx])
                num = (num * 10) + n
                idx += 1
            elif num == 0:
                return 0
            else:
                break
            
        if is_neg:
            num = -num

        if num < (2**31)*(-1):
            return (2**31)*-1

        if num > 2**31 - 1:
            return 2**31 - 1
        
        return num

#==============================================================================
# 57. Given an integer array nums, return all the triplets [nums[i], nums[j], 
# nums[k]] such that i != j, i != k, and j != k, and 
# nums[i] + nums[j] + nums[k] == 0.
# 
# Notice that the solution set must not contain duplicate triplets.
# 
# Example:
# nums = [1, 2, -1, 0, 3, -3]
# left_hash = 1: 1
# right_hash = 1: 1, 2: 1, 0: 1, 3: 1, -3: 1, -1: 0
# 
def three_sum(nums: []) -> []:
    output = set()
    left_hash = {}
    right_hash = {}
    nums.sort()

    left_hash[nums[0]] = 1
    for i in range(1, len(nums)):
        right_hash[nums[i]] = right_hash.get(nums[i], 0) + 1
    
    for i in range(1, len(nums)):
        right_hash[nums[i]] -= 1
        if right_hash[nums[i]] == 0:
            del right_hash[nums[i]]
        
        for key in left_hash.keys():
            search = -(key + nums[i])
            if search in right_hash:
                output.add((key, nums[i], search))
        
        left_hash[nums[i]] = left_hash.get(nums[i], 0) + 1

    return list(output)

#==============================================================================
# 58.  You need to construct a binary tree from a string consisting of 
# parenthesis and integers.
# 
# The whole input represents a binary tree. It contains an integer followed 
# by zero, one or two pairs of parenthesis. The integer represents the root's 
# value and a pair of parenthesis contains a child binary tree with the same 
# structure.
# 
# You always start to construct the left child node of the parent first if 
# it exists.
# 
# Example:
# s = 5(2(3)(4))(8()(7))
#         5
#     2       8
#   3   4   N   7
# 
class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

def traverse(s: str, ind: int) -> TreeNode:
    start = ind
    while start < len(s) and (s[start].isdigit() or s[start] == "-"):
        start += 1
    
    val = s[ind: start]
    new_node = TreeNode(val)

    if start < len(s) and s[start] == "(":
        new_node.left, start = traverse(s, start + 1)
    
    if start < len(s) and s[start] == "(":
        new_node.right, start = traverse(s, start + 1)
    
    return new_node, start + 1

def build_tree(s: str) -> TreeNode:
    if not s:
        return None
    
    root, _ = traverse(s, 0)
    return root

#==============================================================================
# 59. Given an integer array nums sorted in non-decreasing order, remove the 
# duplicates in-place such that each unique element appears only once. The 
# relative order of the elements should be kept the same. Then return the 
# number of unique elements in nums.
# 
# example: [1, 1, 1, 2, 3, 3, 4]
# output: [1, 2, 3, 4, _, _, _]
# 
def remove_dups(nums: []):
    left = 0

    right = 1
    while right < len(nums):
        while right < len(nums) and nums[right] == nums[right - 1]:
            right += 1
        
        if right == len(nums):
            break

        left += 1
        nums[left] = nums[right]

        right += 1
    
    return left + 1

#==============================================================================
# 60. Given an m x n integer matrix, if an element is 0, set its entire row and 
# column to 0's.
# #
# #You must do it in place.
# #
# #example:
# #[[1, 2, 3],
# # [0, 4, 5],
# # [7, 8, 0],
# #]
#
def set_zeroes(matrix:[]):
    row_max = len(matrix)
    col_max = len(matrix[0]) 

    rows = set()
    cols = set()

    for i in range(row_max):
        for j in range(col_max):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)
    
    for row in rows:
        for j in range(col_max):
            matrix[row][j] = 0
    
    for col in cols:
        for i in range(row_max):
            matrix[i][col] = 0
    
    return
#==============================================================================
# 61.  You are given a string s consisting of lowercase English letters. 
# A duplicate removal consists of choosing two adjacent and equal letters and 
# removing them.
# 
# We repeatedly make duplicate removals on s until we no longer can.
# Return the final string after all such duplicate removals have been made. 
# It can be proven that the answer is unique.
# 
# Example:
# s = "aabddbcaefe"
# 
def remove_adj(s: str) -> str:
    adj_stack = []

    for i in range(len(s)):
        if len(adj_stack) == 0:
            adj_stack.append(s[i])
        else:
            if adj_stack[-1] == s[i]:
                adj_stack.pop()
            else:
                adj_stack.append(s[i])
    
    return "".join(adj_stack)

#==============================================================================
# 62. There is a car with capacity empty seats. The vehicle only drives east 
# (i.e., it cannot turn around and drive west).
# 
# You are given the integer capacity and an array trips where 
# trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has 
# numPassengersi passengers and the locations to pick them up and 
# drop them off are fromi and toi respectively. The locations are given as 
# the number of kilometers due east from the car's initial location.
# 
# Return true if it is possible to pick up and drop off all passengers for 
# all the given trips, or false otherwise.
#
# Example:
# capacity = 3
# trips = [[2, 1, 2], [1, 2, 5], [2, 4, 7]]
# 
# time: 1 2 3 4 5 6 7 8 9 10
# cap:  2 1 1 3 2 2 2 0 0 0 
# 
def car_pooling(capacity: int, trips: [[]]) -> bool:
    t_stack = []

    for trip in trips:
        cap, start, end = trip
        t_stack.append((start, cap))
        t_stack.append((end, -cap))

    t_stack.sort()

    for _, pcount in t_stack:
        cur_capacity += pcount
        if cur_capacity > capacity:
            return False

    return True

#==============================================================================
# 63. Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in 
# place.
# 
# You can think of the left and right pointers as synonymous to the predecessor 
# and successor 
# pointers in a doubly-linked list. For a circular doubly linked list, the 
# predecessor of the first element is the last element, and the successor of 
# the last element is the first element.

# We want to do the transformation in place. After the transformation, the 
# left pointer of the tree node should point to its predecessor, and the right 
# pointer should point to its successor. You should return the pointer to the 
# smallest element of the linked list.

# Example:
# Input: root = [4,2,5,1,3]
# Output = [1, 2, 3, 4, 5]

def tree_to_list(root: TreeNode) -> TreeNode:
    head = None
    tail = None

    def traverse(root: TreeNode):
        if root == None:
            return

        traverse(root.left)

        if not tail:
            head = root
        else:
            tail.right = root
            root.left = tail
        
        tail = root

        traverse(root.right)
        return
    
    traverse(root)
    head.prev = tail
    tail.next = head

    return head

#==============================================================================
# 64. There is an integer array nums sorted in ascending order 
# (with distinct values).
# Given the array nums after the possible rotation and an integer target, 
# return the index of target if it is in nums, or -1 if it is not in nums.
# 
# You must write an algorithm with O(log n) runtime complexity.
#
# Example:
# nums = [4,5,6,7,0,1,2], target = 5

def find_valley(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] > nums[-1]:
                start = mid + 1
            else:
                end = mid - 1
        return start

def search(self, nums: List[int], target: int) -> int:
    if len(nums) <= 1:
        if len(nums) == 1 and nums[0] == target:
            return 0
        return -1

    start = 0
    end = len(nums) - 1
    offset = self.find_valley(nums)

    while start <= end:
        mid = start + (end - start) // 2
        act_mid = (mid + offset) % len(nums)
        if nums[act_mid] == target:
            return act_mid
        if nums[act_mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1

#==============================================================================
# 65. Given an integer array nums, find the subarray with the largest sum, and 
# return its sum.
# 
# Example:
# 
# nums = [1, 2, -1, 3, -6, 4, 1, -2]
# 
# 1+2 = 3
# 3 - 1 = 2
# 2 + 3 = 5
# 5 - 6 = -1, 0
# -6 + 4 = -2
# 4 + 1 = 5
# 5 - 2 = 3
# 
def max_subarray(nums: []) -> int:
    max_sum = nums[0]
    cur_sum = 0

    for num in nums:
        cur_sum = max(cur_sum, 0) + num
        max_sum = max(max_sum, cur_sum)

#==============================================================================
# 66. You are climbing a staircase. It takes n steps to reach the top.
# 
# Each time you can either climb 1 or 2 steps. In how many distinct ways can 
# you climb to the top?
#
def climb(n: int, cache: []) -> int:
    if n <= 2:
        return n
    
    if cache[n] != -1:
        return cache[n]

    cache[n] = climb(n-1, cache) + climb(n-2, cache)
    return cache[n]

def climb_count(n: int) -> int:
    cache = [-1 for i in range(n)]

    return climb(n, cache)

#==============================================================================
# 67. You have a long flowerbed in which some of the plots are planted, and 
# some are not. However, flowers cannot be planted in adjacent plots.
# 
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty 
# and 1 means not empty, and an integer n, return true if n new flowers can be 
# planted in the flowerbed without violating the no-adjacent-flowers rule and 
# false otherwise.
# 
# Example:
# 
# flowerbed = [1, 0, 0, 0, 1, 0], n = 3
# 
def plant(flowerbed: [], n: int) -> bool:
    if n == 0:
        return True
    
    i = 0
    while i < len(flowerbed):
        if flowerbed[i] == 1:
            i += 1
            continue
        
        if ((i == 0 or flowerbed[i - 1] == 0) and
            (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)):
            n -= 1
            i += 2
            if n == 0:
                return True
        else:
            i += 1
    
    return False

#==============================================================================
# 68.  Given the availability time slots arrays slots1 and slots2 of two people 
# and a meeting duration duration, return the earliest time slot that works for 
# both of them and is of duration duration.
# 
# If there is no common time slot that satisfies the requirements, return an 
# empty array.
# 
# The format of a time slot is an array of two elements [start, end] 
# representing an inclusive time range from start to end.
#
# Example:
# slots1 = [[2,5], [8,10], [20, 30]]
# slots2 = [[1,3], [5,10], [15, 35]] 
# duration = 5
# 
def get_slot(slots1: [], slots2: []) -> []:
    slots1.sort()
    slots2.sort()
    p1 = 0
    p2 = 0

    while p1 < len(slots) and p2 < len(slots2):
        new_x = max(slots1[p1][0], slots2[p2][0])
        new_y = min(slots1[p1][1], slots2[p2][1])

        if new_x <= new_y and new_y - new_x >= duration:
            return [new_x, new_x + duration]
        
        if new_y < slots2[p2][1]:
            p1 += 1
        else:
            p2 += 1
    
    return []

#==============================================================================
# 69. You are given an inclusive range [lower, upper] and a sorted unique 
# integer array nums, where all elements are within the inclusive range.
# 
# A number x is considered missing if x is in the range [lower, upper] 
# and x is not in nums.
# 
# Example: lower = 0 and upper = 20
# nums: [0, 2, 3, 4, 8, 10]
# 
# ranges= [[1, 1], [5, 7], [9,9]]
# 
def missing_ranges(nums: [], lower: int, upper: int) -> []:
    if lower == upper:
        return []

    ranges = []

    for num in nums:
        if num > lower:
            ranges.append([lower, num - 1])
            lower = num + 1
        else:
            lower = num + 1
    
    if lower <= upper:
        ranges.append(lower, upper)

    return ranges

#==============================================================================
# 70.  Implement the BSTIterator class that represents an iterator over the 
# in-order traversal of a binary search tree (BST):
# 
# - BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. 
# The root of the BST is given as part of the constructor.
# The pointer should be initialized to a non-existent number smaller than any 
# element in the BST.
# - boolean hasNext() Returns true if there exists a number in the traversal
#  to the right of the pointer, otherwise returns false. 
# - int next() Moves the pointer to the right, then returns the 
# number at the pointer.

class BSTIterator:
    def __init__(self, root: TreeNode):
        self.nums = []
        self.cur_idx = -1
        def inorder(root: TreeNode):
            if root == None:
                return
            
            inorder(root.left)
            self.nums.append(root.val)
            inorder(root.right)

            return
        inorder(root)
    
    def hasNext(self) -> bool:
        if self.cur_idx + 1 < len(self.nums):
            return True
        return False
    
    def next(self) -> bool:
        self.cur_idx += 1
        return self.nums[self.cur_idx]
    
#==============================================================================
# 71. Given an m x n 2D binary grid grid which represents a map of '1's (land) 
# and '0's (water), return the number of islands.
# 
# An island is surrounded by water and is formed by connecting adjacent lands 
# horizontally or vertically. You may assume all four edges of the grid are all 
# surrounded by water.
#
def num_of_islands(grid:[[]]) -> int:
    row_max = len(grid)
    col_max = len(grid[0])

    dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    queue = deque()
    seq_num = 1

    for i in range(row_max):
        for j in range(col_max):
            if grid[i][j] == "1":
                queue.append((i, j))
                seq_num += 1
                grid[i][j] = str(seq_num)

            
            while queue:
                row, col = queue.popleft()

                for d in dirs:
                    nrow = row + d[0]
                    ncol = col + d[1]

                    if 0 <= nrow < row_max and 0 <= ncol < col_max and grid[nrow][ncol] == "1":
                        queue.append((nrow, ncol))
                        grid[nrow][ncol] = seq_num
    
    return seq_num - 1

#==============================================================================
# 72. Given an array of integers nums, calculate the pivot index of this array.
# 
# The pivot index is the index where the sum of all the numbers strictly to 
# the left of the index is equal to the sum of all the numbers strictly to 
# the index's right.
# 
# If the index is on the left edge of the array, then the left sum is 0 because 
# there are no elements to the left. This also applies to the right edge of the 
# array.
# 
# Return the leftmost pivot index. If no such index exists, return -1.
#
def pivot_index(nums: []) -> int:
    left_sum = 0
    right_sum = sum(nums)

    for i in range(len(nums)):
        right_sum -= nums[i]

        if left_sum == right_sum:
            return i
        
        left_sum += nums[i]
    
    return -1

#==============================================================================
# 73. Given a binary search tree (BST), find the lowest common ancestor (LCA) 
# node of two given nodes in the BST.
# 
# According to the definition of LCA on Wikipedia: “The lowest common ancestor 
# is defined between two nodes p and q as the lowest node in T that has both p 
# and q as descendants (where we allow a node to be a descendant of itself).”

def traverse(root, p, q):
    if not root:
        return None

    if p.val <= root.val <= q.val:
        return root
    if root.val > q.val:
        return traverse(root.left, p, q)
    else:
        return traverse(root.right, p, q)

def lca_bst(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if p.val > q.val:
        p, q = q, p
    
    return traverse(root, p, q)

#==============================================================================
# 74.  Given an array of meeting time intervals intervals where 
# intervals[i] = [starti, endi], return the minimum number of conference rooms 
# required.
# 
# Example:
# intervals: [[2, 5], [4, 10], [15, 20]]
# 
# rooms = [[2, 20], [4, 10]]
# 
def meeting_rooms2(intervals: []) -> int:
    intervals.sort()
    rooms = [intervals[0]]

    for i in range(1, len(intervals)):
        cur_start, cur_end = intervals[i]

        room_found = False
        for i in range(len(rooms)):
            room_start, room_end = rooms[i]

            if room_start < cur_start < room_end:
                continue
            
            room_found = True
            rooms[i][1] = room_end
            break
        
        if not room_found:
            rooms.append(intervals[i])
    
    return len(rooms)

#==============================================================================
# 75.  Given a string s, you can transform every letter individually to be 
# lowercase or uppercase to create another string.
# 
# Return a list of all possible strings we could create. Return the output 
# in any order.
# 
# Example:
# s = "a1b2"
# A1b2 A1B2 a1B2 a1b2
# 
# [A1b2] [a1B2] [a1b2] [A1B2]
# 
def permute(s: str) -> str:
    def traverse(s: str, ind: int) -> []:
        if ind == len(s):
            return []
        
        words = traverse(s, ind + 1)
        new_words = []

        for word in words:
            if s[ind].isdigit():
                new_words.append(s[ind] + word)
            else:
                clower = s[ind].lower()
                cupper = s[ind].upper()
                new_words.append(clower + word)
                new_words.append(cupper + word)
        
        return new_words

    return traverse(s, 0)

#==============================================================================
# 76. Given the root of a binary tree, return the number of nodes where the 
# value of the node is equal to the average of the values in its subtree.
# 
# Note:
# 
# The average of n elements is the sum of the n elements divided by n and 
# rounded down to the nearest integer. A subtree of root is a tree consisting 
# of root and all of its descendants.
# 
# Example:
#             4
#         8       5
#       1   2       6
# 
def tree_average(root: TreeNode) -> int:
    def traverse(root: TreeNode) -> (int, int):
        if root == None:
            return 0, 0
        
        left_sum, left_count = traverse(root.left)
        right_sum, right_count = traverse(root.right)

        cur_sum = left_sum + right_sum + root.val
        cur_count = left_count + right_count + 1

        if cur_sum // cur_count == root.val:
            count += 1
        
        return cur_sum, cur_count

    count = 0
    traverse(root)
    return count

#==============================================================================
# 77.  You are given an integer array ribbons, where ribbons[i] represents 
# the length of the ith ribbon, and an integer k. You may cut any of the ribbons 
# into any number of segments of positive integer lengths, or perform no cuts at 
# all.
# 
# For example, if you have a ribbon of length 4, you can:
# Keep the ribbon of length 4,
# Cut it into one ribbon of length 3 and one ribbon of length 1,
# Cut it into two ribbons of length 2,
# Cut it into one ribbon of length 2 and two ribbons of length 1, or
# Cut it into four ribbons of length 1.
# Your task is to determine the maximum length of ribbon, x, that allows you 
# to cut at least k ribbons, each of length x. You can discard any leftover 
# ribbon from the cuts. If it is impossible to cut k ribbons of the same 
# length, return 0.
# 
# Example:
# ribbons = [3, 4, 5]
# 
def check_cut(ribbons: [], k: int, size: int) -> bool:
    count = 0

    for ribbon in ribbons:
        count += ribbon // size
        if count == k:
            return True
    
    return False

def cur_ribbons(ribbons: [], k: int) -> int:
    start = 1
    end = max(ribbons)

    while start <= end:
        mid = start + (end - start) // 2

        if check_cut(ribbons, k, mid):
            start = mid + 1
        else:
            end = mid - 1
    
    return end

#==============================================================================
# 78.  Given a string s, return the longest palindromic substring in s.
# 
def longest_palin_substring(s: str) -> str:
    start = -1
    end = -1
    max_len = 0
    size = len(s)
    for i in range(size):
        left = i
        right = i
        while 0 <= left < size and 0 <= right < size and s[left] == s[right]:
            cur_len = right - left + 1
            if cur_len > max_len:
                start = left
                end = right
                max_len = cur_len
            left -= 1
            right += 1
        
        left = i
        right = i + 1
        while 0 <= left < size and 0 <= right < size and s[left] == s[right]:
            cur_len = right - left + 1
            if cur_len > max_len:
                start = left
                end = right
                max_len = cur_len
            left -= 1
            right += 1

    return s[start: end + 1]

#==============================================================================
# 79. You are given the heads of two sorted linked lists list1 and list2.
# 
# Merge the two lists into one sorted list. The list should be made by 
# splicing together the nodes 
# of the first two lists.
# 
# Return the head of the merged linked list.
# 
# Example:
# list1 = 1 -> 3 -> 5
# list2 = 1 -> 6 
# 
# dummy -> 1 -> 1 -> 3 -> 5 -> 6
# 
def sort_list(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode(-1)
    prev = dummy

    while list1 and list2:
        if list1.val < list2.val:
            prev.next = list1.val
            list1 = list1.next
        else:
            prev.next = list2.val
            list2 = list2.val
        
        prev = prev.next
    
    if list1:
        prev.next = list1
    
    elif list2:
        prev.next = list2

    return dummy.next

#==============================================================================
# 80.  Given two binary strings a and b, return their sum as a binary string.
# 
# Example:
# a = 101
# b = 11
# 1000
# 
def binary_sum(a: str, b: str) -> str:
    p1 = len(a) - 1
    p2 = len(b) - 1
    carry = 0
    result = ""

    while p1 >=0 or p2 >= 0:
        n1 = 0
        n2 = 0
        if p1 >= 0:
            n1 = int(s[p1])
        if p2 >= 0:
            n2 = int(s[p2])
        
        if n1 == 1 and n2 == 1:
            if carry:
                result += "1"
            else:
                result += "0"
        elif n1 ^ n2:
            if carry:
                result += "0"
            else:
                result += "1"
                carry = 0
        else:
            if carry:
                result += "1"
                carry = 0
            else:
                result += "0"
        i -= 1
        j -= 1

    if carry:
        result += "1"
    
    return result[::-1]

#==============================================================================
# 81.  You are given an m x n integer matrix matrix with the following two 
# properties:
# 
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the 
# previous row.Given an integer target, return true if target is in matrix 
# or false otherwise.
# 
# You must write a solution in O(log(m * n)) time complexity.
# 
# Example: target = 11
# 1 5 6
# 7 11 20
# 25 26 30
# 
def matrix_find(matrix: [], target: int) -> bool:
    start = 0
    row_size = len(matrix)
    col_size = len(matrix[0])
    end = (row_size * col_size) - 1

    while start <= end:
        mid = start + (end - start) // 2

        row_idx = mid // row_size
        col_idx = mid % col_size

        if matrix[row_idx][col_idx] == target:
            return True
        
        if matrix[row_idx][col_idx] > target:
            end = mid - 1
        else:
            start = mid + 1
    
    return False

#==============================================================================
# 82.  You are given a perfect binary tree where all leaves are on the 
# same level, and every parent has two children. The binary tree has the 
# following definition:
# 
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is 
# no next right node, the next pointer should be set to NULL.
# 
# Initially, all next pointers are set to NULL.
# 
# Example:
#         5
#     3       4
#   1   2   6   7
# 
# level 2: 3 ---> 4
# level 3: 1 --> 2 ---> 6 ----> 7
# 
def point_right(root: TreeNode):
    def traverse(root: TreeNode, level_ptr: [], ind: int):
        if root == None:
            return None
        
        if ind == len(level_ptr):
            level_ptr.append(root)
        else:
            level_ptr[ind].next = root
            level_ptr[ind] = root
        
        traverse(root.left, level_ptr, ind + 1)
        traverse(root.right, level_ptr, ind + 1)

        return
    
    levels = []
    traverse(root, levels, 0)
    return root

#==============================================================================
# 83.  You are given an integer array nums consisting of n elements, and an 
# integer k.
# 
# Find a contiguous subarray whose length is equal to k that has the 
# maximum average value and return this value. Any answer with a calculation 
# error less than 10-5 will be accepted.
# 
# Example:
# nums = [3, 4, -2, 4, 1], k = 2
# 
def array_avg(nums: [], k: int) -> float:
    if len(nums) < k:
        return 0
    
    cur_sum = 0
    max_avg = 0

    for i in range(k):
        cur_sum += nums[i]
    
    max_avg = max(max_avg, cur_sum / k)

    start = 0
    end = k

    while end < len(nums):
        cur_sum -= nums[start]
        cur_sum += nums[end]

        max_avg = max(max_avg, cur_sum / k)

        start += 1
        end += 1
    
    return max_avg

#==============================================================================
# 84. Given a string s, return the number of palindromic substrings in it.
# 
# A string is a palindrome when it reads the same backward as forward.
# 
# A substring is a contiguous sequence of characters within the string.
# 
# Example:
# s = "abc"
# output = 3
# 
def palindrome_count(s: str) -> int:
    size = len(s)
    count = 0

    for i in range(size):
        left = i
        right = i

        while 0 <= left < size and 0 <= right < size and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        
        left = i
        right = i + 1

        while 0 <= left < size and 0 <= right < size and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
    
    return count

#==============================================================================
# 85. Given a 0-indexed integer array nums of length n and an integer k, 
# return the number of pairs (i, j) where 0 <= i < j < n, such that 
# nums[i] == nums[j] and (i * j) is divisible by k.
# 
def countPairs(self, nums: List[int], k: int) -> int:
    index_hash = defaultdict(list)
    count = 0
    for i in range(len(nums)):
        if nums[i] not in index_hash:
            index_hash[nums[i]].append(i)
        else:
            indices = index_hash[nums[i]]
            for index in indices:
                if (index * i) % k == 0:
                    count += 1
            index_hash[nums[i]].append(i)
    
    return count

#==============================================================================
# 86. Given a string num which represents an integer, return true if num is a 
# strobogrammatic number.
# 
# A strobogrammatic number is a number that looks the same when rotated 180 
# degrees (looked at upside down).
# 
# Example:
# s = "96"
# 
def strobogrammatic(s: str) -> bool:
    matches = {'0': '0', '6': '9', '1': '1', '8': '8', '9': '6'}

    start = 0
    end = len(s) - 1

    while start <= end:
        if s[end] in matches and s[start] == matches[s[end]]:
            start += 1
            end -= 1
        else:
            return False
    
    return True

#==============================================================================
# 87.  Given an integer n, return all the strobogrammatic numbers that are of 
# length n. You may return the answer in any order.
# 
# A strobogrammatic number is a number that looks the same when rotated 180 
# degrees (looked at upside down).
# 
def strobogrammatic_build(n: int) -> []:
    matches = {'0': '0', '6': '9', '1': '1', '8': '8', '9': '6'}

    def traverse(ind: int) -> []:
        if ind == 0:
            return []
        if ind == 1:
            return ['0', '1', '8']
        
        res = traverse(n - 2)

        temp = []
        for r in res:
            for k, v in matches.items():
                if ind == n and k == '0':
                    continue 
                temp.append(k + res + v)
            
        return temp
    
    return traverse(n)

#==============================================================================
# 88.  Given an m x n matrix, return true if the matrix is Toeplitz. 
# Otherwise, return false.
# 
# A matrix is Toeplitz if every diagonal from top-left to bottom-right has 
# the same elements.
# 
# Example:
# 1 2 3 4
# 5 1 2 3
# 6 5 1 2
# 
# (r - c) = 0 => (0, 0) (1, 1) (2, 2)
# (r - c) = 1 => (1, 0) (2, 1)
# (r - c) = 2 => (2, 0)
# (r - c) = -1 => (0, 1) (1, 2) (2, 3)
# (r - c) = -2 => (0, 2) (1, 3)
# (r - c) = -3 => (0, 3)
# 
def toeplitz(matrix: []) -> bool:
    mat_map = {}
    row_max = len(matrix)
    col_max = len(matrix[0])

    for i in range(row_max):
        for j in range(col_max):
            if (i - j) not in mat_map:
                mat_map[i - j] = matrix[i][j]
            else:
                if matrix[i][j] != mat_map[i - j]:
                    return False
    
    return True

#==============================================================================
# 89. Write a function to find the longest common prefix string amongst an 
# array of strings. If there is no common prefix, return an empty string "".
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

def longest_prefix(strs: [str]) -> str:
    longest = strs[0]

    for i in range(1, len(strs)):
        cur_word = strs[i]
        max_ind = min(len(longest), cur_word)

        ind = 0
        while ind < max_ind and longest[ind] == cur_word[ind]:
            ind += 1
        
        longest = longest[:ind]
    
    return longest

#==============================================================================
# 90. Given a string s, find the length of the longest substring without 
# duplicate characters.
# 
# Input: s = "abcabcbb"
# Output: 3
#
def longest_substring(s: str) -> int:
    index_map = {}
    start = 0
    max_len = 0

    for i in range(len(s)):
        if s[i] not in index_map:
            index_map[s[i]] = i
            max_len = max(max_len, i - start + 1)
        else:
            while s[start] != s[i]:
                del index_map[s[start]]
                start += 1
            index_map[s[i]] = i
            start += 1
    
    return max_len

#==============================================================================
# 91. You are given an n x n binary matrix grid where 1 represents land and 0 
# represents water.
# 
# An island is a 4-directionally connected group of 1's not connected to any '
# 'other 1's. There are exactly two islands in grid.
# 
# You may change 0's to 1's to connect the two islands to form one island.
# 
# Return the smallest number of 0's you must flip to connect the two islands.
# 

def shortestBridge(self, grid: List[List[int]]) -> int:
    dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    row_max = len(grid)
    col_max = len(grid[0])
    
    queue = deque()
    second_queue = deque()
    first, second = -1, -1
    found = False
    for r in range(row_max):
        for c in range(col_max):
            if grid[r][c] == 1:
                found = True
                queue.append((r, c))
                second_queue.append((r, c, 0))
                grid[r][c] = 2
                break
        if found == True:
            break
    
    while len(queue) > 0:
        row, col = queue.popleft()
                
        for d in dirs:
            nrow = row + d[0]
            ncol = col + d[1]
                    
            if 0 <= nrow < row_max and 0 <= ncol < col_max and grid[nrow][ncol] == 1:
                queue.append((nrow, ncol))
                second_queue.append((nrow, ncol, 0))
                grid[nrow][ncol] = 2
                        
    while len(second_queue) > 0:
        row, col, dist = second_queue.popleft()
        for d in dirs:
            nrow = row + d[0]
            ncol = col + d[1]
            if 0 <= nrow < row_max and 0 <= ncol < col_max:
                if grid[nrow][ncol] == 1:
                    return dist
                elif grid[nrow][ncol] == 0:
                    grid[nrow][ncol] = -1
                    second_queue.append((nrow, ncol, dist + 1))

#==============================================================================
# 92. Given an integer array nums sorted in non-decreasing order, return an 
# array of the squares of each number sorted in non-decreasing order.
#
def sortedSquares(self, nums: List[int]) -> List[int]:
        nums.sort(key = lambda x: abs(x))
        output = []

        for num in nums:
            output.append(num**2)
        
        return output

#==============================================================================
# 93. You are given two strings word1 and word2. Merge the strings by adding 
# letters in alternating order, starting with word1. If a string is longer than 
# the other, append the additional letters onto the end of the merged string.
# 
# Return the merged string.
# 
def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        for c1, c2 in zip(word1, word2):
            output += c1 + c2

        output += word1[len(output)//2:] + word2[len(output)//2:]

        return output

#==============================================================================
# 94. There are n persons on a social media website. You are given an integer 
# array ages where ages[i] is the age of the ith person.
# 
# A Person x will not send a friend request to a person y (x != y) if any of 
# the following conditions is true:
# 
# age[y] <= 0.5 * age[x] + 7
# age[y] > age[x]
# age[y] > 100 && age[x] < 100
# Otherwise, x will send a friend request to y.
# 
# Note that if x sends a request to y, y will not necessarily send a request 
# to x. Also, a person will not send a friend request to themself.
# 
# Return the total number of friend requests made.
# 
def numFriendRequests(self, ages: List[int]) -> int:
    age_cnt = [0 for i in range(121)]
    requests = 0
    for age in ages:
        age_cnt[age] += 1
    
    for i, g1_cnt in enumerate(age_cnt):
        for j, g2_cnt in enumerate(age_cnt):
            if (j <= (0.5 * i) + 7) or (j > i) or (j > 100 and i < 100):
                continue
            if i == j:
                requests -= g1_cnt
            requests += g1_cnt * g2_cnt
    return requests

#==============================================================================
# 95. You are given an n x n binary matrix grid. You are allowed to change at 
# most one 0 to be 1.
# 
# Return the size of the largest island in grid after applying this operation.
# An island is a 4-directionally connected group of 1s.
# 
# Input: grid = [[1,1],[1,0]]
# Output: 4
# 
def largestIsland(self, grid: List[List[int]]) -> int:
    size = len(grid)
    dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    queue = deque()
    island_map = {}
    island_idx = 2
    for i in range(size):
        for j in range(size):
            if grid[i][j] == 1:
                queue.append((i, j))
                grid[i][j] = island_idx
            island_size = 1
            while len(queue) > 0:
                row, col = queue.popleft()
                for d in dirs:
                    nrow = row + d[0]
                    ncol = col + d[1]
                    if (0 <= nrow < size and 
                        0 <= ncol < size and 
                        grid[nrow][ncol] == 1):
                        queue.append((nrow, ncol))
                        grid[nrow][ncol] = island_idx
                        island_size += 1
            
            island_map[island_idx] = island_size
            island_idx += 1
    max_island_size = 0
    for i in range(size):
        for j in range(size):
            if grid[i][j] == 0:
                cur_size = 0
                island_set = set()
                for d in dirs:
                    new_i = i + d[0]
                    new_j = j + d[1]
                    if (0 <= new_i < size and 
                        0 <= new_j < size and 
                        grid[new_i][new_j] != 0 and
                        grid[new_i][new_j] not in island_set):
                        island_set.add(grid[new_i][new_j])
                        cur_size += island_map[grid[new_i][new_j]]
                
                max_island_size = max(max_island_size, cur_size + 1)
    
    if max_island_size == 0:
        return island_map[2]
    
    return max_island_size

#==============================================================================
# 96. Given the root of a binary tree, calculate the vertical order traversal 
# of the binary tree.
# 
# For each node at position (row, col), its left and right children will be at 
# positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of 
# the tree is at (0, 0).
# 
# The vertical order traversal of a binary tree is a list of top-to-bottom 
# orderings for each column index starting from the leftmost column and ending
# on the rightmost column. There may be multiple nodes in the same row and same 
# column. In such a case, sort these nodes by their values.
# 
# Return the vertical order traversal of the binary tree.
# 
# Input: root = [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]
# 
def traverse(root: TreeNode, col_map: {}, row: int, col: int):
    if root == None:
        return
    
    col_map[col].append((row, root.val))

    if root.left != None:
        traverse(root.left, col_map, row + 1, col - 1)
    
    if root.right != None:
        traverse(root.right, col_map, row + 1, col + 1)
    
    return

def vertical_order_traversal(root: TreeNode) -> []:
    col_map = defaultdict(list)
    traverse(root, col_map, 0, 0)

    sorted_col_list = sorted(col_map.keys())

    for col in sorted_col_list:
        level_list = []
        elems = sorted(col_map[col], key = lambda x: x[0])
        for elem in elems:
            level_list.append(elem[1])
        
        output.append(level_list)
    
    return output

#==============================================================================
# 97. Given a string s, return whether s is a valid number. 
# 
# Cases to handle:
# 1. exponents
# 2. dot
# 3. signs

def is_valid(s: str) -> bool:
    is_number = False
    is_decimal = False
    is_exponent = False

    for i in range(len(s)):
        if s[i].isdigit():
            is_number = True
        elif s[i] in "+-":
            if i > 0 and s[i-1] != "e" and s[i-1] != "E":
                return False
        elif s[i] == ".":
            if is_exponent or is_decimal:
                return False
            is_decimal = True
        elif s[i] == "e" or s[i] == "E":
            if not is_number or is_exponent:
                return False
            is_exponent = True
            is_number = False
        else:
            return False
    
    return is_number

# Variant: no exponents
def is_valid(s: str) -> bool:
    is_number = False
    is_decimal = False

    for i in range(len(s)):
        if s[i].isdigit():
            is_number = True
        elif s[i] in "+-":
            if is_number:
                return False
        elif s[i] == ".":
            if is_decimal:
                return False
            is_decimal = True
        else:
            return False
    
    return is_number

#==============================================================================
# 98. You are given two integer arrays nums1 and nums2, sorted in 
# non-decreasing order, and two integers m and n, representing the number of 
# elements in nums1 and nums2 respectively.
# 
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# 
def merge_array(nums1: [], nums2: [], m: int, n: int) -> []:
    p1 = m - 1
    p2 = n - 1

    for i in range(m + n - 1, -1 , -1):
        if p2 < 0:
            break

        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[i] = nums1[p1]
            p1 -= 1
        else:
            nums[i] = nums2[p2]
            p2 -= 1
    
    return nums1

#==============================================================================
# 99. You are given an array of k linked-lists lists, each linked-list is 
# sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.
#
def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    dummy = ListNode(-1)
    prev = dummy
    min_heap = []

    for i in range(len(lists)):
        if lists[i] != None:
            heapq.heappush(min_heap, (lists[i].val, i, lists[i]))
        
    while len(min_heap) > 0:
        _, _, min_head = heapq.heappop(min_heap)
        prev.next = min_head
        prev = prev.next
        min_head = min_head.next
        if min_head != None:
            i += 1
            heapq.heappush(min_heap, (min_head.val, i, min_head))
        
    return dummy.next

#==============================================================================
# 100. Assume the following rules are for the tic-tac-toe game on an n x n board 
# between two players:
# 
# A move is guaranteed to be valid and is placed on an empty block.
# Once a winning condition is reached, no more moves are allowed.
# A player who succeeds in placing n of their marks in a horizontal, vertical, 
# or diagonal row wins the game. Implement the TicTacToe class:
# 
# TicTacToe(int n) Initializes the object the size of the board n.
# int move(int row, int col, int player) Indicates that the player with id 
# player plays at the cell (row, col) of the board. The move is guaranteed 
# to be a valid move, and the two players alternate in making moves. Return
# 0 if there is no winner after the move,
# 1 if player 1 is the winner after the move, or
# 2 if player 2 is the winner after the move.

class TicTacToe:
    def __init__(self, n: int):
        self.board = [[0 for i in range(n)] for i in range(n)]
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player

        for i in range(self.n):
            if self.board[row][i] != player:
                break
            if i == self.n - 1:
                return player
        
        for i in range(self.n):
            if self.board[i][col] != player:
                break
            if i == self.n - 1:
                return player

        for i in range(self.n):
            if self.board[i][i] != player:
                break
            if i == self.n - 1:
                return player

        for i in range(self.n):
            if self.board[i][self.n - 1 - i] != player:
                break
            if i == self.n - 1:
                return player

        return 0

#==============================================================================
#101. There is a ball in a maze with empty spaces (represented as 0) and walls 
#(represented as 1). The ball can go through the empty spaces by rolling up, 
#down, left or right, but it won't stop rolling until hitting a wall. When the 
#ball stops, it could choose the next direction.
#
#Given the m x n maze, the ball's start position and the destination, 
#where start = [startrow, startcol] and 
#destination = [destinationrow, destinationcol], return true if the ball 
#can stop at the destination, otherwise return false.
#
#You may assume that the borders of the maze are all walls (see examples).
# 
def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
    row_max = len(maze)
    col_max = len(maze[0])
    dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    def dfs(row: int, col: int, visited: {}) -> bool:
        if (row, col) in visited:
            return False
        if row == destination[0] and col == destination[1]:
            return True
        visited.add((row, col))
        for d in dirs:
            nrow = row
            ncol = col
            while 0 <= nrow < row_max and 0 <= ncol < col_max and maze[nrow][ncol] == 0:
                nrow += d[0]
                ncol += d[1]
            nrow -= d[0]
            ncol -= d[1]
            if dfs(nrow, ncol, visited):
                return True
        return False
    visited = set()
    return dfs(start[0], start[1], visited)

#==============================================================================
# 102. Given the head of a linked list, return the list after sorting it in 
# ascending order.
# 
def get_mid(self, root: ListNode) -> ListNode:
    slow = root
    fast = root
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(self, left: ListNode, right: ListNode) -> ListNode:
    dummy = ListNode(0)
    prev = dummy
    while left != None and right != None:
        if left.val < right.val:
            prev.next = left
            left = left.next
        else:
            prev.next = right
            right = right.next
        prev = prev.next
    
    prev.next = left if left else right
    return dummy.next
def lprint(self, root: ListNode):
    while root != None:
        print(root.val)
        root = root.next
def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head == None or head.next == None:
        return head
    
    mid = self.get_mid(head)
    second = mid.next
    mid.next = None
    left = self.sortList(head)
    right = self.sortList(second)
    temp = self.merge(left, right)
    return temp

#==============================================================================
# 103. Given an integer array nums with possible duplicates, randomly output 
# the index of a given target number. You can assume that the given target 
# number must exist in the array.
#
#Implement the Solution class:
#
#    Solution(int[] nums) Initializes the object with the array nums.
#    int pick(int target) Picks a random index i from nums where 
#    nums[i] == target. If there are
#    multiple valid i's, then each index should have an equal probability of 
#    returning.
#
# Input
# ["Solution", "pick", "pick", "pick"]
# [[[1, 2, 3, 3, 3]], [3], [1], [3]]
# Output
# [null, 4, 0, 2]
#
class Solution:
    def __init__(self, nums: []):
        self.index_map = defaultdict(list)

        for i in range(len(nums)):
            self.index_map[nums[i]].append(i)
    
    def pick(self, target: int) -> int:
        indices = self.index_map[target]

        rand_idx = random.randint(0, len(indices) - 1)
        return self.index_map[target][rand_idx]

#variant 1:
#----------
#O(n) and no extra space
#return ind of max int in the array, if multiple then each have equal probability

def reservior_sampling(nums: []) -> int:
    max_num = float('-inf')
    picked_ind = -1
    count = 0

    for i in range(len(nums)):
        if nums[i] > max_num:
            max_number = nums[i]
            count = 1
            picked_ind = i
        elif nums[i] == max_number:
            count += 1
            roll = random.randint(0, count - 1)
            if roll == 0:
                picked_ind = i

    return picked_ind

#Variant 2:
#----------
#O(n) and no extra space
#pick k numbers 

def reservior_sampling(nums: [], k: int) -> int:
    output = []

    for i in range(k):
        output.append(nums[i])
    
    for i in range(k, len(nums)):
        total = i + 1
        roll = random.randint(0, total - 1)
        if roll < k:
            output[roll] = nums[i]

    return result

#==============================================================================
# 104. Given a sorted integer array arr, two integers k and x, return the k 
# closest integers to x in the array. The result should also be sorted in 
# ascending order.
#
def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    def binary_search(start: int, end: int) -> int:
        while start <= end:
            mid = start + (end - start) // 2
            if arr[mid] < x:
                start = mid + 1
            else:
                end = mid - 1
        
        return start
    
    right = binary_search(0, len(arr) - 1)
    left = right - 1
    while k > 0:
        if left < 0:
            right += 1
        elif right >= len(arr):
            left -= 1
        elif abs(arr[left] - x) <= abs(arr[right] - x):
            left -= 1
        else:
            right += 1
        k -= 1
    return arr[left + 1:right]

#==============================================================================
# 105. Given an integer array nums, return an array answer such that answer[i] 
# is equal to the product of all the elements of nums except nums[i].
# 
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit 
# integer.
# 
# You must write an algorithm that runs in O(n) time and without using the 
# division operation.

def array_product(nums: []) -> []:
    temp = 1
    output = [1 for i in range(len(nums))]

    for i in range(1, len(nums)):
        output[i] = temp * nums[i - 1]
        temp = output[i]

    temp = nums[-1]
    for i in range(len(nums) - 2, -1, -1):
        output[i] = temp * output[i]
        temp = temp * nums[i]

    return output

#==============================================================================