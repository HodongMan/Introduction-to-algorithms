import sys

class FindMaxSubArray(object):

  def __init__(self):
	
	  self._data = list()
	  self._array = list()

  def setData(self, data):
	
	  self._data = data

  def printData(self):
	
	  print(self._array)

  def findMaxCrossingSubarray(self, low, mid, high):
  
	  left_sum = 0
	  left_sum -= sys.maxsize - 1
	  sum_value = 0

	  for i in range(mid, low - 1, -1):
		sum_value += self._data[i]
		if sum_value > left_sum:
		  left_sum = sum_value
		  max_left = i

	  right_sum = 0
	  right_sum -= sys.maxsize - 1
	  sum_value = 0

	  for i in range(mid + 1, high):
		sum_value += self._data[i]
		if sum_value > right_sum:
		  right_sum = sum_value
		  max_right = i
		  
	  return (max_left, max_right, left_sum + right_sum)


	def findMaximumSubarray(self, low, high):

	  if high == low:
		return(low, high, self_.data[low])
	  else mid == (low+high) // 2:
		pass
