"""
1188. Design Bounded Blocking Queue
Medium

Implement a thread-safe bounded blocking queue that has the following methods:

    * BoundedBlockingQueue(int capacity) - The constructor initializes the queue with
      a maximum capacity.

    * void enqueue(int element) - Adds an element to the front of the queue. If the
      queue is full, the calling thread is blocked until the queue is no longer full.

    * int dequeue() - Returns the element at the rear of the queue and removes it.
      If the queue is empty, the calling thread is blocked until the queue is no
      longer empty.

    * int size() - Returns the number of elements currently in the queue.

Your implementation will be tested using multiple threads at the same time. Each thread
will either be a producer thread that only makes calls to the enqueue method or a
consumer thread that only makes calls to the dequeue method. The size method will be
called after every test case.

Please do not use built-in implementations of bounded blocking queue as this will not
be accepted in an interview.


Example 1:
    Input:
        1 producer, 1 consumer
        ["BoundedBlockingQueue","enqueue","dequeue","dequeue","enqueue","enqueue","enqueue","enqueue","dequeue"]
        [[2],[1],[],[],[0],[2],[3],[4],[]]

    Output: [1,0,2,2]

    Explanation: The queue is initialized with capacity = 2. The producer thread
                 enqueues 1 first. The consumer thread dequeues 1. When dequeue is
                 called on an empty queue, the consumer is blocked until the producer
                 enqueues more elements.

Example 2:
    Input:
        3 producers, 4 consumers
        ["BoundedBlockingQueue","enqueue","enqueue","enqueue","dequeue","dequeue","dequeue","enqueue"]
        [[3],[1],[0],[2],[],[],[],[3]]

    Output: [1,0,2,1]

    Explanation: Since the number of threads for producer/consumer is greater than 1,
                 we do not know how the threads will be scheduled in the operating
                 system, even though the input seems to imply the ordering.


Constraints:
    * 1 <= capacity <= 100
    * Multiple producer and consumer threads can operate simultaneously

"""

from threading import Semaphore, Condition, Lock
from collections import deque


class BoundedBlockingQueue(object):
    def __init__(self, capacity: int):
        self.queue = deque()
        self.condition = Condition()
        self.capacity = capacity

    def enqueue(self, element: int) -> None:
        with self.condition:
            self.condition.wait_for(lambda: len(self.queue) < self.capacity)
            self.queue.append(element)
            self.condition.notify_all()

    def dequeue(self) -> int:
        with self.condition:
            self.condition.wait_for(lambda: len(self.queue) > 0)
            val = self.queue.popleft()
            self.condition.notify_all()
            return val

    def size(self) -> int:
        return len(self.queue)
