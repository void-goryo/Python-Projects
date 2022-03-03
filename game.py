#
#   Python:     3.10.2
#
#   Author:     Gabriel Jones
#
#   Purpose:    The Tech Academy - Python Course, Creating our first program together.
#               Demonstraiting how to pass variables from a function to another function
#               while producing a functional game
#
#               Remember: function_name(variable) means that we pass in the variable.
#               Return variable means that we are returning the variable back to the calling function
#
#

import time

def start(nice = 0, mean = 0, name = ''):
    #get user's name
    name = describeGame(name)
    nice, mean, name = niceMean(nice, mean, name)

def describeGame(name):
    '''
        check if this is a new game of not.
        If it is new, get the user's name.
        If is is not a new game,
        thank the user for playing again and continue with the game
    '''
    #meaning, if we do not already have this user's name,
    #then they are a new player and we need to get their name
    if name != '':
        print('\nThank you for playing again, {}'.format(name))
    else:
        stop = True
        while stop:
            if name == '':
                name = input('\nWhat is your name? \n>>>').capitalize()
                if name != '':
                    print('Welcome, {}!'.format(name))
                    print('\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean')
                    print('but at he end of the game your fate \nwill be sealed by your actions.')
                    stop = False
    return name

def niceMean(nice, mean, name):
    stop = True
    while stop:
        showScore(nice, mean, name)
        pick = input('\nA stranger approaches you for a \nconversation. Will you be nice\nor mean? (N/M) \n>>>').lower()
        if pick == 'n':
            print('\nThe stranger walks away smiling...')
            nice = (nice + 1)
            stop = False
        if pick == 'm':
            print('the stranger glares at you\nmenecingly and storms off')
            mean = (mean + 1)
            stop = False
    score(nice, mean, name) #pass the variables to score

def showScore(nice, mean, name):
    print('\n{}, your current total: \n({}, Nice) and ({}, Mean)'.format(name, nice, mean))


def score (nice, mean, name):
    #score function is being passed the value stared within the 3 variables
    if nice > 2:
        win(nice, mean, name)
    if mean > 2:
        lose(nice, mean, name)
    else:
        niceMean(nice, mean, name)

def win(nice, mean, name):
    print('\nNice job {}, you win! \nEveryone loves you and you\'ve \nmade lots of friends along the way!'.format(name))
    again(nice, mean, name)


def lose(nice, mean, name):
    print('\nAhhhhh too bad, game over! \n{}, you live as a outcast in a little shack by a river.'.format(name))
    again(nice, mean, name)





def again(nice, mean, name):
    stop = True
    while stop:
        choice = input('\nDo you want to play again? (Y/N)').lower()
        if choice == 'y':
            stop = False
            reset(nice, mean, name)
        if choice == 'n':
            print('now exiting the game...')
            time.sleep(1)
            stop = False
            quit()
        else:
            print('\nPlease type \'Y\' for Yes and \'N\' for No')


def reset(nice, mean, name):
    nice = 0
    mean = 0
    start(nice, mean, name)


    

if __name__ == '__main__':
    start()

