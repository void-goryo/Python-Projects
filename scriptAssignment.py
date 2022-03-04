
#
#   Python:     3.10.2
#
#   Author:     Gabriel Jones
#
#   Purpose:    The Tech Academy has challenged me to make a program
#               that will find all .txt files using an absolute path,
#               print the files, and display there dates
#
#

import os
import time     #to make it a little more readable

fPath = 'C:\\Users\\Gabe\\Desktop\\findMe'

fConc = os.path.join(fPath, 'cheese.txt')    #change to username on computer
fTime = os.path.getmtime(fConc)
realTime = time.ctime(fTime)
fList = os.listdir(fPath)

def fileName():
    for i in fList:
        if '.txt' in i:
            print(i)



if __name__ == '__main__':
    print(fConc)
    print(realTime)
    fileName()
