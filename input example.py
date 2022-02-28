mySentence = 'loves the color'
colorList = ['Red','Orange','Yellow','Green','Blue','Purple','Pink']

def colorFunction(name):
    lst = []
    for i in colorList:
        msg = '{} {} {}'.format(name,mySentence,i)
        lst.append(msg)
    return lst

def getName():
    go = True
    while go:   #while go = True
        name = input('What is your name? ')
        if name == '':
            print('You need to provide a name!')
        elif name == 'Sally':
            print('{}, You may not use this software'.format(name))
        else:
            go = False   
    lst = colorFunction(name)
    for i in lst:
        print(i)

getName()


fname = input('What was your first name again?\t')      #\t is tab, \n is new line, \\ is backslash, \' single quote, \" double quote, \b backspace
