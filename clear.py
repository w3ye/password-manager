from os import system, name

def clear():

    # OS = windows
    if name == 'nt':
        _ = system('cls')
    # mac or linux
    else: 
        _system('clear')