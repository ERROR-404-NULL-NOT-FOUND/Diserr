import curses
def renderMessages(win,messages):
    win.border("|","|","-","-",0,0,0,0)
    j=0
    for i in messages:
        win.addstr(j,5,i.content.content)
        j+=1
    win.refresh()

