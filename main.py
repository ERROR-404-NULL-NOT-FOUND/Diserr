import discord
from discord.ext import commands
import curses
import os
import time

import messageRenderer
import channelOpenMessageFetch

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
    stdscr.addstr('                                                               ',curses.color_pair(1))
    stdscr.addstr('\n     ')
    stdscr.addstr('                                                               ',curses.color_pair(1))
    stdscr.addstr('\n     ')
    stdscr.addstr('                                                               ',curses.color_pair(1))
    stdscr.addstr(23, 7, "                                                           ", curses.color_pair(2))
    stdscr.move(23, 7)
    curses.echo()
    stdscr.refresh()
    return stdscr.getstr()
def main(stdscr):
    token=str(get_token(stdscr))[2:]
    token=token[:len(token)-1]
    win=curses.newwin(size.lines-4,int((size.columns/3)*2),0, int((int(size.columns)/5)))
    client=commands.Bot(command_prefix="")
    @client.event
    async def on_ready():
        messageRenderer.renderMessages(win,channelOpenMessageFetch.fetchChannelMessages(await client.fetch_channel(729649553648910401),client))
    client.run(token,bot=False)
wrapper(main)
