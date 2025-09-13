#Student Name: Sariah Shoemaker
#Student ID: 873644188

import pandas as pd
import numpy as np
import scipy
import A0_Utils as A0
import random

## Question 1 - Basics

def add(a, b):
    # See Question 1a
    ## TODO: Define Function
    ## TODO: comment out "raiseNotDefined()" when you start working on this function
    # A0.raiseNotDefined()
    if((type(a) == int or type(a) == float)):
        if(type(b) == list or type(b) == str):
            returnString = str(a)
            for item in b:
                returnString += str(item)
            return(returnString)
        elif(type(b) == int or type(b) == float):
            return(a + b)
        else:
            print("Error!")
            return(None)
    elif(type(a) == list):
        if(type(b) == list):
            a.extend(b)
            return a
        elif(type(b) == int or type(b) == float or type(b) == str):
            returnString = ""
            for item in a:
                returnString += str(item)
            returnString += str(item)
            return(returnString)
        else:
            print("Error!")
            return(None)
    elif(type(a) == str):
        if(type(b) == str):
            return(a + b)
        elif(type(b) == int or type(b) == float):
            return(a + str(b))
        elif(type(b) == str):
            returnString = a
            for item in b:
                returnString += str(item)
            return(returnString)
        else:
            print("Error!")
            return(None)
    else:
        print("Error!")
        return(None)
        

def calcMyGrade(AssignmentScores, MidtermScores, PracticumScores, ICAScores, Weights):
    # See Question 1b
    ## TODO: Define Function
    ## TODO: comment out "raiseNotDefined()" when you start working on this function
    # A0.raiseNotDefined()
    assignmentAverage = sum(AssignmentScores) / len(AssignmentScores)
    midtermAverage = sum(MidtermScores) / len(MidtermScores)
    practicumAverage = sum(PracticumScores) / len(PracticumScores)
    icaAverage = sum(ICAScores) / len(ICAScores)
    
    return(((assignmentAverage * Weights[0]) + (midtermAverage * Weights[1]) + (practicumAverage * Weights [2]) + (icaAverage * Weights[3])) * 0.01)


## Question 2 - Classes

class node:
    # See Question 2a
    def __init__(self, key: int, value) -> object:
        # A0.raiseNotDefined()
        self.key = key
        self.value = value
        self.leftchild = None
        self.rightchild = None
    
    def getChildren(self):
        children = []
        children.append(self.leftchild)
        children.append(self.rightchild)
        return(children)
    
    def getKey(self):
        return(self.key)
    
    def getValue(self):
        return(self.value)
    
    def assignLeftChild(self, child: 'node'):
        self.leftchild = child
        
    def assignRightChild(self, child: 'node'):
        self.rightchild = child
        
    def inOrderTraversal(self):
        result = []
        if(self.leftchild != None):
            result += self.leftchild.inOrderTraversal()
        result.append(self.value)
        if (self.rightchild != None):
            result += self.rightchild.inOrderTraversal()
        return(result)
         
        

class queue:
    # See Question 2b
    def __init__(self) -> object:
        # A0.raiseNotDefined()
        self.values = []
        
    def push(self, value):
        self.values.append(value)
        
    def pop(self):
        if(self.values == []):
            return(None)
        else:
            return(self.values.pop(0))
        
    def checkSize(self):
        return(len(self.values))


## Question 3 - Libraries

def generateMatrix(numRows, numcolumns, minVal, maxVal):
    # See Question 3ai
    ## TODO: Define Function
    ## TODO: comment out "raiseNotDefined()" when you start working on this function
    # A0.raiseNotDefined()
    matrix = np.random.uniform(minVal, maxVal + 1, size=(numRows, numcolumns))
    return matrix

def multiplyMat(m1, m2):
    # See Question 3a_ii
    ## TODO: Define Function
    ## TODO: comment out "raiseNotDefined()" when you start working on this function
    # A0.raiseNotDefined()
    try:
        return(np.matmul(m1, m2))
    except:
        print("Incompatible Matrices")
        return(None)

def statsTuple(a, b):
    # See Question 3b
    ## TODO: Define Function
    ## TODO: comment out "raiseNotDefined()" when you start working on this function
    try:
        return(int(np.sum(a)), 
               float(np.mean(a)),
               int(np.min(a)),
               int(np.max(a)),
               int(np.sum(b)), 
               float( np.mean(b)),
               int(np.min(b)),
               int(np.max(b)),
               round(float(scipy.stats.pearsonr(a, b)[0]), 2),
               round(float(scipy.stats.spearmanr(a, b)[0]), 2)
               )
    except:
        return(None)

def pandas_func(fileName):
    # See Question 3c
    ## TODO: Define Function
    ## TODO: comment out "raiseNotDefined()" when you start working on this function
    # A0.raiseNotDefined()
    df = pd.read_csv(fileName, sep="\t")
    ListOfMeans = []
    ListOfColumnNames = []
    
    for label, content in df.items():
        if pd.api.types.is_numeric_dtype(content):
            ListOfMeans.append(round(content.mean(), 2))
        else:
            ListOfColumnNames.append(label)
                
    return (ListOfMeans, ListOfColumnNames)