#!/usr/bin/env python
# encoding: utf-8

import sys

def generateMatrixFromLines(lines):
    if(len(lines) == 0):
        return;

    matrix = {}
    
    matrixDimensionsLine = lines[0].split();
    if(len(matrixDimensionsLine) != 2):
        print("Error at reading line '" + lines[0].rstrip() + "'. Matrix must be defined with only 2 values: height & width.")
        return;
    
    matrixHeight, matrixWidth = map(int, matrixDimensionsLine)
    matrix["width"] = matrixWidth
    matrix["height"] = matrixHeight
    
    for line in lines[1:]:
        lineParts = line.split()
        if(len(lineParts) != 3):
            print("Error at reading line '" + line.rstrip() + "'. Every line needs exactly 3 values!")
            return;
        
        try:
            matrix[int(lineParts[0]), int(lineParts[1])] = float(lineParts[2])
        except ValueError:
            print("Error at reading line '" + line.rstrip() + "'. All values must be numbers (ints or floats)!")
            return;
        
    return matrix

def importMatricesFromFile(fileName):
    matricesLines = []
    file = open(fileName, 'r', encoding='utf8')
    lines = file.readlines()
    
    matrixLines = []
    for line in lines:
        if(line == "\n"):
            matricesLines.append(matrixLines)
            matrixLines = []
        else:
            matrixLines.append(line)
            
    # End of file (no \n at the end?)
    if(len(matrixLines) > 0):
        matricesLines.append(matrixLines)
        matrixLines = []
    
    matrices = []
    for matrixLines in matricesLines:
        matrix = generateMatrixFromLines(matrixLines)
        
        # Error in matrix formatting
        if(matrix == None):
            return;
        else:
            matrices.append(matrix)
    
    return matrices
    
def multiplyMatrices(matrix1, matrix2):
    matrix1Width = matrix1["width"]
    matrix1Height = matrix1["height"]
    matrix2Width = matrix2["width"]
    matrix2Height = matrix2["height"]
    
    # Cannot multiply if sizes don't match
    if(matrix1Width != matrix2Height):
        print("Width of matrix 1 (" + str(matrix1Width) + ") must match height of matrix 2 (" + str(matrix2Height) + ")")
        return {}
    
    multipliedMatrix = {}
    multipliedMatrix["height"] = matrix1Height
    multipliedMatrix["width"] = matrix2Width
    
    for i in range(matrix1Height):
        for j in range(matrix2Width):
            multipliedValue = 0
            for k in range(matrix1Width):
                multipliedValue += matrix1.get((i, k), 0)*matrix2.get((k, j), 0)
                if(multipliedValue != 0):
                    multipliedMatrix[i, j] = multipliedValue
    
    return multipliedMatrix
    
def printMatrix(matrix):
    matrixWidth = matrix.get("width", 0)
    matrixHeight = matrix.get("height", 0)
    for i in range(matrixHeight):
        for j in range(matrixWidth):
            print("{:9.3f}".format(matrix.get((i, j), 0)), end = "")
        print()

def saveMatrixToFile(matrix, fileName):
    with open(fileName, "w") as file:
        file.write(str(matrix.get("height", 0)) + " " + str(matrix.get("width", 0)) + "\n")
        for key in matrix:
            if(key != "width" and key != "height"):
                file.write(str(key[0]) + " " + str(key[1]) + " " + str(matrix[key]) + "\n")

if __name__ == "__main__":
    matrixFileName = sys.argv[1]
    matricesLines = importMatricesFromFile(matrixFileName)
    
    if(matricesLines != None):
        if(len(matricesLines) < 2):
            print("Please specify at least 2 matrices in the file (separated with new line)")
        else:
            multipliedMatrix = multiplyMatrices(matricesLines[0], matricesLines[1])
            printMatrix(multipliedMatrix)
        
            saveMatrixToFile(multipliedMatrix, "matrices_out.txt")
