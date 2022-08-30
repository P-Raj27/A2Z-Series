#Bubble Sort
def bubbleSort(array):
    for i in range(len(array)):
        swapped = False
        for j in range(len(array)-i-1):
            if(array[j] > array[j+1]):
                array[j],array[j+1] = array[j+1],array[j]
                swapped = True
        if(swapped == False):
            break
    return array
if __name__ == "__main__":
    array = [4,3,5,6,2,1]
    print(bubbleSort(array))
