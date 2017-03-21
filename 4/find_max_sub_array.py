import sys

class FindMaxSubarray(object):
    def __init__(self):

        self._data = list()
        self._subarray = list()

    def setData(self, data):

        self._data = data

    def printData(self):

        print(self._subarray)

    def findMaxCrossingSubarray(self, low, mid, high):
        left_sum = 0
        left_sum -= sys.maxsize - 1
        sum_value = 0
        max_left = 0
        max_right = 0

        for i in range(mid, low - 1, -1):
            sum_value += self._data[i]
            if sum_value > left_sum:
                left_sum = sum_value
                max_left = i

        right_sum = 0
        right_sum -= sys.maxsize - 1
        sum_value = 0

        for i in range(mid + 1, high + 1):
            sum_value += self._data[i]


            if sum_value > right_sum:
                right_sum = sum_value
                max_right = i

        return (max_left, max_right, left_sum + right_sum)

    def findMaxSubarray(self, low, high):

        if high == low:

            return(low, high, self._data[low])

        else:

            mid = (low+high) // 2

            (left_low, left_high, left_sum) = self.findMaxSubarray(low, mid)
            (right_low, right_high, right_sum) = self.findMaxSubarray(mid + 1, high)
            (cross_low, cross_high, cross_sum) = self.findMaxCrossingSubarray(low, mid, high)

            if left_sum >= right_sum and left_sum >= cross_sum:
                return (left_low, left_high, left_sum)
            elif right_sum >= left_sum and right_sum >= cross_sum:
                return (right_low, right_high, right_sum)
            else:
                return (cross_low, cross_high, cross_sum)

    def findSubarray(self):

        max_low, max_high, max_sum = self.findMaxSubarray(0, len(self._data) - 1)
        self._subarray = self._data[max_low : max_high + 1]

data = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

fbs = FindMaxSubarray()
fbs.setData(data)
fbs.findSubarray()
fbs.printData()
