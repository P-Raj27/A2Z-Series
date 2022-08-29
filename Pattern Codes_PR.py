def patternIsoscelesStar(num):
    
    '''
    *
    **
    ***
    ****
    *****
    '''
    
    for i in range(1,num+1):
        for j in range(i):
            print("*",end ="")
        print()
def patternEquilateralStar(num):
    ''' *    
       ***   
      *****  
     ******* 
    *********'''
    
    for i in range(1,num+1):
        start = num - i + 1
        end = start + 2*i -2
        #print(f"Start is = {start}, and end is = {end}")
        for j in range(1,2*num):
            
            if (j >= start and j<=end):
                print("*",end = "")
            else:
                print(" ",end = "")
        print()
def patternEquilateralStarReverse(num):
    '''
    *********
     ******* 
      *****  
       ***   
        *  
    '''
    
    for i in range(1,num+1):
        start = i
        end = 2*num - i
        #print(f"Start is = {start}, and end is = {end}")
        for j in range(1,2*num):
            
            if (j >= start and j<=end):
                print("*",end = "")
            else:
                print(" ",end = "")
        print()
def isoscelesEquilateralTriangleIncreasingNumber(num):
    
    """
    1 
    2 3 
    4 5 6 
    7 8 9 10 
    11 12 13 14 15 
    """
    number = 1
    for i in range(1,num+1):
        for j in range(i):
            print(number,end = " ")
            number = number + 1
        print()
 if __name__ == "__main__":
    num = int(input())
    patternIsoscelesStar(num)
    patternEquilateralStar(num)
    patternEquilateralStarReverse(num)
    
    partition = num // 2
    patternEquilateralStar(partition)
    patternEquilateralStarReverse(partition)
    
    isoscelesEquilateralTriangleIncreasingNumber(num)
    
