"""
Table Convertor Module
exports mysql Tables to different types of files
"""

def saveAsTXT(table, path):
    try:
        outputFile = open(path, 'w+')
        
        outputFile.close()
    except:
        print 'Output file could not be opened'
    return

def saveAsXLSX(table, path):
    return

def saveAsPDF(table, path):
    return

def saveAsXML(table, path):
    return

def saveAsHTML(table, path):
    return