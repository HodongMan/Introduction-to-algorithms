class Node:

    def __init__(self, value):

        self.value = value
        self.n = 0
        self.key = []
        self.leaf = True


class B_Tree():

    def __init__(self, root=None):

        self.root = root

    def initialize():

        self.root = Node()
        self.diskWrite(self.root)

    def search(self, value):

        i = 0

        while i <= self.root.n and k > self.root.key[i]:
            i = i + 1
        if i < self.root.n and value == self.root.key[i]
            return(self.root, i)
        elif x.leaf:
            return None
        else
            self.diskRead(self.key)
            return self.searchChild(self.key, value)






