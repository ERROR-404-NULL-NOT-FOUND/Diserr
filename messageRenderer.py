import curses
def renderMessages(win,messages):
    #creatinf wondow border
    win.border("|","|","-","-",0,0,0,0)
    j=0
    #
    print(messages)
    win.refresh()