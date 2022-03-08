

#parent class

class Organism:
    name = 'unknown'
    species = 'unknown'
    legs = None
    arms = None
    dna = 'Sequence A'
    origin = 'unknown'
    carbonBased = True

    def information(self):
        msg = '\nName: {}\nLegs: {}\nArms: {}\nDNA: {}\nOrigin: {}\nCarbon Based: {}'.format\
                (self.name, self.species, self.legs, self.arms, self.dna, self.origin, self.carbonBased)
        return msg


#child class

class Human(Organism):
    name = 'Gabe'
    species = 'Human'
    legs = 2
    arms = 2
    origin = 'Earth'

    def friends(self):
        msg = '\nCreates friends with other species'
        return msg


#child class

class Dog(Organism):
    name = 'Max'
    species = 'Canine'
    legs = 4
    arms = 0
    dna = 'Sequence B'
    origin = 'Earth'

    def bite(self):
        msg = '\nEmits a loud growl and bites down on an unfortunate soul'
        return msg

class Cat:
    def __init__(cat, age, lives):
        cat.age = age
        cat.lives = lives

cat1 = Cat(9, 3)







if __name__ == '__main__':
    human = Human()
    print(human.information())
    print(human.friends())
    dog = Dog()
    print(dog.information())
    print(dog.bite())
    print(cat1.age, cat1.lives)
