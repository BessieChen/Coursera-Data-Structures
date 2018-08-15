# python3

import sys, threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size

class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        print("into_inOrder")
        self.result = []

        def inOrder_recursive(root):
            print("root",root)
            print("self.left[root]",self.left[root])
            print('self.right[root]',self.right[root])
            if self.left[root] != -1:
                print("into_inOrder_recursive(self.left[root])")
                inOrder_recursive(self.left[root])
            self.result.append(self.key[root])
            if self.right[root] != -1:
                print("into_inOrder_recursive(self.right[root])")
                inOrder_recursive(self.right[root])

        inOrder_recursive(0) #got it!it is easier than the harvard one.
        print("out_from_inOrder")
        return self.result

    def preOrder(self):
        print("into_inOrder")
        self.result = []

        # Finish the implementation
        # You may need to add a new recursive method to do that
        def preOrder_recursive(root):
            print("root", root)
            print("self.left[root]", self.left[root])
            print('self.right[root]', self.right[root])
            self.result.append(self.key[root])
            if self.left[root] != -1:
                print("into_preOrder_recursive(self.left[root])")
                preOrder_recursive(self.left[root])
            if self.right[root] != -1:
                print("into_preOrder_recursive(self.right[root])")
                preOrder_recursive(self.right[root])

        preOrder_recursive(0)
        print("out_from_inOrder")
        return self.result

    def postOrder(self):
        print("into_inOrder")
        self.result = []

        # Finish the implementation
        # You may need to add a new recursive method to do that
        def postOrder_recursive(root):
            print("root", root)
            print("self.left[root]", self.left[root])
            print('self.right[root]', self.right[root])
            if self.left[root] != -1:
                print("into_postOrder_recursive(self.left[root])")
                postOrder_recursive(self.left[root])
            if self.right[root] != -1:
                print("into_postOrder_recursive(self.right[root])")
                postOrder_recursive(self.right[root])
            self.result.append(self.key[root])

        postOrder_recursive(0)
        print("out_from_inOrder")
        return self.result


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()