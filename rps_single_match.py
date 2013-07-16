#!/usr/local/bin/python3
# Name: August Brenner
# File name: rps_single_match.py
# Date: July 8th, 2013

import HTML_Modules
from RPS_Modules import rps_game_winner, rps_winner

print("Content-type: text/html\n")
HTML_Modules.HTML_START("Single Match")

game = [["Armando", "P"], ["Dave", "S"]]

print(game)
print('<pre>' + rps_winner(rps_game_winner(game)) + '</pre>')

HTML_Modules.HTML_End()
