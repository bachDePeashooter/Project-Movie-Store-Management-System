import numpy as np
import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle

#homepage
def main2(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
    BLUE_AND_BLACK=curses.color_pair(1)
    RED_AND_BLACK=curses.color_pair(2)
    CYAN_AND_BLACK=curses.color_pair(3)
    stdscr.clear()
    stdscr.addstr(3,3,"Welcome to our movie store management system !",BLUE_AND_BLACK | curses.A_BOLD)
    stdscr.addstr(5,3,"Press any key for starting...",CYAN_AND_BLACK | curses.A_DIM )
    stdscr.attron(RED_AND_BLACK)
    rectangle(stdscr,1,1,7,50)
    stdscr.attroff(RED_AND_BLACK)
    stdscr.refresh()
    stdscr.getch()
    curses.endwin()
wrapper(main2)

from msms_Input import*
