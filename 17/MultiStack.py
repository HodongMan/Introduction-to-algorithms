
class MultiStack:

    def __init__(self):

        self._data = []

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):

        raise Exception("Data can not insert")

    def __len__(self):
        
        return len(self._data)

    def push(self, value):

        self._data.append(value)

    def isEmpty(self):

        return len(self._data) == 0

    def pop(self):

        return self._data.pop()

    def multiPop(self, count):

        while not self.isEmpty() and count > 0:
            
            yield self.pop()
            count -= 1


if __name__ == "__main__":

    multi = MultiStack()

    multi.push(47)
    multi.push(10)
    multi.push(39)
    multi.push(6)
    multi.push(17)
    multi.push(23)

    for i in multi.multiPop(4):

        print(i)







