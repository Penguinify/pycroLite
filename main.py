# certified shitcode
import pynput
from time import sleep
from threading import Thread
from os import listdir
from random import randint
keyboard = pynput.keyboard.Controller()
mouse = pynput.mouse.Controller()
class parameters:
    version = 'v1.0.1'
debug = False
class keywords:
    pressable = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0',',','.','/','[',']','shift','space','ctrl','`','=','-']
    clickable = ['lb','rb','mb']
def press(line):
    if len(line) > 1:
        if line == 'space':
            keyboard.press(pynput.keyboard.Key.space)
        elif line == 'lshift':
            keyboard.press(pynput.keyboard.Key.shift_l)
        elif line == 'ctrl':
            keyboard.press(pynput.keyboard.Key.ctrl_l)
        elif line == 'left':
            mouse.press(pynput.mouse.Button.left)
        elif line == 'middle':
            mouse.press(pynput.mouse.Button.middle)
        elif line == 'right':
            mouse.press(pynput.mouse.Button.right)
        else:
            print('unfatal error: Unrecognized Key')
    else:
        keyboard.press(line)
    print('pressed ', line)
def release(line):
    if len(line) > 1:
        if line == 'space':
            keyboard.release(pynput.keyboard.Key.space)
        elif line == 'lshift':
            keyboard.release(pynput.keyboard.Key.shift_l)
        elif line == 'ctrl':
            keyboard.release(pynput.keyboard.Key.ctrl_l)
        elif line == 'left':
            mouse.release(pynput.mouse.Button.left)
        elif line == 'middle':
            mouse.release(pynput.mouse.Button.middle)
        elif line == 'right':
            mouse.release(pynput.mouse.Button.right)
        else:
            print('unfatal error: Unrecognized Key')
    else:
        keyboard.release(line)
    print('released ', line)
def interpretLines(lines):
    print('Running!')
    lines = lines[lines.index(['MACRO']) + 1:]
    counter = 1
    if debug == True : print(lines)
    run = True
    sleep(1)
    while run:
        for line in lines:
            if line[0] == 'press':
                press(line[1])
            elif line[0] == 'release':
                release(line[1])
            elif line[0] == 'delay':
                sleep(float(line[1]))
                print('delayed', line[1], 'seconds')
            elif line[0] == 'print':
                print(line[1])
            elif line[0] == 'mousemove':
                mouse.move(int(line[1]),int(line[2]))
                print('moved the mouse (x:', line[1], 'y:', line[2], ')')
            elif line[0] == 'mouseset':
                mouse.position = (int(line[1]),int(line[2]))
                print('set the mouse position to (x:', line[1], 'y:', line[2], ')')
            elif line[0] == 'counter':
                print(counter, line[1])
            
        counter += 1
def main():
    scripts = listdir('scripts/')
    print('.pycrolite has loaded!\n---Welcome User! Select your script from the ones listed below "/scripts/*.pscript"')
    for c,i in enumerate(scripts) : print(f'({c + 1})  —  ' + i)
    script = scripts[int(input('»>»')) - 1]
    with open('scripts/' + script) as reader:
        lines = reader.readlines()
    if debug == True : print(lines)
    lines = [line.replace('\n', '') for line in lines]
    lines = [line.split(',') for line in lines]
    if debug == True : print(lines)
    if float(lines[0][1]) < 1.0:
        print('\n\n\n\n\n\nfatal error: outdated script version. Continuing the program may result in a crash.\nWould you like to continue?')
        if input('⚠ Y/N ⚠\n') == 'Y':
            pass
        else:
            main()
    interpretLines(lines)
if __name__ == '__main__':
    main()