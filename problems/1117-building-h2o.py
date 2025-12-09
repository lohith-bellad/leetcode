"""
1117. Building H2O
Medium

There are two kinds of threads: oxygen and hydrogen. Your goal is to group these threads
to form water molecules.

There is a barrier where each thread has to wait until a complete molecule can be formed.
Hydrogen and oxygen threads will be given releaseHydrogen and releaseOxygen methods
respectively, which will allow them to pass the barrier. These threads should pass the
barrier in groups of three, and they must immediately bond with each other to form a
water molecule. You must guarantee that all the threads from one molecule bond before
any other threads from the next molecule do.

In other words:
    - If an oxygen thread arrives at the barrier when no hydrogen threads are present,
      it must wait for two hydrogen threads.
    - If a hydrogen thread arrives at the barrier when no other threads are present,
      it must wait for an oxygen thread and another hydrogen thread.

Write synchronization code for oxygen and hydrogen molecules that enforces these constraints.


Example 1:
    Input: water = "HOH"
    Output: "HHO"
    Explanation: "HOH" and "OHH" are also valid answers.

Example 2:
    Input: water = "OOHHHH"
    Output: "HHOHHO"
    Explanation: "HOHHHO", "OHHHHO", "HHOHOH", "HOHHOH", "OHHHOH", "HHOOHH", "HOHOHH"
                 and "OHHOHH" are also valid answers.


Constraints:
    * 3 * n == water.length
    * 1 <= n <= 20
    * water[i] is either 'H' or 'O'
    * There will be exactly 2 * n 'H' in water
    * There will be exactly n 'O' in water

"""

from threading import Semaphore, Barrier


class H2O:
    def __init__(self):
        self.hydrogen_semaphore = Semaphore(2)
        self.oxygen_semaphore = Semaphore(1)
        self.barrier = Barrier(3)

    def hydrogen(self, releaseHydrogen: "Callable[[], None]") -> None:
        self.hydrogen_semaphore.acquire()
        self.barrier.wait()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        self.hydrogen_semaphore.release()

    def oxygen(self, releaseOxygen: "Callable[[], None]") -> None:
        self.oxygen_semaphore.acquire()
        self.barrier.wait()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.oxygen_semaphore.release()
