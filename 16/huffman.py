import heapq
from collections import namedtuple

huffmanNode = namedtuple("huffmanNode", ("value", "freq"))


class PriorityQueue:

    def __init__(self):

        self._queue = []
        self._index = 0

    def __len__(self):

        return len(self._queue)
    
    def push(self, item):
        
        heapq.heappush(self._queue, (item.freq, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Node:

    def __init__(self):

        self.left = None
        self.right = None
        self.freq = 0

    def printNode(self):

        print(self.freq)
        self.printPreorderTraversal(self.left)
        self.printPreorderTraversal(self.right)

    def printPreorderTraversal(self, node):

        if isinstance(node, Node):

            print(node.freq)
            self.printPreorderTraversal(node.left)
            self.printPreorderTraversal(node.right)
        else:
            print(node)


    @property
    def freq(self):
        
        if isinstance(self._freq, huffmanNode):
            return self._freq.frequency
        return self._freq

    @freq.setter
    def freq(self, value):

        self._freq = value



def makeHuffmanTree(q):

    n = len(q)

    for i in range(n - 1):
        z = Node()
        z.left = q.pop()
        z.right = q.pop()
        z.freq = z.left.freq + z.right.freq
        q.push(z)

    return q.pop()



if __name__ == "__main__":

    q = PriorityQueue()
    q.push(huffmanNode("f", 5))
    q.push(huffmanNode("e", 9))
    q.push(huffmanNode("c", 12))
    q.push(huffmanNode("b", 13))
    q.push(huffmanNode("d", 16))
    q.push(huffmanNode("a", 45))

    makeHuffmanTree(q).printNode()
