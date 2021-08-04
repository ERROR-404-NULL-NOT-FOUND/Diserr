#!/usr/bin/env python3
#imports
import discord
import curses
import os
import messageRenderer
import channelOpenMessageFetch
import asyncio
client = discord.Client()

#read token from token.txt
#depending on how this script is used we might want an installation directory to acess Diserr globally.
def getToken():
    global token
    try:
        open("token.txt", "x")
        f = open("token.txt", "w")
        f.write(input("enter token: "))
        f = open("token.txt", "r")
        token = f.read()
    except:
        f = open("token.txt", "r")
        token = f.read()
getToken()
if token.startswith("mfa."):
    print("Thats not a Bot Token! \n delete token.txt and get an bot token")
    exit()
#methods
async def refscreen():
    while True:
        stdscr.refresh()
        if dm_win:
            dm_win.refresh()
        if server_win:
            server_win.refresh()
        if main_win:
            main_win.refresh()
        if member_win:
            member_win.refresh()
        await asyncio.sleep(0.1)
def stop():
    task.cancel()

#window management
#get terminal size. has to be auto updated later
size=os.get_terminal_size()
#create screens and call auto update loop
stdscr = curses.initscr()
dm_win= curses.newwin(int((size[1] * 25)/100), int((size[0] * 25)/100), 1, 1)
server_win= curses.newwin(size[1] - int((size[1] * 25)/100) -3, int((size[0] * 25)/100), int((size[1] * 25)/100) +1, 1)
main_win = curses.newwin(size[1] -2, int((size[0] * 50)/100), 1,int((size[0] * 25)/100)+1)
member_win = curses.newwin(size[1] -2, int((size[0] * 25)/100)-1,1,size[0]- int((size[0] * 25)/100))
loop = asyncio.get_event_loop()
#loop.call_later(5, stop)       #stop auto update after x seconds
task = loop.create_task(refscreen())

@client.event
async def on_ready():
    stdscr.addstr(size[1] -2, 1, 'We have logged in as {0.user}'.format(client))
    stdscr.refresh()
    stdscr.getch()  #exit after bot is ready, only needed on windows as ctrl + c doesnt work
    exit()

def main(stdscr):
    #window frames
    curses.curs_set(0)
    stdscr.border(0)
    dm_win.border(0)
    server_win.border(0)
    main_win.border(0)
    member_win.border(0)
    #
    client.run(token)
    stdscr.getch() #needed so the client doesnt stop after the bot started
curses.wrapper(main)
