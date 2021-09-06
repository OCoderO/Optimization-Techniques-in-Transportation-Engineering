from test import Test
import utils

import network

class MaxFlowData:
    
    def __init__(self, argumentList):
        self.network = network.Network(argumentList[0], argumentList[1])
        self.source = int(argumentList[2])
        self.sink = int(argumentList[3])
        
class MaxFlowAnswer:        

    def __init__(self, answerLines, numNodes):
        self.totalFlow = float(answerLines[0])
        self.x = list()
        for i in range(numNodes):
            self.x.append([0] * numNodes)
        for line in answerLines[1:]:
            i,j,x = line.split(",")
            self.x[int(i)][int(j)] = float(x)

class MaxFlowTest(Test):
   
    def __init__(self, testFileName):
        super().__init__(testFileName)
        self.testName = "max flow"
        
    def testFileProcessor(self, cleanLines):
        self.pointsPossible = int(cleanLines[0])
        self.data = MaxFlowData(cleanLines[1:5])
       
        self.answer = MaxFlowAnswer(cleanLines[5:], self.data.network.numNodes)

    def testRunner(self):
        self.studentB, self.studentX = \
                                self.data.network.maxFlow(self.data.source,
                                                          self.data.sink)
            
    def testChecker(self):
        correctFlows = 0
        numAnswers = 0
        for i in range(self.data.network.numNodes):
            for j in range(self.data.network.numNodes):
                if self.data.network.matrix[i][j] == 0:
                    continue
                numAnswers += 1
                if utils.approxEqual(self.studentX[i][j],
                                     self.answer.x[i][j]):
                    correctFlows += 1
        if correctFlows < numAnswers:
            print("Wrong labels:")
            print("Tail, head, correct value, your value:")
            for i in range(self.data.network.numNodes):
                for j in range(self.data.network.numNodes):             
                    if self.data.network.matrix[i][j] != 0:
                        print("%d,%d,%f,%f" % (i, j,
                                               self.answer.x[i][j],
                                               self.studentX[i][j]))
            print("...fail")
        
        if utils.approxEqual(self.studentB, self.answer.totalFlow):
            correctFlows += 1
        else:
            print("Wrong total flow: correct value is %d, you answered %f" %
                  (self.answer.totalFlow, self.studentB))
            print("...fail")          
            
        if correctFlows == numAnswers + 1:           
            print("...pass")
        return round(self.pointsPossible * 
                         (correctFlows / float(numAnswers + 1)), 
                     1)       