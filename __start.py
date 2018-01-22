#!/usr/bin/python3
import configparser
from game_controller import GameController

# Global Game Parameters
_SECTOR_SIDE = 1000


param = 'param'
one_pam = 'pam'
pam = 'WTF 0_o'


game = GameController()


while not game.to_exit:
    game.act()






