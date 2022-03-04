import os


fname = 'hello.txt'

fPath = 'C:\\Users\\Gabe\\Desktop\\Python'

abPath = os.path.join(fPath, fname)
print(abPath)

def writeData():
    data = 'Hello!!'
    with open('test.txt', 'a') as f:
        f.write(data)
        f.close()


def openFile():
    with open('test.txt', 'r') as f:
        data = f.read()
        print(data)
        f.close()   #no memory leaks



if __name__ == '__main__':
    writeData()
    openFile()
