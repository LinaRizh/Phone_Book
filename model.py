from ui import *

surname = 'Ben'
name = 'Big'
phone = '89564324563'
comment  = ""

def init(list_date):
    global surname, name, phone, comment
    surname = list_date[0]
    name = list_date[1]
    phone = list_date[2]
    comment = list_date[3]
# init(get_data())