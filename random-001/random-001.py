# LEARNING PYTHON - RANDOMNESS
# Implementation of the simulation of a simple game
# of raquets.
# Matteo
# TO DO: CHECK LOGIC BEHIND SINGLE MATCH RESULT

from random import random

# FUNCTIONS

def printRules():
    print('''Simulating a game of raquets.
    The user needs to enter the probability of winning (0 - 0.99)
    of the two players and the number of matches to simulate.''')

def getData():
    """ Asking user for input: probability of the two players of winning
    the match and number of games to simulate.
    """
    player1 = float(input('Enter the probability to win of Player 1: '))
    player2 = float(input('Enter the probability to win of Player 2: '))
    games_to_simulate = int(input('Enter the number of games to simulate: '))
    return player1, player2, games_to_simulate

def simulate_match(pl1, pl2):
    """Simulating a single match of 30 sets each.
    If player one is leading (served the match), every time they score they get 
    one point, but if they were not leading the match they serving goes to 
    player two and vice versa.
    Not sure if the logic is accurate, to be confirmed.
    """
    score1 = score2 = 0
    leading = 1
    for i in range(30):
        if leading == 1:
            if (random() < pl1) & (random() > pl2):
                score1 += 1
            elif (random() < pl1) & (random() < pl2): #chaos 50%
                if random() < 0.5:
                    score1 += 1
            else:
                leading = 2
        else:
            if (random() < pl2) & (random() > pl1):
                score2 += 1
            elif (random() < pl2) & (random() < pl1): #chaos 50%
                if random() < 0.5:
                    score2 += 1 
            else: leading = 1
    if score1 > score2:
        return 1
    else:
        return 2

def simulate_game(pl1, pl2, games):
    """Simulating the full number of matches entered by the user, saved
    under the variable 'games'. The total scores are converted
    to a percentual in the form of a string and returned.
    """
    game1 = game2 = 0
    for i in range(games):
        game_result = simulate_match(pl1, pl2)
        if game_result == 1:
            game1 +=1
        else:
            game2 += 1
    stat1 = str(game1*100/games)
    stat2 = str(game2*100/games)
    print('Stat1 is {} and Stat2 is {}'.format(stat1, stat2))
    return stat1, stat2

def printOutcome(one, two):
    """Pretty-printing the outcome of the match using the data from
    the simulate_game dunction.
    """
    print(' Statistical Results: '.center(50, '~'))
    print('Player 1'.ljust(25) + 'Player2'.rjust(25))
    print('{}%{}%'.format(one.ljust(25), two.rjust(23)))
    

def startSimulation():
    """Game's starting function.
    Call this function to start the game.
    """
    win1 = win2 = 0
    printRules()
    pl1, pl2, games = getData()
    win1, win2 = simulate_game(pl1, pl2, games)
    printOutcome(win1, win2)

# starting MAIN
if __name__ == '__main__':
    startSimulation()