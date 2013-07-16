#!/usr/local/bin/python3
# Name: August Brenner
# File name: RPS_Modules.py
# Date: July 8th, 2013

import random


class WrongNumberOfPlayersError(Exception):
    pass


class NoSuchStrategyError(Exception):
    pass

STRATEGY_NAMES = {
    'R': 'Rock',
    'P': 'Paper',
    'S': 'Scissors',
}


# error handlers
def error_handling(game):
    strategies = STRATEGY_NAMES.keys()
    if len(game) != 2:
        raise WrongNumberOfPlayersError('Wrong number of players!')
    for g in game:
        if g[1].upper() not in strategies:
            raise NoSuchStrategyError('No Such Strategy!')


# code to determine winner
# replays ties with pseudo random RPS selector for pseudo fairness
def rps_game_winner(game):
    error_handling(game)
    first_wins = ['RS', 'PR', 'SP']
    if (game[0][1] + game[1][1]) in first_wins:
        return game[0]
    elif game[0][1].upper() == game[1][1].upper():
        game[0][1] = random.choice(list(STRATEGY_NAMES.keys()))
        game[1][1] = random.choice(list(STRATEGY_NAMES.keys()))
        return rps_game_winner(game)
    else:
        return game[1]


# recursively plays through a nested list of players and runs rps_game_winner on each match.
def rps_tournament_winner(game):
    if isinstance(game[0][0], str):
        return rps_game_winner(game)
    else:
        return rps_game_winner([rps_tournament_winner(game[0]), rps_tournament_winner(game[1])])


# generates string output for matches
def rps_winner(winner):
    return 'player ' + winner[0] + ' wins with ' + STRATEGY_NAMES[winner[1]]



