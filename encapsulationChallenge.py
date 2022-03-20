class Protect:
    def __init__(self):
        self._protectedVar = 0

class Private:
    def __init__(self):
        self.__privateVar = 12

    def getPrivate(self):
        print(self.__privateVar)


if __name__ == '__main__':
    obj1 = Protect()
    obj2 = Private()
    print(obj1._protectedVar)
    obj2.getPrivate()
