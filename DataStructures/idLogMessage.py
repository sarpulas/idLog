'''
Created on Jul 26, 2012

@author: Alp Sayin
'''

from datetime import datetime

class idLogMessage():
    """
    A simple class to keep log messages
    members:
        _id : int
        _user : string
        _creationdate : datetime
        _lastmodified : datetime
        _category : string
        _content : string
        _precededby : int list
        _succeededby : int list
        _active : boolean
    """
    def __init__(self, info_list):
        """
        Constructor
        initializes a message instance from the info_list list
        self._id = int(info_list[0])
        self._user = info_list[1]
        self._creationdate = info_list[2]
        self._lastmodified = info_list[3]
        self._category = info_list[4]
        self._content = info_list[5]
        self._precededby = info_list[6]
        self._succeededby = info_list[7]
        self._active = info_list[8]
        """
        self._id = int(info_list[0])
        self._user = info_list[1]
        self._creationdate = info_list[2]
        self._lastmodified = info_list[3]
        self._category = info_list[4]
        self._content = info_list[5]
        self._precededby = info_list[6]
        self._succeededby = info_list[7]
        self._active = info_list[8]
        
    def __str__(self):
        """
        __str__
        returns a string representation of the instance
        """
        infolist = [self._id, self._user, str(self._creationdate), str(self._lastmodified), self._category, self._content, self._precededby, self._succeededby, self._active]        
        return str(infolist)
    
    def getId(self):
        """
        getId()
        returns the id of the message
        """
        return self._id
    
    def getUser(self):
        """
        getUser()
        returns the committing user of the message
        """
        return self._user
    
    def getCreationDate(self):
        """
        getCreationDate()
        returns the datetime instance representing the creation date of the message
        """
        return self._creationdate
    
    def getLastModified(self):
        """
        getLastModified()
        returns the datetime instance representing the last modification date of the message
        """
        return self._lastmodified
    
    def getCategory(self):
        """
        getCategory()
        return the category string
        """
        return self._category
    
    def getContent(self):
        """
        getContent()
        returns the content string
        """
        return self._content
    
    def getPrecededBy(self):
        """
        getPrecededBy()
        returns a list of integers containing the messages that precedes this message
        """
        return self._precededby
    
    def getSucceededBy(self):
        """
        getSucceededBy()
        returns a list of integers containing the messages that succeeds this message
        """
        return self._succeededby
    
    def isActive(self):
        """
        isActive()
        returns a boolean indicating the status of the message
        """
        return self._active
    
    def setActive(self, active):
        """
        isActive()
        sets the active field to the input boolean value
        """
        self._active = active
    
    def setUser(self, username):
        """
        setUser(username)
        parms:
            username: string containing the new username
        """
        self._user = username
        
    def setCreationDate(self, creationdate):
        """
        setCreationDate(creationdate)
        parms:
            creationdate : datetime instance to set creationdate
        """
        self._creationdate = creationdate
    
    def setCategory(self, category):
        """
        setCategory(category)
        parms:
            category : string to set category
        """
        self._category = category
        
    def setContent(self, content):
        """
        setContent(content)
        parms:
            content : string to set content
        """
        self._content = content
        
    def addPrecededBy(self, pid):
        """
        addPrecededBy(pid)
        add pid to the preceded by list, of the id exists a duplicate is not added
        parms:
            pid : integer id to add to the list
        """
        if(pid not in self._precededby):
            self._precededby.append(pid)
        
    def removePrecededBy(self, pid):
        """
        removeSucceededBy(pid)
        remove the pid from the list, if the pid doesn't exist no error is thrown
        and nothing is done
        parms:
            pid : integer id to be removed from the list
        """
        if(pid in self._precededby):
            self._precededby.remove(pid)
    
    def addSucceededBy(self, sid):
        """
        addSucceededBy(sid)
        add sid to the succeeded by list, of the id exists a duplicate is not added
        parms:
            sid : integer id to add to the list
        """
        if(sid not in self._succeededby):
            self._succeededby.append(sid)
    
    def removeSuccededBy(self, sid):
        """
        removeSucceededBy(sid)
        remove the sid from the list, if the sid doesn't exist no error is thrown
        and nothing is done
        parms:
            sid : integer id to be removed from the list
        """
        if(sid in self._succeededby):
            self._succeededby.remove(sid)
            
    def getAsList(self):
        """
        getAsList()
        returns the message as a list containing the members
        infolist = [self._id, 
                    self._user, 
                    self._creationdate, 
                    self._lastmodified, 
                    self._category, 
                    self._content, 
                    self._precededby, 
                    self._succeededby, 
                    self._active]        
        """
        infolist = [self._id, self._user, self._creationdate, self._lastmodified, self._category, self._content, self._precededby, self._succeededby, self._active]        
        return infolist
    
if( __name__ == '__main__'):
    print 'hello'
    sampleMessageList = [1, 'alpsayin', datetime.now(), datetime.now(), 'some cate', 'some content', [0], [2], True]
    m = idLogMessage(sampleMessageList)
    print m.getPrecededBy()
    print m.getSucceededBy()
    m.addPrecededBy(-2)
    m.addPrecededBy(-2)
    m.addSucceededBy(12)
    print m.getPrecededBy()
    print m.getSucceededBy()
    m.removePrecededBy(5)
    m.removeSuccededBy(12)
    print m.getPrecededBy()
    print m.getSucceededBy()
    print m
    print 'bye bye'
