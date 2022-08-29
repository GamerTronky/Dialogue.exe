import os
clear = lambda: os.system('cls')
al=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
allCombs,skipCombs=[],[]
for i in al:
    for m in al:
        if not m==i:allCombs.append(i+m)
        elif m==i:skipCombs.append(i+m)
    allCombs.append(i)
helpCommands=f'''For more information on a specific command, type HELP command-name
{'COLOR':<30}Changes console color to other color.
{'CLS':<30}Clears console, but leaves 1 blank line.
{'HELP':<30}Provides Help information for Dialogue commands.'''
helpHelp='''Provides help information for Dialogue commands.

HELP [command]

    command - displays help information on that command.'''
helpColor='''Sets the default console foreground and background colors.\n
COLOR [attr]\n
  attr        Specifies color attribute of console output\n
Color attributes are specified by TWO hex digits -- the first
corresponds to the background; the second the foreground. Each digit
can be any of the following values:

    0 = Black       8 = Gray
    1 = Blue        9 = Light Blue
    2 = Green       A = Light Green
    3 = Aqua        B = Light Aqua
    4 = Red         C = Light Red
    5 = Purple      D = Light Purple
    6 = Yellow      E = Light Yellow
    7 = White       F = Bright White
    
If no argument is given, this command restores the color to what it was
when Dialogue.EXE started. If one hex digit was given, first hex digit
corresponds to foreground.\n
the COLOR command with a foreground and background color that are the
same.\n
Example: "COLOR fc" produces light red on bright white'''
helpCls='''Clears the screen.

CLS'''
commands=['help','color','cls']
unnapropriate=[',',';',':']
foreground,background='7','0'
path=os.path.normpath(os.path.realpath(__file__))
full_path=path.split(os.sep)
userdir=[]
for i in range(3):
    userdir.append(full_path[i])
    userdir.append('\x5c')
userdir[-1]='>'
userdir=str(''.join(userdir))
print('Dialogue [Version 10.0.19044.1889]\n(c) by GamerTronky. All rights not reserved.\n')
while True:
    try:
        ocom=input(userdir)
        for un in unnapropriate:ocom=ocom.replace(un,' ')
        if ocom.split():
            com=ocom.lower()
            ocom,com=ocom.split(),com.split()
            if com[0] in commands:
                if com[0]=='help'and len(com)==1:print(helpCommands)
                elif com[0]=='help' and len(com)==2:
                    if com[1] in commands:
                        if com[1]=='help':print(helpHelp)
                        elif com[1]=='color':print(helpColor)
                        elif com[1]=='cls':print(helpCls)
                elif 'color'in com[0]:
                    if len(com)==1:os.system('color 07')
                    else:
                        if com[1] in allCombs:os.system(f'color {com[1]}')
                        elif com[1] in skipCombs:pass
                        else:print(helpColor)
                elif com[0]=='cls':clear()
            else:print(f"'{ocom[0]}' is not recognized as an internal or external command,\noperable program or batch file.")
            print()
    except:print('\n')