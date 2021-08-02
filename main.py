import discord 
import curses
import os
from discord.ext import commands
from curses import wrapper
size=os.get_terminal_size()
token=""
def get_token(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    tokenrequestimage=open('token-message-ascii-art', 'r')
    for j in range(20):
        stdscr.addstr(tokenrequestimage.readline().strip('\n'))
        stdscr.move(j+1,0)
    stdscr.addstr('\n\n     ')
    stdscr.addstr('                                ',curses.color_pair(1))
    stdscr.addstr('\n     ')
    stdscr.addstr('                                ',curses.color_pair(1))
    stdscr.addstr('\n     ')
    stdscr.addstr('                                ',curses.color_pair(1))
    stdscr.addstr(23, 7, "                            ", curses.color_pair(2))
    stdscr.move(23, 7)
    curses.echo()
    stdscr.refresh()
    token=stdscr.getstr()

def main(stdscr):
    win=curses.newwin(int((int(size.lines)/3)*2),int((int(size.columns)/3)*2),int((int(size.lines)/3)*2), int((int(size.columns)/3)*2))
    client=commands.Bot(command_prefix="")

    client.run(token)
wrapper(main)