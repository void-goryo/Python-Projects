

def getInfo():
    var1 = input('\nplease provide the first numeric value ')
    var2 = input('\nplease provide the second numeric value ')
    return var1, var2


def compute():
    go = True
    while go:
        var1, var2 = getInfo()
        try:
            var3 = int(var1) + int(var2)
            go = False
        except ValueError:
            print('{} \n\nYou did not provide a numeric value!')
        except:
            print('oops, the program will now close.')
    print('{} + {} = {}'.format(var1, var2, var3))



if __name__ == '__main__':          #start to type this line on every bit of code
    compute()
