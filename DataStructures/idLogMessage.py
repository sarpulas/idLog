'''
Created on Jul 26, 2012

@author: Alp Sayin
'''

from datetime import datetime

class idLogMessage():
    '''
    A simple class to keep log messages
    members:
        _id : int
        _user : string
        _creationdate : datetime
        _lastmodified : datetime
        _category : string
        _content : string
        _preeceededby : int list
        _succeededby : int list
        _active : boolean
    '''
    def __init__(self, info_list):
        '''
        Constructor
        '''
        self._id = int(info_list[0])
        self._user = info_list[1]
        self._creationdate = info_list[2]
        self._lastmodified = info_list[3]
        self._category = info_list[4]
        self._content = info_list[5]
        self._preceededby = info_list[6]
        self._succeededby = info_list[7]
        self._active = info_list[8]
        
    def __str__(self):
        infolist = [self._id, self._user, str(self._creationdate), str(self._lastmodified), self._category, self._content, self._preceededby, self._succeededby, self._active]        
        return str(infolist)
    
    def getId(self):
        return self._id
    
    def getUser(self):
        return self._user
    
    def getCreationDate(self):
        return self._creationdate
    
    def getLastModified(self):
        return self._lastmodified
    
    def getCategory(self):
        return self._category
    
    def getContent(self):
        return self._content
    
    def getPreceededBy(self):
        return self._preceededby
    
    def getSucceededBy(self):
        return self._succeededby
    
    def isActive(self):
        return self._active
    
    def setActive(self, active):
        self._active = active
    
    def setUser(self, username):
        self._user = username
        
    def setCreationDate(self, creationdate):
        self._creationdate = creationdate
    
    def setCategory(self, category):
        self._category = category
        
    def setContent(self, content):
        self._content = content
        
    def addPreceededBy(self, pid):
        if(pid not in self._preceededby):
            self._preceededby.append(pid)
        
    def removePreceededBy(self, pid):
        if(pid in self._preceededby):
            self._preceededby.remove(pid)
    
    def addSucceededBy(self, sid):
        if(sid not in self._succeededby):
            self._succeededby.append(sid)
    
    def removeSuccededBy(self, sid):
        if(sid in self._succeededby):
            self._succeededby.remove(sid)
            
    def getAsList(self):
        infolist = [self._id, self._user, self._creationdate, self._lastmodified, self._category, self._content, self._preceededby, self._succeededby, self._active]        
        return infolist
    
if( __name__ == '__main__'):
    print 'hello'
    sampleMessageList = [1, 'alpsayin', datetime.now(), datetime.now(), 'some cate', 'some content', [0], [2], True]
    m = idLogMessage(sampleMessageList)
    print m.getPreceededBy()
    print m.getSucceededBy()
    m.addPreceededBy(-2)
    m.addPreceededBy(-2)
    m.addSucceededBy(12)
    print m.getPreceededBy()
    print m.getSucceededBy()
    m.removePreceededBy(5)
    m.removeSuccededBy(12)
    print m.getPreceededBy()
    print m.getSucceededBy()
    print m
    print 'bye bye'