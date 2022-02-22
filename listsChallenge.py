listA = ['this', 'is', 'a', 'list']

for i in listA:
    print(i)

listA.append('ok?')

for i in listA:
    print(i)
listB = listA.copy()

listC = listA + listB

listC.sort(reverse = True)
print(listC)
