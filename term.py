def getTerminalSize():
    import os
    rows, columns = os.popen('stty size', 'r').read().split()
    return (rows,columns)
    
def setTerminalSize(row, column):
    import sys
    sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=row, cols=column))