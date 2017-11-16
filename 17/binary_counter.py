

def increment(array):

    i = len(array) - 1
    while i >= 0 and array[i] == 1:
        array[i] = 0
        i = i - 1
    if i >= 0:
        array[i] = 1

    return array


if __name__ == "__main__":

    binary = [0] * 8
    
    for i in range(8):
        binary = increment(binary)
        print(binary)
