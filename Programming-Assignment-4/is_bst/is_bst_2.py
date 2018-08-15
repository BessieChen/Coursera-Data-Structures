#!/usr/bin/python3
import sys, threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 25)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        if self.n == 0:
            self.key = [0]
            self.left = [-1]
            self.right = [-1]
        else:
            self.key = [0 for i in range(self.n)]
            self.left = [0 for i in range(self.n)]
            self.right = [0 for i in range(self.n)]
            for i in range(self.n):
                [a, b, c] = map(int, sys.stdin.readline().split())
                self.key[i] = a
                self.left[i] = b
                self.right[i] = c

    def inOrder(self):
        self.result = []

        def inOrder_recursive(root):
            if self.left[root] != -1:
                inOrder_recursive(self.left[root])
            self.result.append(self.key[root])
            if self.right[root] != -1:
                inOrder_recursive(self.right[root])

        inOrder_recursive(0)
        return self.result

    def IsBinarySearchTree(self):
        # Implement correct algorithm here
        in_order = self.inOrder()
        in_order_sort = sorted(in_order)
        if in_order == in_order_sort:
            return True
        else:
            return False


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if tree.IsBinarySearchTree():
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()