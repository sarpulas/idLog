'''
Created on Jul 26, 2012

@author: Alp Sayin
'''

class idLogTable():
    '''
    A Simple Class to keep tables with fixed column size
    '''
    def __init__(self, headers_vect):
        '''
        Constructor
        Only initializes _rows and _cols
        '''
        self._rows = []
        self._cols = headers_vect
        
    def addRow(self, vect, index=-1):
        if(len(vect) != len(self._cols)):
            raise Exception('Row Column size mismatch')
        if(index < 0):
            self._rows.append(vect)
        else:
            if(index > len(self._rows)):
                while(len(self._rows) <= index):
                    self._rows.append([])
            self._rows[index] = vect

    def getRow(self, num):
        return self._rows[num]
    
    def removeRow(self, num):
        self._rows.remove(self._rows[num])
    
    def setHeaders(self, vect):
        if(len(self._cols) != len(vect)):
            raise Exception('setHeaders column size mismatch')
        self._cols = vect
        
    def getHeaders(self):
        return self._cols
    
    def getHeadersLength(self):
        return len(self._cols)
    
    def printTable(self):
        for i in range(len(self._cols)):
            print self._cols[i]+'\t\t',
        print
        for i in range(len(self._rows)):
            for j in range(len(self._cols)):
                print str(self._rows[i][j])+'\t\t',
            print
        
    
if __name__ == '__main__':
    dummyTable = idLogTable(['id', 'username', 'category', 'blabla'])
    print dummyTable.getHeaders(), dummyTable.getHeadersLength()
    dummyTable.setHeaders(['id', 'username', 'category', 'content'])
    print dummyTable.getHeaders(), dummyTable.getHeadersLength()
    dummyTable.addRow([1, 'alpsayin', 'farnell', 'raspberry pi siparisleri verildi'])
    dummyTable.printTable()
    dummyTable.addRow([2, 'alpsayin', 'farnell', 'raspberry pi siparisleri elimize ulasti'])
    dummyTable.addRow([3, 'umutgultepe', 'g-man', 'some entry'])
    dummyTable.printTable()
    dummyTable.removeRow(2)
    dummyTable.printTable()
    
    