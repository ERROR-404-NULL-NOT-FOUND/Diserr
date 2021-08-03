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
    #makes it so ther isnt a blinking cursor
    curses.curs_set(0)
    #initiating color pairs
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    #opening the asciiart image and displaying it
    tokenrequestimage=open('token-message-ascii-art', 'r')
    for j in range(20):
        stdscr.addstr(tokenrequestimage.readline().strip('\n'))
        stdscr.move(j+1,0)
    #creating the input field
    stdscr.addstr('\n\n     ')
    stdscr.addstr('                                                               ',curses.color_pair(1))
    stdscr.addstr('\n     ')
    stdscr.addstr('                                                               ',curses.color_pair(1))
    stdscr.addstr('\n     ')
    stdscr.addstr('                                                               ',curses.color_pair(1))
    stdscr.addstr(23, 7, "                                                           ", curses.color_pair(2))
    stdscr.move(23, 7)
    #making it so you can see what your typing
    curses.echo()
    #refreshing the screen
    stdscr.refresh()
    #what is outputted by the function
    return stdscr.getstr()
def main(stdscr):
    #returns a weird format, so i have to remove the beginnig and end
    token=str(get_token(stdscr))[2:]
    token=token[:len(token)-1]
    #making sure the window is the correct size
    win=curses.newwin(size.lines-4,int((size.columns/3)*2),0, int((int(size.columns)/5)))
    #starting up the bot
    client=commands.Bot(command_prefix="")
    @client.event
    async def on_ready():
        #rendering messages
        messageRenderer.renderMessages(win,channelOpenMessageFetch.fetchChannelMessages(await client.fetch_channel(729649553648910401),client))
    client.run(token,bot=False)
wrapper(main)