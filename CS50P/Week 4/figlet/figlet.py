import pyfiglet
import sys
import random

figlet = pyfiglet.Figlet()

fonts = figlet.getFonts()

if len(sys.argv) == 3:
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        if sys.argv[2] in fonts:
            figlet.setFont(font=sys.argv[2])
        else:
            sys.exit('Invalid usage')
    else:
        sys.exit('Invalid usage')
elif len(sys.argv) == 1:
    figlet.setFont(font=random.choice(fonts))
    pass
else:
    sys.exit('Invalid usage')

text = input('Input: ')

print(f'Output: \n {figlet.renderText(text)}')
