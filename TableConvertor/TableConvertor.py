"""
Table Convertor Module
exports mysql Tables to different types of files
"""

from openpyxl.workbook import Workbook
from openpyxl.writer.excel import ExcelWriter

from openpyxl.cell import get_column_letter

def saveAsTXT(table, path):
    try:
        outputFile = open(path, 'w+')
        
        outputFile.close()
    except:
        print 'Output file could not be opened'
    return

def saveAsXLSX(table, path):
    wb = Workbook()
    entrySheet = wb.worksheets[0]
    entrySheet.title = 'Entries'
    entrySheet.cell('A1').value = 'Alp'
    
    for col_idx in xrange(1, 40):
        col = get_column_letter(col_idx)
        for row in xrange(1, 600):
            entrySheet.cell('%s%s'%(col, row)).value = '%s%s' % (col, row)
    
    wb.create_sheet()
    catSheet = wb.worksheets[1]
    catSheet.title = 'Categories'
    catSheet.cell('A1').value = 'Sayin'
    
    wb.save(filename = path)
    
    return

def saveAsPDF(table, path):
    return

def saveAsXML(table, path):
    return

def saveAsHTML(table, path):
    return

if __name__ == "__main__":
    print 'hello'
    saveAsXLSX('alp', 'alp.xlsx')
    print 'bye bye'