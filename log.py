from datetime import datetime as dt
from queue import Empty
import model

def log_tel(exp_format):
    with open('log_tel.csv', 'a') as logf:
        if exp_format == 1:     
            logf.write(f'{(model.surname)} {(model.name)} {(model.phone)} {(model.comment)}')
        else: logf.write(f'{(model.surname)}\n {(model.name)}\n {(model.phone)}\n {(model.comment)}\n')


def format():
    a = open("imp_tel.csv", "r")
    temp = a.readline()
    if ';' in temp:
        l = temp.split(';')
    elif ',' in temp:
        l = temp.split(',')
    else: 
        l = temp.split(' ')
    return len(l)


def imp_tel(imp_format, exp_format):
    if imp_format > 1:
        a = open("imp_tel.csv", "r")

        for line in a:
            if ';' in line:
                model.init(line.split(';'))
                log_tel(exp_format) 
            elif ',' in line:
                model.init(line.split(','))
                log_tel(exp_format) 
            else:
                model.init(line.split(' '))
                log_tel(exp_format) 

    else: 
        a = open("imp_tel.csv", "r")
        l_str = []
        for line in a:
            if len(line) != 1:
                l_str.append(line.strip())
                if len(l_str) == 4:
                    model.init(l_str)
                    log_tel(exp_format)
                    l_str = []


