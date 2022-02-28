
mySentence = 'loves the color'
colorList = ['Red','Orange','Yellow','Green','Blue','Purple','Pink']

def colorFunction(name):
    lst = []
    for i in colorList:
        msg = '{} {} {}'.format(name,mySentence,i)
        lst.append(msg)
    return lst

lst = colorFunction('Gabe')
for i in lst:
    print(i)

y = lambda x: x + x     #single line function

print(y(2))

def getSum(num1, num2):
    answer = num1 + num2
    print('The answer is {}.'.format(answer))

getSum(2,4)
