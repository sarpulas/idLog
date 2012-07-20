#aaaa

import getpass

def tool(n):

  namelist = ['osman','mahmut','sarpulas']
  pwlist = ['namso','tumham','salupras']
  
  username = raw_input('Enter username:\n')
  print "uname ", username;
  if username in namelist:
      i = namelist.index(username)
      pw = getpass.getpass(prompt='Enter password:\n')
      if pw == pwlist[int(i)]:
        print('GREAT SUCCESS')
      else:
        print('FAIL')
  else:
      print('NAME NOT FOUND')
  

if __name__ == "__main__":
    import sys
    tool(1)