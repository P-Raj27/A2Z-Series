#Selection Sort.

def selectionSort(array):
    '''Sorts the given array using Selection Sort'''
    index = 0
    for i in range(len(array)):
        minimum = max(array) + 1
        for j in range(i,len(array)):
            if (array[j] < minimum):
                minimum = array[j]
                index = j
        array[i],array[index] = array[index],array[i]
    return array

if __name__ == "__main__":
    array = [4,3,5,6,2,1]
    print(selectionSort(array))
