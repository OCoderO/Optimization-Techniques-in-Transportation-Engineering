import sys
import traceback

NO_PATH_EXISTS = -1
INFINITY = 99999

IS_MISSING = -1

def approxEqual(value, target, tolerance = 0.01):
    if (abs(target) <= tolerance ):
        return abs(value) <= tolerance
    return abs(float(value) / target - 1) <= tolerance
    
def check(name, value, target, tolerance = 0.01):
    if approxEqual(value, target, tolerance):
        return True
    else:
        print("\nWrong %s: your value %f, correct value %f"
                    % (name, value, target))
        return False

class NotYetAttemptedException(Exception):
    pass

def cleanLines(rawLines, commentCharacter = "#"):
    """
    Given a list of strings, returns a "clean" version with whitespace
    stripped, blank lines removed, and comments removed.  
    """
    cleanedLines = list()
    
    for line in rawLines:
        # Ignore comments and blank lines
        cleanLine = line.strip().split(commentCharacter)[0]
        if len(cleanLine) > 0:
            cleanedLines.append(cleanLine)

    return cleanedLines

def processFile(fileName, commentCharacter = "#"):
    """
    Reads all lines from a text file, then cleans them.
    """
    try:
        with open(fileName, "r") as textFile:
            rawLines = textFile.read().splitlines()
            cleanedLines = cleanLines(rawLines)
            return cleanedLines
        
    except IOError:
        print("\nError reading network file %s" % networkFile)
        traceback.print_exc(file=sys.stdout)
