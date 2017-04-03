import random


def RandomizedSelect(list_item, start, end, i):

    if start == end:
        return list_item[start]

    q = RandomizedPartition(list_item, start, end)
    k = q - start + 1

    if i == k:
        return list_item[q]
    elif i < k:
        return RandomizedSelect(list_item, start, end - 1, i)
    else:
        return RandomizedSelect(list_item, start + 1, end, i)


def RandomizedPartition(list_item, start, end):

    i = random.randrange(start, end + 1)
    list_item[end], list_item[i] = list_item[i], list_item[end]


    return Partition(list_item, start, end)

def Partition(list_item, start, end):

    x = list_item[end]
    i = start - 1

    for j in range(start, end):

        if list_item[j] <= x:
            i += 1
            list_item[i], list_item[j] = list_item[j], list_item[i]

    list_item[i + 1], list_item[end] = list_item[end], list_item[i + 1]

    return i + 1




list_item = [3, 2, 4, 8, 9, 6, 5, 1]

print(RandomizedSelect(list_item, 0, len(list_item) - 1, 2))
