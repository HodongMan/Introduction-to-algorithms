class CountingSort(object):

    def __init__(self):

        self._data = list()

    def setData(self, data):

        self._data = data

    def printData(self):

        print(self._data)

    def countingSort(self, max_item):

        data_len = len(self._data)
        temp_list = list()
        ordered_list = list()

        for i in range(max_item + 1):
            temp_list.append(0)

        for i in range(data_len):
            temp_list[self._data[i]] += 1
            ordered_list.append(0)

        for i in range(1, max_item + 1):
            temp_list[i] = temp_list[i] + temp_list[i-1]

        for i in range(data_len - 1, -1, -1):
            ordered_list[temp_list[self._data[i]] - 1] = self._data[i]
            temp_list[self._data[i]] -= 1

        self._data = ordered_list
cs = CountingSort()
cs.setData([2, 5, 3, 0, 2, 3, 0, 3])
cs.countingSort(5)
cs.printData()
