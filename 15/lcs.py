"""
    commonsubsequence class solution
"""

class CommonSubsequence:

    def __init__(self, x="", y=""):

        self.stringX = "x" + x
        self.stringY = "y" + y

        self.initialize()

    def initialize(self):

        m = len(self.stringX)
        n = len(self.stringY)

        self.arrow_list = [["" for x in range(n)] for y in range(m)]
        self.number_list = [[0 for x in range(n)] for y in range(m)]

    def LCSLength(self):

        m = len(self.stringX)
        n = len(self.stringY)

        for i in range(1, m):
            for j in range(1, n):
                
                if self.stringX[i] == self.stringY[j]:
                    self.number_list[i][j] = self.number_list[i-1][j-1] + 1
                    self.arrow_list[i][j] = "cross"
                elif self.number_list[i-1][j] >= self.number_list[i][j-1]:
                    self.number_list[i][j] = self.number_list[i-1][j]
                    self.arrow_list[i][j] = "up"
                else:
                    self.number_list[i][j] = self.number_list[i][j-1]
                    self.arrow_list[i][j] = "left"


    def printLCS(self, i, j):

        if i == 0 or j == 0:
            return
        if self.arrow_list[i][j] == "cross":
            self.printLCS(i-1, j-1)
            print(self.stringX[i], end="")
        elif self.arrow_list[i][j] == "up":
            self.printLCS(i-1, j)
        else:
            self.printLCS(i, j-1)

    def printResult(self):

        self.LCSLength()
        self.printLCS(len(self.stringX) - 1 , len(self.stringY) - 1)
        print()

"""
    common sequence function solution
"""
def LCSLength(stringX, stringY):


    m = len(stringX)
    n = len(stringY)

    b = [["" for x in range(n)] for y in range(m)]
    c = [[0 for x in range(n)] for y in range(m)]


    for i in range(1, m):
        for j in range(1, n):
            if stringX[i] == stringY[j]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = "cross"
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = "up"
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = "left"
    return b, c
    

def printLCS(b, X, i, j):

    if i == 0 or j == 0:
        return
    if b[i][j] == "cross":
        printLCS(b, X, i-1, j-1)
        print(X[i])
    elif b[i][j] == "up":
        printLCS(b, X, i-1, j)
    else:
        printLCS(b, X, i, j-1)


if __name__ == "__main__":
    

    lcs = CommonSubsequence("ABCBDBA", "BDCABA")
    lcs.printResult()
