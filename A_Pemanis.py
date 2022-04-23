import time
import os

def loading():
    animation = [
    "--------- LOADING [        ] ---------",
    "--------- LOADING [=       ] ---------",
    "--------- LOADING [===     ] ---------",
    "--------- LOADING [====    ] ---------",
    "--------- LOADING [=====   ] ---------",
    "--------- LOADING [======  ] ---------",
    "--------- LOADING [======= ] ---------",
    "--------- LOADING [========] ---------",
    "--------- LOADING [ =======] ---------",
    "--------- LOADING [  ======] ---------",
    "--------- LOADING [   =====] ---------",
    "--------- LOADING [    ====] ---------",
    "--------- LOADING [     ===] ---------",
    "--------- LOADING [      ==] ---------",
    "--------- LOADING [       =] ---------",
    "--------- LOADING [        ] ---------",
    "--------- LOADING [        ] ---------" ]
    notcomplete = True
    i = 0
    while notcomplete:
        print(animation[i % len(animation)], end='\r')
        time.sleep(.1)
        i += 1
        if i == 30:
            break


folder = 'Z_BMOframes'
def animatedbmo(repeat = 2):
    global folder
    filenames = []
    for i in range(14):
        filenames.append(f"Z_BMOframes/{i}.txt")

    frames = []
    for name in filenames:
        with open(name, "r", encoding="utf8") as f:
            frames.append(f.readlines())

    for i in range(repeat):
        for frame in frames:
            print("".join(frame))
            time.sleep(0.1)

    print('''
======================================================================================

▒█▀▀▀█ ▒█▀▀▀ ▒█░░░ ░█▀▀█ ▒█▀▄▀█ ░█▀▀█ ▀▀█▀▀ 　 ▒█▀▀▄ ░█▀▀█ ▀▀█▀▀ ░█▀▀█ ▒█▄░▒█ ▒█▀▀█ 
░▀▀▀▄▄ ▒█▀▀▀ ▒█░░░ ▒█▄▄█ ▒█▒█▒█ ▒█▄▄█ ░▒█░░ 　 ▒█░▒█ ▒█▄▄█ ░▒█░░ ▒█▄▄█ ▒█▒█▒█ ▒█░▄▄ 
▒█▄▄▄█ ▒█▄▄▄ ▒█▄▄█ ▒█░▒█ ▒█░░▒█ ▒█░▒█ ░▒█░░ 　 ▒█▄▄▀ ▒█░▒█ ░▒█░░ ▒█░▒█ ▒█░░▀█ ▒█▄▄█

======================================================================================

    ''')