set1 = {'hello', 'hola', 'ni hao', 'konnichiwa'}
set2 = ('hello', 'hola', 'zi jian', 'ohiyo')
set1.add('Hi')
set1.remove('hello')
print(set1)
print(set2)
difference1 = set1.difference(set2)

print(difference1)

print(type(set1))
