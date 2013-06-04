#!/usr/bin/env python
# encoding: utf-8

import sys
import math

def importHypothesisFromFile(fileName):
    with open(fileName) as file:
        hypothesis = map(lambda x: sorted(x.split(), key = float), file.readlines())
        
    return hypothesis

def printHeader():
    quantiles = [x for x in range(10, 100, 10)]
    quantilesJoined = "#".join(['Q' + str(x) for x in quantiles])
    
    print("Hyp#" + quantilesJoined)

def printHausdorffDistanceValues(hypothesisValues):
    quantiles = [x for x in range(10, 100, 10)]
    
    hausdorffDistances = []
    for q in quantiles:
        hdValueIndex = int(math.floor(q/100*len(hypothesisValues)))
        hausdorffDistance = hypothesisValues[hdValueIndex]
        hausdorffDistances.append(hausdorffDistance)
    
    print('#'.join(map(lambda x: "{:3.2f}".format(float(x)), hausdorffDistances)))
    
if __name__ == "__main__":
    fileName = sys.argv[1]
    
    try:
        with open(fileName): pass
    except IOError:
        print("File '" + fileName + "' doesn't exist. Exiting.")
        exit()
   
    hypothesis = importHypothesisFromFile(fileName)
    
    printHeader()
    for lineNumber, values in enumerate(hypothesis):
        print("{:03}#".format(lineNumber+1), end = "")
        printHausdorffDistanceValues(values)