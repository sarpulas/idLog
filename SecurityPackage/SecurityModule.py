'''
Created on Jul 26, 2012

@author: Alp Sayin
'''

import hashlib

def strToHash(inputStr, algorithm='sha512'):
    """
    hashStr(inputStr, algorithm='sha512')
    hashes a string with a given algorithm, default is sha512
    """
    hasher = hashlib.new(algorithm)
    hasher.update(inputStr)
    return hasher.hexdigest()
    
if(__name__ == '__main__'):
    someString = 'Alp Sayin\n'
    print strToHash(algorithm='sha256', inputStr=someString)