#!/usr/bin/python3
from typing import List
"""
Created on friday 2022

@author: John Danlami
"""


def pascal_triangle(n: int) -> List[List]:
    '''
     pascal_triangle - that returns a list of
     lists of integers representing the Pascal’s
     triangle of n:
     @n: n will be always an integer
     Returns: an empty list if n <= 0
    '''
    if n <= 0:
        return []

    temp = []
    for i in range(1, n+1):
        temp1:list = []
        C = 1
        for j in range(1, i+1):
            temp1.append(C)
            C = C * (i - j) // j
        temp.append(temp1)
    return temp
