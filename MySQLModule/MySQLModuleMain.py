
'''
Created on 25 Tem 2012

@author: Umut Gultepe
'''
import sys
import MySQLdb as mdb


ip='67.228.247.186'
dbName= 'alpsayin_idtest'
con = None
currentTable=None;


def checkPassword(username,password):
     """Function for logging into the database"""   
     global con    
     try:
         con = mdb.connect(ip, username,password, dbName)
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
    ----FOR INTERNAL USE ONLY----"""    
    cur = con.cursor()
    try:
        cur.execute("INSERT INTO Categories(Category_Name) VALUES('%s')" % category)      
    except mdb.Error, e: 
        print "Error %d: %s" % (e.args[0],e.args[1])
        con.rollback()
        sys.exit(1)
    finally:    
        print  "%s categeory pushed!" % cur.rowcount;
        con.commit()
    
def pullCategories():
    """Function to fetch the list of all categories"""
    cur=con.cursor(mdb.cursors.DictCursor)
    
    try: 
        cur.execute("SELECT * FROM Categories")
    except mdb.Error, e: 
        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)
    finally:    
        print "pulled categories:"
        rows = cur.fetchallDict()
        for row in rows:
            print "%s %s" % (row["ID"], row["Category_Name"])
 
def closeConnection(): 
    """Used to close the ongoing connection"""  
    con.close()
            
def clearCategories():
    """Used to clear the categories table
    WARNING: USE WITH CAUTION!!!"""
    
    cur = con.cursor()
    try: 
        cur.execute("DELETE FROM Categories")
    except mdb.Error, e: 
        print "Error %d: %s" % (e.args[0],e.args[1])
        con.rollback()
        sys.exit(1)
    finally:    
        print  "%s categeories deleted!" % cur.rowcount;
        con.commit()


def pullAll():
    """Pulls all of the log entries from the database
    ---WARNING: HIGH DATA TRANSFER POSSIBLE-CONSIDER USING pullLast function instead"""
    
    cur=con.cursor()
    try: 
        cur.execute("SELECT * FROM Log")
    except mdb.Error, e: 
        print "Error %d: %s" % (e.args[0],e.args[1])
        con.rollback()
        sys.exit(1)
    finally:  
        printResult(cur) 
        
   
def printResult(currentCursor):
    
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
   
    
            
def pullLast(count):
    """Pulls a number of the latest log entries from the database
    input    : The number of log entries to be downloaded """
    cur=con.cursor()
    try: 
        cur.execute("SELECT * FROM Log ORDER BY ID Desc LIMIT %d" % count)
    except mdb.Error, e: 
        print "Error %d: %s" % (e.args[0],e.args[1])
        con.rollback()
        sys.exit(1)
    finally:  
        printResult(cur)          

def pushNewMessage(category,content,preceededBy=None):
    cur = con.cursor()
    cur.execute("INSERT INTO Writers SET Name = %s WHERE Id = %s", ("Guy de Maupasant", "4")) 

  
    
    

print "beginning..."
connection=checkPassword('alpsayin_test','sayin')
if connection is 1:
    print "initiating process..."
    #pushCategory('IdLog')
    #clearCategories()
    #pullCategories()
    pullAll()
    #pullLast(1)
    print "closing connection"
    closeConnection()
print "program completed..."      