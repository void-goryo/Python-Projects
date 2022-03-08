

class Pet:
    legs = None
    age = None
    hair = None


class Dog(Pet):
    legs = 4
    hair = 'short hair'
    ownerName = 'Gabe'

class Cat(Pet):
    legs = 4
    age = 3
    hair = 'short hair'
    ownerName = 'Emily'
    catName = 'Lucky'

if __name__ == '__main__':
    print(Dog.ownerName)
    print(Cat.legs)
