import os
import sys
from support import sub

def callFun():
    
    print('This is callFun.')
    print('python install at: ', os.path.dirname(sys.executable))
    
    Obj = sub('Yash')
    Obj.getMsg()
    
if __name__ == "__main__":
    callFun()