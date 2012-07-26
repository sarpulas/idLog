'''
Created on Jul 26, 2012

@author: Alp Sayin
'''

class idLogTable():
    '''
    A Simple Class to keep tables with fixed column size
    members:
        _rows : list of lists
        _cols : list of strings
    '''
    def __init__(self, headers_list):
        '''
        Constructor
        Only initializes _rows and _cols
        parms:
            headers_list: a list containing the header titles
        '''
        self._rows = []
        self._cols = headers_list
        
    def __str__(self):
        """
        __str__
        returns a string representation of the table
        """
        strn = ''
        for i in range(len(self._cols)):
            strn = strn + str(self._cols[i])+'\t\t'
        print
        for i in range(len(self._rows)):
            if(len(self._rows[i]) != 0):
                for j in range(len(self._cols)):
                        strn = strn + str(self._rows[i][j])+'\t\t'
                strn = strn + '\n'
            else:
                strn = strn + '-\n'
        return strn
    
    def __len__(self):
        """
        __len__
        return the number of rows
        """
        return len(self._rows)
        
    def addRow(self, rowList, index=-1):
        """
        addRow(rowList, index=-1)
        parms:
            rowList: a rowList which contains the row information, its size must be the same
                as the number of columns or an exception will be thrown
            index: the index that the row should be inserted
                if the index is greater than the num of existing rows, empty rows will be inserted between
                if the index is less then 0, then the row will be appended.
                if the index is less then num of existing rows, row will be updated
        """
        if(len(rowList) != len(self._cols)):
            raise Exception('Row-Length vs. NumOfColumns size mismatch')
        if(index < 0):
            self._rows.append(rowList)
        else:
            if(index > len(self._rows)):
                while(len(self._rows) <= index):
                    self._rows.append([])
            self._rows[index] = rowList

    def getRow(self, index):
        """
        getRow(index)
        parms:
            index: index of the row to be returned
        returns:
            array containing the row
        """
        return self._rows[index]
    
    def removeRow(self, num):
        """
        removeRow(index)
        parms:
            index: index of the row to be removed
        """
        self._rows.remove(self._rows[num])
    
    def setHeaders(self, headerList):
        """
        setHeaders(headerList)
        parms:
            headerList: a headerList containing the new header information, the size must be
                the same as the existing headers, else an exception will be thrown
        """
        if(len(self._cols) != len(headerList)):
            raise Exception('setHeaders column size mismatch')
        self._cols = headerList
        
    def getHeaders(self):
        """
        getHeaders()
        returns:
            a list containing the headers
        """
        return self._cols
    
    def getHeadersLength(self):
        """
        getHeadersLength()
        returns:
            return the length of the headers array
        """
        return len(self._cols)
    
    def printTable(self):
        """
        printTable()
        prints the table to stdout
        """
        for i in range(len(self._cols)):
            print self._cols[i]+'\t\t',
        print
        for i in range(len(self._rows)):
            if(len(self._rows[i]) != 0):
                for j in range(len(self._cols)):
                        print str(self._rows[i][j])+'\t\t',
                print
            else:
                print '-'
        
    
if __name__ == '__main__':
    dummyTable = idLogTable(['id', 'username', 'category', 'blabla'])
    print dummyTable.getHeaders(), dummyTable.getHeadersLength()
    dummyTable.setHeaders(['id', 'username', 'category', 'content'])
    print dummyTable.getHeaders(), dummyTable.getHeadersLength()
    dummyTable.addRow([1, 'alpsayin', 'farnell', 'raspberry pi siparisleri verildi'])
    dummyTable.printTable()
    dummyTable.addRow([2, 'alpsayin', 'farnell', 'raspberry pi siparisleri elimize ulasti'])
    dummyTable.addRow([3, 'umutgultepe', 'g-man', 'some entry'], 6)
    dummyTable.printTable()
    dummyTable.removeRow(2)
    
    print str(dummyTable)
    print len(dummyTable)
    
    