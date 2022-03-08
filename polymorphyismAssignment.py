

class Pet:
    legs = 'Unknown'
    age = None
    hair = 'Unknown'
    
    def info(self):
        msg = '\nNumber of legs: {}\nPet age: {}\nHair type: {}'.format\
              (self.legs, self.age, self.hair)
        return msg


class Dog(Pet):
    legs = 4
    hair = 'short hair'
    ownerName = 'Gabe'
    dogBreed = 'Black Lab'
    
    def owner(self):
        msg = '\nOwner Name: {}\nDog breed: {}'.format(self.ownerName, self.dogBreed)
        return msg

class Cat(Pet):
    legs = 4
    age = 3
    hair = 'short hair'
    ownerName = 'Emily'
    catName = 'Lucky'
    
    def owner(self):
        msg = '\nOwner Name: {}\nCat name: {}'.format(self.ownerName, self.catName)
        return msg

        
if __name__ == '__main__':
    dog = Dog()
    cat = Cat()
    print(dog.info())
    print(dog.owner())
    print(cat.info())
    print(cat.owner())
