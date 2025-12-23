"""
716. Max Stack
Hard

Design a max stack data structure that supports the stack operations and supports
finding the stack's maximum element.

Implement the MaxStack class:
    * MaxStack() Initializes the stack object.
    * void push(int x) Pushes element x onto the stack.
    * int pop() Removes the element on top of the stack and returns it.
    * int top() Gets the element on the top of the stack without removing it.
    * int peekMax() Retrieves the maximum element in the stack without removing it.
    * int popMax() Retrieves the maximum element in the stack and removes it. If
      there is more than one maximum element, only remove the top-most one.


Example 1:
    Input:
        ["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
        [[], [5], [1], [5], [], [], [], [], [], []]
    Output:
        [null, null, null, null, 5, 5, 1, 5, 1, 5]
    Explanation:
        MaxStack stk = new MaxStack();
        stk.push(5);   // [5] the top of the stack and the maximum number is 5.
        stk.push(1);   // [5, 1] the top of the stack is 1, but the maximum is 5.
        stk.push(5);   // [5, 1, 5] the top of the stack is 5, which is also the max.
        stk.top();     // return 5, [5, 1, 5] the stack did not change.
        stk.popMax();  // return 5, [5, 1] the stack is changed now, and the top is
                       // different from the max.
        stk.top();     // return 1, [5, 1] the stack did not change.
        stk.peekMax(); // return 5, [5, 1] the stack did not change.
        stk.pop();     // return 1, [5] the top of the stack and the max element
                       // is now 5.
        stk.top();     // return 5, [5] the stack did not change.


Constraints:
    * -10^7 <= x <= 10^7
    * At most 10^4 calls will be made to push, pop, top, peekMax, and popMax.
    * There will be at least one element in the stack when pop, top, peekMax,
      or popMax is called.

"""


class MaxStack:
    def __init__(self):
        self.max_heap = []
        self.stack = []
        self.removed_elems = set()
        self.ident = 0

    def push(self, x: int) -> None:
        self.stack.append((x, self.ident))
        heapq.heappush(self.max_heap, (-x, -self.ident))
        self.ident += 1
        return

    def pop(self) -> int:
        while self.stack and self.stack[-1][1] in self.removed_elems:
            self.stack.pop()

        elem, ident = self.stack.pop()
        self.removed_elems.add(ident)
        return elem

    def top(self) -> int:
        while self.stack and self.stack[-1][1] in self.removed_elems:
            self.stack.pop()

        elem, _ = self.stack[-1]
        return elem

    def peekMax(self) -> int:
        while self.max_heap and self.max_heap[0][1] in self.removed_elems:
            heapq.heappop(self.max_heap)

        return -self.max_heap[0][0]

    def popMax(self) -> int:
        while self.max_heap and self.max_heap[0][1] in self.removed_elems:
            heapq.heappop(self.max_heap)

        elem, ident = heapq.heappop(self.max_heap)
        self.removed_elems.add(-ident)

        return -elem
