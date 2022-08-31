#Merge Sort

def merge(array,l,r,mid):
  
  '''merges two array according to the sorting '''
    i = l
    j = mid+1
    k = l
    temp = [0 for x in range(20)]
    
    #merging the two sorted arrays
    while (i <= mid and j <= r):
      
       # print("i is = ",i,mid)
        if(array[i] < array[j]):
            temp[k] = array[i]
            i = i + 1
        else:
            temp[k] = array[j]
            j = j + 1
        k = k + 1
        
    if (i > mid):
      #taking care of the elements left in right part
        while (j <= r):
            temp[k] = array[j]
            j = j + 1
            k = k + 1
    else:
      #taking care of the elements left in the left part.
        while (i <= mid):
            temp[k] = array[i]
            i = i + 1
            k = k + 1
    print(temp)
    for t in range(l,r+1):
        array[t] = temp[t] 
            
        
        
def mergeSort(array,l,r):
  
  '''Divides the array into two parts'''
    
    #print("mid is = ",mid)
    if(l<r):
        mid = (l+r)//2
        #print("mid is = ",mid,l,r)
        mergeSort(array,l,mid)
        mergeSort(array,mid+1,r)
        merge(array,l,r,mid)
    
if __name__ == "__main__":
    
    array = [4,3,5,6,2,1]
    l = 0
    r = len(array)-1
    
    mergerSort(array,l,r)
    print(array)
