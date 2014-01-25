import ImageGrab
import ImageOps
from numpy import *
import os
import time
import mouse_util

def screenGrab():
    box = (mouse_util.x_pad + 1, mouse_util.y_pad + 1, mouse_util.x_pad+636, mouse_util.y_pad+475)
    im = ImageGrab.grab(box)
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im

def grab():
    box = (x_pad + 1,y_pad+1,x_pad+640,y_pad+480)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    return a


def get_slot1():
    box = (726, 477, 794, 501)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print 'Shell: ' + str(a)
    im.save(os.getcwd() + '\\slot_one__' + str(int(time.time())) + '.png', 'PNG')   
    return a

def get_slot2():
    box = (741, 431, 770, 441)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print 'Meat: ' + str(a)
    im.save(os.getcwd() + '\\slot_two__' + str(int(time.time())) + '.png', 'PNG')   
    return a

def get_slot3():
    box = (748, 397, 762, 402)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print 'T1: ' + str(a)
    im.save(os.getcwd() + '\\slot_three__' + str(int(time.time())) + '.png', 'PNG')   
    return a

def get_slot4():
    box = (747, 371, 762, 376)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print 'T2: ' + str(a)
    im.save(os.getcwd() + '\\slot_four__' + str(int(time.time())) + '.png', 'PNG')   
    return a

def get_order():
    get_slot1()
    get_slot2()
    get_slot3()
    get_slot4()

def main():
    get_order()

if __name__=='__main__':
    main()