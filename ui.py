import readline


def get_data():
    val = input('Enter data - ')
    if ',' in val:
        v = val.split(',')
    elif ';' in val:
        v = val.split(';')
    elif ' ' in val:
        v = val.split(' ')         
    return v
