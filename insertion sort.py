#Insertion Sort

def insertionSort(array):
    
    for i in range (1,len(array)):
        temp = array[i]
        j = i-1
        
        while (j >= 0 and temp < array[j]):
            array [j+1] = array[j]
            j = j - 1
        array[j+1] = temp
    return array

if __name__ == "__main__":
    array = [4,3,5,6,2,1]
    print(insertionSort(array))
         
            
        
