dicUsers = {'em1234':{'fname': 'Bob', 'lname': 'Smith', 'phone': '123-456-7890'},
            'em1235': {'fname':'Mary','lname':'Jones','phone':'152-364-5764'}}
#creates dictionary

print('User: {} {} \nPhone: {}'.format(dicUsers['em1235']['fname'],
                                       dicUsers['em1234']['lname'],
                                       dicUsers['em1235']['phone']))
