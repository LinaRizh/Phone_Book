from ui import *
from model import *
from log import *

print('Change format for export \n 1: \n surname name phone comment \n or 2: \n surname \n name \n phone \n comment \n')
view = int(input())
print('You want to import data from file or keybord iport? Enter file or keybord.')
metod = input()
if metod == 'file':
    imp_tel(format(),view)
else: 
    init(get_data())
    log_tel(view)

