customer = {'cust0001':{'fname':'Gabriel', 'lname':'Jones'},
            'cust0002':{'fname':'Tyler', 'lname':'Jones'},
            'cust0003':{'fname':'Kaylee', 'lname':'Mett'}}

print(customer)

print(customer.get('cust0001'))

customer.update({'cust0001':{'fname':'Gabe', 'lname':'Jones'}})

print(customer.get('cust0001'))

x = {'room1', 'room2'}
y = 0

x.update({'room3'})

peopleInRoom = dict.fromkeys(x,y)
print(peopleInRoom)
