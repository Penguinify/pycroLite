# certified shitcode
import pynput
from time import sleep
from threading import Thread
from glob import glob
from random import randint

keyboard = pynput.keyboard.Controller()
mouse = pynput.mouse.Controller()

debug = True

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
    
    counter = 1
        
    run = True
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
            elif line[0] == 'counter':
                print(counter, line[1])
        counter += 1

def main():
    scripts = glob('scripts/*.pscript')
    print('.pycrolite has loaded!\n---Welcome User! Select your script from the ones listed below "/scripts/*.pscript"')
    for c,i in enumerate(scripts) : print(f'({c + 1})  —  ' + i)
    script = scripts[int(input('»>»')) - 1]

    with open(script) as reader:
        lines = reader.readlines()
    
    lines = [line.replace('\n', '') for line in lines]
    lines = [line.split(',') for line in lines]
    if debug == True : print(lines)
    interpretLines(lines)
        
    
    
if __name__ == '__main__':
    main()