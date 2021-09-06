from test import Test
import utils

import network

class ShortestPathData:
    
    def __init__(self, argumentList):
        self.network = network.Network(argumentList[0], argumentList[1])
        self.origin = int(argumentList[2])
        
class ShortestPathAnswer:        

    def __init__(self, answerLines):
        self.backnode = list()
        self.cost = list()
        for line in answerLines:
            labels = line.split(",")
            self.backnode.append(int(labels[0]))
            self.cost.append(float(labels[1]))

class ShortestPathTest(Test):
   
    def __init__(self, testFileName):
        super().__init__(testFileName)
        self.testName = "shortest path"
        
    def testFileProcessor(self, cleanLines):
        self.pointsPossible = int(cleanLines[0])
        self.data = ShortestPathData(cleanLines[1:4])
       
        self.answer = ShortestPathAnswer(cleanLines[4:])

    def testRunner(self):
        self.studentQ, self.studentL = \
                                self.data.network.shortestPath(self.data.origin)
            
    def testChecker(self):
        correctLabels = 0
        for i in range(self.data.network.numNodes):
            correctLabels += 1 if self.studentQ[i] == self.answer.backnode[i] \
                               else 0
            correctLabels += 1 if utils.approxEqual(self.studentL[i],
                                                    self.answer.cost[i]) \
                               else 0      

        if correctLabels < 2 * self.data.network.numNodes:
            print("Wrong labels; correct values were:")
            print(self.answer.backnode)
            print(self.answer.cost)
            print("Your answers were:")
            print(self.studentQ)
            print(self.studentL)
            print("...fail")
        else:           
            print("...pass")
        return round(self.pointsPossible * 
                         (correctLabels / float(2*self.data.network.numNodes)), 
                     1)       