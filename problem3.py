#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 23 14:58:48 2018

@author: arry
"""

A = ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]

def verify(A):
    listInput = []
    for i in A:
        listInput.append(list(i))
        
    seen3 = set()
    seen4 = set()
    seen5 = set()
    seen6 = set()
    seen7 = set()
    seen8 = set()
    seen9 = set()
    seen10 = set()
    seen11 = set()
    for i in range(9):
        seen1 = set()
        seen2 = set()
        for j in range(9):
            if(listInput[i][j] != "."):
                if(i<3 and j<3):
                    if(listInput[i][j] in seen3):
                        return 0
                    else:
                        seen3.add(listInput[i][j])
                        
                if(i<6 and j<3 and i>2):
                    if(listInput[i][j] in seen4):
                        return 0
                    else:
                        seen4.add(listInput[i][j])
                        
                if(i<9 and j<3 and i>5):
                    if(listInput[i][j] in seen5):
                        return 0
                    else:
                        seen5.add(listInput[i][j])
                        
                if(i<3 and j<6 and j>2):
                    if(listInput[i][j] in seen6):
                        return 0
                    else:
                        seen6.add(listInput[i][j])
                        
                if(i<6 and j<6 and i>2 and j>2):
                    if(listInput[i][j] in seen7):
                        return 0
                    else:
                        seen7.add(listInput[i][j])
                        
                if(i<9 and j<6 and i>5 and j>2):
                    if(listInput[i][j] in seen8):
                        return 0
                    else:
                        seen8.add(listInput[i][j])
                        
                if(i<3 and j<9 and j>5):
                    if(listInput[i][j] in seen9):
                        return 0
                    else:
                        seen9.add(listInput[i][j])
                        
                if(i<6 and j<9 and i>2 and j>5):
                    if(listInput[i][j] in seen10):
                        return 0
                    else:
                        seen10.add(listInput[i][j])
                        
                if(i<9 and j<9 and i>5 and j>5):
                    if(listInput[i][j] in seen11):
                        return 0
                    else:
                        seen11.add(listInput[i][j])
                
                
                
                if(listInput[i][j] in seen1):
                    return 0
                else:
                    seen1.add(listInput[i][j])
                
            if(listInput[j][i]!="."):
                if(listInput[j][i] in seen2):
                    return 0
                else:
                    seen2.add(listInput[j][i])
            
    return 1
print(verify(A))