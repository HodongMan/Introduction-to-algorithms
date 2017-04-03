
def Minimum(data):

    min = data[0]

    for index, item in enumerate(data):

        if min > item:

            min = item

    return min


num_list = [3, 2, 4, 6, 8, 9 ,10]
print(Minimum(num_list))

