
'''
Created on 25 Tem 2012

@author: Umut Gultepe
'''
import sys
import MySQLdb as mdb


ip='67.228.247.186'
dbName= 'alpsayin_idtest'


def checkPassword(username,password):
    
    con = None
    
    try:
        con = mdb.connect(ip, username,password, dbName)

    except mdb.Error, e: 
        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)
    finally:    
            
        if con:    
            print "fuck yeah"
            con.close()
            return 1
        else:
            return 0
        
        
print "beginning..."
checkPassword('alpsayin_test','sayin')
print "complete..."      