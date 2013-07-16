#!/usr/local/bin/python3
# Name: August Brenner
# File name: rps_tournament.py
# Date: July 8th, 2013

import HTML_Modules
from RPS_Modules import rps_tournament_winner, rps_winner, WrongNumberOfPlayersError, NoSuchStrategyError

print("Content-type: text/html\n")
HTML_Modules.HTML_START("Tournament")

four_games_two_divisions = [
[[["Armando", "P"], ["Dave", "S"] ], [ ["Richard", "R"], ["Michael", "S"]]],
[[["Allen", "S" ], ["Omer", "P"] ], [ ["David E.", "R"], ["Richard X.", "P"]]]
]

eight_presidents_playing_rps = [
[['Franklin','P'],['Abe','S']], [['Barack','S'],['George','R']],
[['Grover','P'],['Woodrow','S']], [['John','R'],['John F.','P']],
[['Dick','P'],['Dwight','S']], [['Harry','R'],['Lyndon','S']],
[['Billy','S'],['Bubba','S']], [['Teddy','P'],['Herbert','S']]
]

thirty_two_games_four_divisions = [
[
[['p1','R'],['p2','S']], [['p3','R'],['p4','P']],
[['p5','R'],['p6','S']], [['p7','R'],['p8','R']],
[['p9','P'],['p10','S']], [['p11','R'],['p12','S']],
[['p13','S'],['p14','S']], [['p15','P'],['p16','S']]
],
[
[['p17','R'],['p18','S']], [['p19','R'],['p20','P']],
[['p21','R'],['p22','S']], [['p23','R'],['p24','R']],
[['p25','P'],['p26','S']], [['p27','R'],['p28','S']],
[['p29','S'],['p30','S']], [['p31','P'],['p32','S']]
],
[
[['p33','R'],['p34','S']], [['p35','p'],['p36','S']],
[['p37','R'],['p38','S']], [['p39','R'],['p40','R']],
[['p41','P'],['p42','S']], [['p43','R'],['p44','S']],
[['p45','S'],['p46','S']], [['p47','P'],['p48','S']]
],
[
[['p49','R'],['p50','S']], [['p51','R'],['p52','P']],
[['p53','R'],['p54','S']], [['p55','R'],['p56','R']],
[['p57','P'],['p58','S']], [['p59','R'],['p60','S']],
[['p61','S'],['p62','S']], [['p63','P'],['p64','S']]
]
]

eight_presidents_think_the_pen_is_mighty = [
[['Franklin','P'],['Abe','P']], [['Barack','P'],['George','P']],
[['Grover','P'],['Woodrow','P']], [['John','P'],['John F.','P']],
[['Dick','P'],['Dwight','P']], [['Harry','P'],['Lyndon','P']],
[['Billy','P'],['Bubba','P']], [['Teddy','P'],['Herbert','P']]
]

no_such_strategy_error_example = [
[['Franklin','X'],['Abe','S']], [['Barack','S'],['George','R']],
[['Grover','P'],['Woodrow','S']], [['John','R'],['John F.','P']],
[['Dick','P'],['Dwight','S']], [['Harry','R'],['Lyndon','S']],
[['Billy','S'],['Bubba','S']], [['Teddy','P'],['Herbert','S']]
]

wrong_number_of_players_example = [
[['Abe','S']], [['Barack','S'],['George','R']],
[['Grover','P'],['Woodrow','S']], [['John','R'],['John F.','P']],
[['Dick','P'],['Dwight','S']], [['Harry','R'],['Lyndon','S']],
[['Billy','S'],['Bubba','S']], [['Teddy','P'],['Herbert','S']]
]

games = [four_games_two_divisions, eight_presidents_playing_rps, thirty_two_games_four_divisions,
         eight_presidents_think_the_pen_is_mighty, no_such_strategy_error_example,
         wrong_number_of_players_example]
titles = ['Four Games Two Divisions', 'Eight Presidents Playing RPS', 'Thirty Two Games Four Divisions',
          'Eight Presidents Think the Pen is Mighty', 'No Such Strategy Error Example',
          'Wrong Number of Players Example']


def HTML_ERROR(error):
    error_string = str(error)
    print('<span style="color:red"><strong>' + error_string + '</strong></span>')


for game, title in zip(games, titles):
    print('<h2>' + title +
          '</h2><p>Using this list of games</p><code>')
    print(game)
    print('</code> <br><br>')
    try:
        print(rps_winner(rps_tournament_winner(game)))
    except NoSuchStrategyError as e:
        HTML_ERROR(e)
    except WrongNumberOfPlayersError as e:
        HTML_ERROR(e)


HTML_Modules.HTML_End()
