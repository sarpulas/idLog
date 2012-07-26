
'''
Created on 25 Tem 2012

@author: Umut Gultepe
'''
import sys
import MySQLdb as mdb
from datetime import datetime
import idLogTable
"""Tables in tha database should be as following:

Log Table
    #     Sütun         Türü            Karþýlaþtýrma   Öznitelikler                    Boþ      Varsayýlan           Ekstra   
     1    ID            int(11)                                                         Hayýr    Yok                  AUTO_INCREMENT  
     2    User          varchar(64)     utf8_unicode_ci                                 Hayýr    USER()             
     3    CreationDate  timestamp                                                       Hayýr    0000-00-00 00:00:00     
     4    LastModified  timestamp                       on update CURRENT_TIMESTAMP     Hayýr    CURRENT_TIMESTAMP    ON UPDATE CURRENT_TIMESTAMP      
     5    Category      int(11)                                                         Hayýr    Yok       
     6    Content       varchar(2048)   utf8_unicode_ci                                 Hayýr    Yok        
     7    PreceededBy   int(11)                                                         Evet     NULL       
     8    SucceededBy   int(11)                                                         Evet     NULL       
     9    ActiveFlag    tinyint(1)                                                      Hayýr    1          

Category Table
          Sütun            Türü           Karþýlaþtýrma      Boþ        Varsayýlan     Ekstra  
     1    ID               int(11)                           Hayýr      Yok            AUTO_INCREMENT     
     2    Category_Name    varchar(64)    utf8_unicode_ci    Hayýr      Yok           

"""

ip='67.228.247.186'
dbName= 'alpsayin_idtest'
con = None
currentTable=None
userName=None

def checkPassword(user,password):
     """Function for logging into the database"""   
     global con    
     global userName
     userName=user
     try:
         con = mdb.connect(ip, userName,password, dbName)
     except mdb.Error, e: 
        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)
     finally:    
            
        if con:    
            print "connected..."
            return 1
        else:
            return 0
               
def pushCategory(category):
    """Used to insert a new category to the table
    Returns the ID of the pushed Category
    ----FOR INTERNAL USE ONLY----"""    
    queryString="INSERT INTO Categories(Category_Name) VALUES('%s')" % category
    cur=executeQueryWithHandling(queryString)
    print  "%s categeory pushed!" % cur.rowcount;
    con.commit()    
    queryString="SELECT ID FROM Categories WHERE Category_Name='%s'" % category
    cur=executeQueryWithHandling(queryString)
    idRow=cur.fetchone()
    return idRow[0]

def pullCategories():
    """Function to fetch the list of all categories
    Returns the cursor of the categories"""
    queryString="SELECT Category_Name FROM Categories"
    cur=executeQueryWithHandling(queryString)
    #printResult(cur)
    return cur 
 
def closeConnection(): 
    """Used to close the ongoing connection"""  
    con.close()
            
def clearCategories():
    """Used to clear the categories table
    WARNING: USE WITH CAUTION!!!"""
    queryString="DELETE FROM Categories"
    cur=executeQueryWithHandling(queryString)
    print  "%s categeories deleted!" % cur.rowcount;
    con.commit()
    
def pullAll():
    """Pulls all of the log entries from the database
    ---WARNING: HIGH DATA TRANSFER POSSIBLE-CONSIDER USING pullLast function instead"""
    
    queryString="SELECT * FROM Log"
    cur=executeQueryWithHandling(queryString)
    return cur
         
def printResult(currentCursor):
    """Convenient method for printing the results of a query
    In the first row, prints the table headers.
    The results of the query are listed row by row below
    ---FOR INTERNAL USE ONLY---"""
    desc=currentCursor.description  
    for field in desc:
        print "%s \t" % field[0] ,
    print "\n"
    
    rows=currentCursor.fetchall()
    
    for row in rows:
        index=0
        for field in row:
            print "%s \t" % field,
            index+=1
        print "\n"
   
def executeQueryWithHandling(queryString): 
    """Executes an SQL Query with exception handling
    ---FOR INTERNAL USE ONLY---"""
    cur=con.cursor()
    try: 
        cur.execute(queryString)
    except mdb.Error, e: 
        print "Error %d: %s" % (e.args[0],e.args[1])
        con.rollback()
        sys.exit(1)
    finally:  
        return cur
          
def pullLast(count):
    """Pulls a number of the latest log entries from the database
    input    : The number of log entries to be downloaded """
    queryString="SELECT * FROM Log ORDER BY ID Desc LIMIT %d" % count
    cur=executeQueryWithHandling(queryString)
    return cur    

def pullSystemTime():
    """Used to acquire the system time
    Returns the current time stamp in string form"""
    queryString="SELECT CURRENT_TIMESTAMP"
    cur=executeQueryWithHandling(queryString)
    timeRow=cur.fetchone()
    return timeRow[0]

def getCategoryID(categoryName):
    """Returns the ID of a category specified with its name"""
    """Returns None if the category is not yet in the database"""
    categoryCursor=pullCategories()
    categoryRows=categoryCursor.fetchall()
    
    queryString=None
    
    for row in categoryRows:
        index=0
        for field in row:
            if field == categoryName:
                #print "found the category"                
                queryString="SELECT ID FROM Categories WHERE Category_Name='%s'" % field
                break
        if queryString is not None:
            break
        
    categoryCursor.close()
    if queryString is None:
        return None
    else:
        cur=executeQueryWithHandling(queryString)
        idRow=cur.fetchone()
        return idRow[0]
    
def pullByCategory(category,n=20):
    """Get a certain number of latest entries for a given category
    input    : the name of the category, 
               number of entries to be retrieved (default=20)"""
    id=getCategoryID(category)
    
    if id is None:
        return None
    
    queryString="SELECT * FROM Log WHERE CATEGORY = %s LIMIT %s" % (id,n)
    cur=executeQueryWithHandling(queryString)
    return cur
    
def pullNumOfEntries():
    """Method for geting the total number of entries"""
    queryString="SELECT COUNT(ID) FROM Log"
    cur=executeQueryWithHandling(queryString)
    return cur

def pullByDateRange(after,before):
    """Function to pull all the entries between two dates
    input: The earlier date limit (Enter as day/month/year)
         : The later date limit(Enter as day/month/year)""" 
    earlyValue = datetime.strptime(after, "%d/%m/%Y")
    lateValue = datetime.strptime(before, "%d/%m/%Y")
    print earlyValue
    queryString= "SELECT * FROM Log WHERE CreationDate > '%s' AND CreationDate < '%s'" % (earlyValue.strftime("%Y-%m-%d"),lateValue.strftime("%Y-%m-%d"))
    cur=executeQueryWithHandling(queryString)
    return cur

def pullByKeyword(keyword):
    """Searches the content of the messages for the given keyword.
    input : Keyword combination 
          : So far, only one keyword :D"""
    queryString="SELECT * FROM Log WHERE INSTR(Content,'%s') > 0" % keyword
    cur=executeQueryWithHandling(queryString)
    return cur
    
def pullByID(id):
    """Pull a log entry by its ID
    input: ID of the desired log entry"""
    queryString="SELECT * FROM Log WHERE ID = %s" % (id)
    cur=executeQueryWithHandling(queryString)
    return cur

def pushNewMessage(category,content,succeeding=None):
    """Used to push a new log message 
    input   : Category Name (New category will be created automatically if it is a new category
            : Content of the log entry
            : The preceeding entry ID, should be given in integer form."""   
    categoryID=getCategoryID(category)
    
    if categoryID is None:
        categoryID=pushCategory(category)
    
    curTime=pullSystemTime()
    print userName
    
    if succeeding is None:
        queryString="INSERT INTO Log(User,CreationDate,Category,Content) VALUES('%s','%s','%d','%s')" % (userName,curTime,categoryID,content)
        cur=executeQueryWithHandling(queryString)
        con.commit()
    else:
        queryString="INSERT INTO Log(User,CreationDate,Category,Content,PreceededBy) VALUES('%s','%s','%s','%s','%s')" % (userName,curTime,categoryID,content,succeeding)
        cur=executeQueryWithHandling(queryString)
        queryString="SELECT ID FROM Log WHERE CreationDate = '%s'" % curTime
        cur=executeQueryWithHandling(queryString)
        idRow=cur.fetchone()
        newID=idRow[0]
        queryString="UPDATE Log SET SucceededBy = %d WHERE ID = %d" % (newID,succeeding)
        cur=executeQueryWithHandling(queryString)
        con.commit()
        
def pullByUser(user,n=20):
    """Pull a number of latest entries by a given user.
    input   : The name of the user
            : The number of entries to be pulled (default is 20)"""
    queryString="SELECT * FROM Log WHERE User = '%s' ORDER BY ID Desc LIMIT %d" % (user,n)
    cur=executeQueryWithHandling(queryString)     
    return cur
    


print "beginning..."
connection=checkPassword('alpsayin_test','sayin')
if connection is 1:
    print "initiating process..."
    #print pushCategory('IdLogXY')
    #clearCategories()
    #print pullSystemTime()
    #pushNewMessage('IdLogX','TestRun5')
    cur=pullByUser(userName)
    printResult(cur)
    #print getCategoryID('test')
    #pullByCategory('test')
    #pullCategories()
    #pullAll()
    #pullLast(1)
    #pullByDateRange("24/07/2012","26/07/2012")
    #pullByKeyword('yeah f')
    #pullByID(1)
    print "closing connection"
    closeConnection()
print "program completed..."      