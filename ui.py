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

# a = open("imp_tel.csv", "r")
# for line in a:
#     m = line
#     print(len(m))
# a = open("imp_tel.csv", "r")
# l = (a.readline()).split(' ')
# if len(l) > 1:
#     # print(l[2])

# a = open("imp_tel.csv", "r")
# temp = a.readline().split(' ')
# print(temp)
# print(len(temp))
# print(temp[0])