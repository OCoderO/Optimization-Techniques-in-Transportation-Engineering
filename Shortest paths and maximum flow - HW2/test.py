import sys
import traceback
import utils

"""
Generic class for running tests; each specific type of test should be built
by creating a derived class with the appropriate initializer, reader, runner,
and checker.
"""
class Test:

    def __init__(self, testFileName = None):
        self.testName = None
        self.testFileName = testFileName
        self.pointsPossible = 0

    def testFileProcessor(self, cleanLines):
        pass

    def testRunner(self):
        pass

    def testChecker(self):
        pass

    def doTest(self):
        try:
            print("Running " + self.testName + " test: " +
                  str(self.testFileName) + "...", end='')
            self.readTestFile()
            if self.data == utils.IS_MISSING:
                raise IOError

            try:
                self.testRunner()
            except utils.NotYetAttemptedException:
                print("...not yet attempted")
                return 0, self.pointsPossible
            self.points = self.testChecker()
            return self.points, self.pointsPossible
        
        except IOError:
            print("\nError running test %s, attempting to continue"
                  "with remaining tests.   Exception details: "
                  % self.testFileName)
            traceback.print_exc(file=sys.stdout)
            return 0, 0
        except:
            print("\nException raised, attempting to continue:")
            traceback.print_exc(file=sys.stdout)                            
            print("\n...fail")
            return 0, self.pointsPossible            
 
    def readTestFile(self):
        with open(self.testFileName, "r") as testFile:
            # Read test information
            fileLines = testFile.read().splitlines()
            cleanLines = list()
            for line in fileLines:
                cleanLine = line.strip().split("#")[0]
                if len(cleanLine) > 0:
                    cleanLines.append(cleanLine)
                
            # Read problem data
            self.testFileProcessor(cleanLines)

