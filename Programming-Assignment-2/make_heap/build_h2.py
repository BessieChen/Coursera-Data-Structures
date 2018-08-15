# python3
import heapq
import sys

class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self._data = []

    def ReadData(self):
        # n = int(input())
        # self._data = [int(s) for s in input().split()]
        self.n = int(sys.stdin.readline())
        self._data = list(map(int, sys.stdin.readline().split()))
        assert self.n == len(self._data)

    def WriteResponse(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def GenerateSwaps(self):
        # The following naive implementation just sorts
        # the given sequence using selection sort algorithm
        # and saves the resulting sequence of swaps.
        # This turns the given array into a heap,
        # but in the worst case gives a quadratic number of swaps.
        # TODO: replace by a more efficient implementation
        size = len(self._data)
        n = len(self._data)
        for i in range((n - 1) // 2, -1, -1):
            self.ShiftDown(i)
            """
          for i in range(n-2):
            self._data[0],self._data[size-1]=self._data[size-1],self._data[0]
            size=size-1
            self.ShiftDown(1)
            """

    def LeftChild(self, i):
        return 2 * i + 1

    def RightChild(self, i):
        return 2 * i + 2

    def ShiftDown(self, i):
        minIndex = i
        size = len(self._data)
        l = self.LeftChild(i)

        if l <= size - 1 and self._data[l] < self._data[minIndex]:
            minIndex = l

        r = self.RightChild(i)
        if r <= size - 1 and self._data[r] < self._data[minIndex]:
            minIndex = r
        if i != minIndex:
            self._data[i], self._data[minIndex] = self._data[minIndex], self._data[i]
            self._swaps.append([i, minIndex])
            self.ShiftDown(minIndex)

    def Solve(self):
        self.ReadData()
        self.GenerateSwaps()
        self.WriteResponse()


if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()