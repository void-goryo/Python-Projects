
def fname():
    fname = input('What is your first name? ')
    return fname

def lname():
    lname = input('What is your last name? ' )
    return lname


fname = fname()
lname = lname()

print('Hello {} {}, Welcome to Python!'.format(fname, lname))

c = format(8, 'b')
print(c)
print('this is a format {0:c} {0:b} {0:%}'.format(7))
