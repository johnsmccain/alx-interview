''' Module: #0x00. Pascal's Triangle
'''

def pascal_triangle(n):
    '''
     pascal_triangle - that returns a list of 
     lists of integers representing the Pascal’s 
     triangle of n:
     @n: lists of integers
     Return: []
    '''
    temp = []
    
    if n <= 0:
        return []

    for i in range(1, n+1):
        temp1 = [] 
        C = 1

        for j in range(1, i+1):
            temp1.append(C)
            C = C * (i - j) // j
        temp.append(temp1)
         
    return temp
