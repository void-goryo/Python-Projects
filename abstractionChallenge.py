

from abc import ABC, abstractmethod
class car(ABC):
    def paySlip(self, amount):
        print('Your purchase amount: ${}'.format(amount))
    #this function is telling us to pass in an argument, but it doesn't tell you
    #how or what kind of data it will be
    @abstractmethod
    def payment(self, amount):
        pass

class debitCardPayment(car):
    def payment(self, amount):
        print('Your purchase amount of ${} exceeded your $100 limit'.format(amount))

if __name__ == '__main__':
    obj = debitCardPayment()
    obj.paySlip('400')
    obj.payment('400')