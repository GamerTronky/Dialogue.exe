import os,random,time,sys
os.system('title Dialogue Prompt')
if os.path.isfile('start_settings.txt'):
    with open('start_settings.txt','r')as s:os.system(f'title {s.read()}')
    os.remove('start_settings.txt')
al=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
allCombs,skipCombs=[i+m for i in al for m in al if not m==i],[i+m for i in al for m in al if m==i]
credit='''Dialogue.exe developed GamerTronky.\nInspired by CMD.exe\n\n(c) All rights not reserved.\n\nGo look at other projects: https://gamertronky.itch.io/'''
helpCommands=f'''For more information on a specific command, type HELP command-name
{'BINCONVERT':<30}Prints binary value of given string.
{'CLS':<30}Clears console, but leaves 1 blank line.
{'COLOR':<30}Changes console color to other color.
{'CREDITS':<30}Just some information.
{'HELP':<30}Provides Help information for Dialogue commands.
{'START':<30}Starts a separate window to run a specified program or command.
{'TITLE':<30}Sets the window title for a Dialogue.exe session.
{'TIME':<30}Displays current time.
{'RCHANGE':<30}Randomly changes given argument.'''
helpHelp='''Provides help information for Dialogue commands.\n\nHELP [command]\n\n    command - displays help information on that command.'''
helpColor='''Sets the default console foreground and background colors.\n
COLOR [attr]\n\n    attr        Specifies color attribute of console output\n\nColor attributes are specified by TWO hex digits -- the first
corresponds to the background; the second the foreground. Each digit\ncan be any of the following values:\n
    0 = Black       8 = Gray\n    1 = Blue        9 = Light Blue\n    2 = Green       A = Light Green
    3 = Cyan        B = Light Cyan\n    4 = Red         C = Light Red\n    5 = Purple      D = Light Purple
    6 = Yellow      E = Light Yellow\n    7 = White       F = Bright White\n   
If no argument is given, this command restores the color to what it was\nwhen Dialogue.EXE started. If one hex digit was given, first hex digit
corresponds to foreground.\nBackground and Foreground can't be the same.\nExample: "COLOR fc" produces light red on bright white.'''
helpCls='''Clears the screen.\n\nCLS'''
helpTitle='''Sets the window title for the Dialogue window.\n\nTITLE [string]\n\n    string       Specifies the title for the Dialogue window.'''
helpConvertBin='''Prints binary value of given string.\n\nBINCONVERT [string]\n\n    string       Any character.'''
helpWordMess='''Randomly changes given argument.\n\nRCHANGE [string]\n\n    string       Any character.'''
helpCredits='''Just some information.\n\nCREDITS'''
helpStart='''Starts a separate window to run a specified command.\n\nSTART [title]\n\n    title        Title for new window.(optional)'''
helpTime='''Displays current time.\n\nTIME'''
commands=['help','color','cls','title','binconvert','credits','start','rchange','time']
userdir='\x5c'.join(os.path.normpath(os.path.realpath(__file__)).split(os.sep)[:3])+'>'
print('Dialogue [Version 10.0.19044.1889]\n(c) by GamerTronky. All rights not reserved.\n')
while True:
    #try:
    ocom=input(userdir)
    if ((ocom.replace(':','')).replace(';','')).replace(',','').split():
        com=ocom.lower().split()
        if com[0] in commands:
            if com[0]=='help'and len(com)==1:print(helpCommands)
            elif com[0]=='help' and len(com)==2:
                if com[1]=='help':print(helpHelp)
                elif com[1]=='color':print(helpColor)
                elif com[1]=='cls':print(helpCls)
                elif com[1]=='title':print(helpTitle)
                elif com[1]=='binconvert':print(helpConvertBin)
                elif com[1]=='credits':print(helpCredits)
                elif com[1]=='start':print(helpStart)
                elif com[1]=='rchange':print(helpWordMess)
                elif com[1]=='time':print(helpTime)
                else:
                    try:print(f'This command is not supported by the help utility. Did you mean "{[c for c in commands if com[1] in c][0]}"?')
                    except:print('This command is not supported by the help utility.')
            elif 'color'in com[0]:
                if len(com)==1:os.system('color 07')
                else:
                    if com[1] in allCombs:os.system(f'color {com[1]}')
                    elif com[1] in skipCombs:pass
                    else:print(helpColor)
            elif com[0]=='cls':os.system('cls')
            elif com[0]=='title':os.system(ocom)
            elif com[0]=='binconvert':
                try:print(''.join(format(ord(x), 'b') for x in ocom.split(maxsplit=1)[1]))
                except:print(helpConvertBin)
            elif com[0]=='credits':print(credit)
            elif com[0]=='start':
                if len(com)>1:
                    with open('start_settings.txt', 'w') as f:f.write(ocom.split(maxsplit=1)[1])
                os.startfile(sys.argv[0])
            elif com[0]=='rchange':print(' '.join([''.join([random.choice(i.replace('.','')) if not i[len(i)-1]==s else random.choice(i) for s in i]) for i in ocom.split(maxsplit=1)[1].split()]))
            elif com[0]=='time':print(time.strftime('Current time: %m/%d/%Y, %H:%M:%S'))
        else:print(f"'{ocom.split()[0]}' is not recognized as an internal or external command,\nuse help if you need help.")
        print()
    #except:print('\n')