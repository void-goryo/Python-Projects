i = 0

while i >= 0:
    if i == 10:
        break
    print(i)
    i += 1

fruit = ['apple', 'bannana', 'pear', 'orange']
i = 0

for i in fruit:
    if i == 'bannana':
        continue
    else:
        print(i)
for i in enumerate(fruit(1)):
    print(i)
