#Maximum number of Consecutive 1's.

array = [1,0,0,1,1,0,1,0,1,1,1]
l = 0
k = 2
zeros = 0
maxx = 0
for i in range(len(array)):
    
    if(array[i] == 0):
        zeros = zeros + 1
    if(zeros > k):
        while(zeros > k):
            if(array[l] == 0):
                zeros = zeros - 1
            l = l + 1
    maxx = max(maxx,i-l+1)
print(maxx)
    
            
