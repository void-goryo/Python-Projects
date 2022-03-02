

import app1

def printApp2():
    name = (__name__)
    return name

if __name__ == '__main__':
    ##This is calling code from within this script
    print('I am running code from {}'.format(printApp2()))

    ##This is calling code from the imported app
    print('I am running code from {}'.format(app1.printApp()))

