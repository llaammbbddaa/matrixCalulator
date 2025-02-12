# matrixFunctions.py
# all of the matrix functionality, including row reduction / gaussian elimination

import numpy as np

def initMatrix(r, c):
    rows = r
    cols = c
    arr = [[0] * cols for _ in range(rows)]  # Creates a rxc array initialized with 0s
    return arr

def outputMatrix(m):
    for i in range(len(m)):
        print ("| ", end=" ")
        for j in range(len(m[i])):
            if (m[i][j] <= 9):
                print(str(m[i][j]), end="   ")
            elif (m[i][j] <= 99):
                print(str(m[i][j]), end="  ")
            else:
                print(str(m[i][j]), end=(" "))
        print(" |")
    print("\n")
        
        
def createMatrix(r,c,inputs):
    arr = initMatrix(r,c)
    numString = inputs
    
    # turns said string into a list
    nums = list(map(float, numString.split()))
    
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            #print("i " + str(i) + " j " + str(j) + " lenNums " + str(len(nums)))
            arr[i][j] = nums[int((i * c)) + j]
            #print("arr >> " + str(arr[i][j]) + " index >> " + str(int((i * (len(nums) / (i + 1)))) + j))
                
    return arr

def getMatrixData():
    row = int(input("enter rows >> "))
    col = int(input("enter columns >> "))
    numString = input("enter values seperated by a space >> ")

    matrix = createMatrix(row, col, numString)
    outputMatrix(matrix)
    
    return matrix

def transpose(m):
    a = initMatrix(len(m[0]), len(m))
    for i in range(len(m)):
        for j in range(len(m[i])):
            a[j][i] = m[i][j]
    
    return a

def add(a, b):
    if (len(a) == len(b) and len(a[0]) == len(b[0])):
        c = initMatrix(len(a), len(a[0]))
        for i in range(len(a)):
            for j in range(len(a[i])):
                c[i][j] = a[i][j] + b[i][j]
                
        return c
    else:
        print("matrice dimensions are not equal, addition is not possible")
        
def sub(a, b):
    if (len(a) == len(b) and len(a[0]) == len(b[0])):
        c = initMatrix(len(a), len(a[0]))
        for i in range(len(a)):
            for j in range(len(a[i])):
                c[i][j] = a[i][j] - b[i][j]
                
        return c
    else:
        print("matrice dimensions are not equal, subtraction is not possible")
        
def scalar(a, c):
    for i in range(len(a)):
        for j in range(len(a[i])):
            a[i][j] *= c
    return a
            
def mult(a, b):
    if (len(a[0]) == len(b)):
        c = initMatrix(len(a), len(b[0]))
        summit = 0
        ci = 0
        cj = 0
        for k in range(len(c)):
            for i in range(len(a)):
                #print("ci >>" + str(ci) + " cj >> " + str(cj))
                for j in range(len(a[i])):
                    summit += a[ci][j] * b[j][i]
                c[ci][cj] = summit
                summit = 0
                if (cj >= (len(c[0]) - 1)):
                    cj = 0
                    ci += 1
                else:
                    cj += 1
        return c
    else:
        print("not proper dimensions, multiplication not possible")

def gaussian(a, b):
    
    # making sure the matrices given are valid for gaussian elimination
    if (len(a) != len(a[0]) or len(b[0]) != 1 or len(b) != len(a)):
        print("one of the matricies has been inputted incorrectly")
        print("matrix one must be square, and matrix two must be a column matrix with size proportional to matrix one")
        
        # just so the code stops before anything else yk
        return
     
    #initialization of necessary variables
    n = len(b)
    m = n - 1
    i = 0
    j = i - 1
    x = np.zeros(n)
    new_line = "/n" # because im lazy
    
    #create our augmented matrix throug Numpys concatenate feature
    aug = np.concatenate((a, b), axis=1)
    #outputMatrix(aug)
    #print("solving for the upper-triangular matrix")
    
    #applying gauss elimination:
    while i < n:
        if aug[i][i] == 0.0: #fail-safe to eliminate divide by zero erroor!
            print("dividing by zero would be a bad idea")
            return # because we can no longer continue
        for j in range(i + 1, n):
            scaleFactor = aug[j][i] / aug[i][i]
            aug[j] = aug[j] - (scaleFactor * aug[i])
            #outputMatrix(aug) #not needed, but nice to visualize the process
            
        i = i + 1
    
        #backwords substitution!
        x[m] = aug[m][n] / aug[m][m]
        for k in range(n - 2 , -1, -1):
            x[k] = aug[k][n]
            for j in range(k + 1, n):
                x[k] = x[k] / aug[k][k]
    
    
    #displaying solution 
    #print("The following x vector matrix solves the above augmented matrix:")
    output = ""
    for i in range(n):
        output += ("x" + str(i + 1) + " = " + str(x[i]) + ", ")
    print(output)
    return x

def main():
    a = createMatrix(3, 3, "1 1 3 0 1 3 -1 3 0")
    b = createMatrix(3, 1, "1 3 5")
    gaussian(a,b)

