a = '''Is this,
multiple lines??'''

print(a)
print(a[3:7])       #the ':' means 'to'. the line says, 'print from 3 to 7
print(a[:9])        #skips up too 9. print from start to 9
print(a[-8:-5])     #only print after 5 to before 8. works backwards



b = (2, 5, 3, 6, 8,)
c = slice(0,5,1)    #start, end, step
print(b[c])

print(len(a))       #counts characters

d = '    this is a string with no space    '
print(d.strip(' ')) #only removes characters at the start and the end
e = d.upper()
print(e)

print('this' in a)  #prints true or false is 'this' is in the string

f = 'I just ' + '\t concatenated this string'   #\t is tab, \n is new line, \r is carriage return
print(f)

if e is not a:
    print(True)
if e in a:
    print(True)
else:
    print(False)
