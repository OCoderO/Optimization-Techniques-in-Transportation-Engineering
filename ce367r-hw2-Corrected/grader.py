from collections import OrderedDict
import os
import sys

import test

from shortestPathTest import ShortestPathTest
from maxFlowTest import MaxFlowTest


def runTests(testClass, testDirectory, isExtraCredit = False):
    score = 0
    possible = 0
    testFileName = os.path.normpath(testDirectory + "tests.txt")
    
    try:
        testList = open(testFileName).read().splitlines()
    except Exception as e:
        print("Error running tests from path %s, attempting to continue with"
              "remaining tests.   Exception details: " % testDirectory)
        print(e)
        return 0, 0
        
    for testFile in testList:
        # Ignore comments and blank lines
        testFile = testFile.strip().split('#')[0]
        if len(testFile) == 0:
            continue
                
        test = testClass(testDirectory + testFile)
        testScore, testPossible = test.doTest()
        score += testScore
        possible += testPossible        
    
    return score, possible if isExtraCredit == False else 0
    
def displayScores(scores):
    longestQuestion = len(max(scores.keys(), key=len))
    totalScore = 0
    totalPossible = 0
    print("")
    print("SCORES: ")
    for question in scores.keys():
        totalScore += scores[question][0]
        totalPossible += scores[question][1]
        print("%s %d/%d" % (question.ljust(longestQuestion),
                            scores[question][0], scores[question][1]))
    print("----------")
    print("%s %d/%d" % ("TOTAL: ".ljust(longestQuestion), totalScore,
                        totalPossible))
    print("")
    print("This is an unofficial score, please submit code on Canvas for final"
          "scoring.")
    print("")
    
if __name__ == '__main__':
    
    scores = OrderedDict()
 
    scores['Q1: Shortest path']=runTests(ShortestPathTest,"tests/shortestPath/")

    scores['Q2: Max flow']=runTests(MaxFlowTest,"tests/maxFlow/", True)
    
    displayScores(scores)
    sys.exit()
    
    

