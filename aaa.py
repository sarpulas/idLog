#aaaa

import getpass
import datetime

def tool(n):

  namelist = ['osman','mahmut','sarpulas']
  pwlist = ['namso','tumham','salupras']
  
  username = raw_input('Enter username:\n')
  print "uname: ", username;
  if username in namelist:
      i = namelist.index(username)
      pw = getpass.getpass(prompt='Enter password:\n')
      if pw == pwlist[int(i)]:
        print('password correct')
        openlist(username)
      else:
        print('FAIL')
  else:
      print('NAME NOT FOUND')
  
def openlist(username):
  f=open('log.txt','r')
  try: 
    for line in f:
      print line
  finally:
    f.close()
    input = raw_input('Write task title if you want to add a new tast. Write \'exit\' to quit\n')
    if input == 'exit':
      print('quitting...')
    else:
      newtask(username,input)
      
def newtask(username, input):
  taskdesc = raw_input('Input task description:\n')
  f = open('log.txt', 'a')
  f.write('\n'+username +' | '+ datetime.datetime.__str__(datetime.datetime.now())+' | '+ input +' | '+ taskdesc);
  f.close
  print('task: \''+input+'\' added')
  openlist(username)
  
if __name__ == "__main__":
    import sys
    tool(1)