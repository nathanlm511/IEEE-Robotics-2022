import string
from cv2 import stereoCalibrate
import steppermotortest
import serial
from time import sleep

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=3)
ser.reset_input_buffer()

# def centreOnTrack():
#     pass


def forwardTree1():
    reading= True
    # read until something is read
    while reading:
        ser.write(b'2F\n')
        ser.reset_input_buffer()
        line = ser.readline().decode('utf-8').rstrip()
        print(f'received from arduino: {line}')
        if line:
            break
    while line != "S":
        print("In while")
        print(line)
        if line == "F":
            steppermotortest.forwards()
        else:
            # code should not be here
            print(line)
            print("Error: robot not moving as expected")
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
    
    steppermotortest.stopMoving()
#forwardTree1()

def forwardTo3():
    reading= True
    # read until something is read
    while reading:
        ser.write(b'3F\n')
        ser.reset_input_buffer()
        line = ser.readline().decode('utf-8').rstrip()
        print(f'received from arduino: {line}')
        print(line)
        if line:
            break   
    while line != "S":
        if line == "F":
            steppermotortest.forwards()
        else:
            # code should not be here
            print("Error: robot not moving as expected")
        line = ser.readline().decode('utf-8').rstrip()
    
    steppermotortest.stopMoving()


def turn1():
    reading= True
    # read until something is read
    while reading:
        ser.write(b'4F\n')
        ser.reset_input_buffer()
        line = ser.readline().decode('utf-8').rstrip()
        print(f'received from arduino: {line}')
        print(line)
        if line:
            break
    while line != "S":
        if line == "F":
            steppermotortest.forwards()
        elif line == "B":
            steppermotortest.backwards()
        elif line == "C":
            steppermotortest.clockwise()
        line = ser.readline().decode('utf-8').rstrip()
    
    steppermotortest.stopMoving()


def forwardTo5():
    reading= True
    # read until something is read
    while reading:
        ser.write(b'5F\n')
        ser.reset_input_buffer()
        line = ser.readline().decode('utf-8').rstrip()
        print(f'received from arduino: {line}')
        print(line)
        if line:
            break   
    while line != "S":
        if line == "B":
            steppermotortest.backwards()
        else:
            # code should not be here
            print("Error: robot not moving as expected")
        line = ser.readline().decode('utf-8').rstrip()
    
    steppermotortest.stopMoving()


def forwardTo6():
    reading= True
    # read until something is read
    while reading:
        ser.write(b'6F\n')
        ser.reset_input_buffer()
        line = ser.readline().decode('utf-8').rstrip()
        print(f'received from arduino: {line}')
        print(line)
        if line:
            break
    while line != "S":
        if line == "F":
            steppermotortest.forwards()
        else:
            # code should not be here
            print("Error: robot not moving as expected")
        line = ser.readline().decode('utf-8').rstrip()
    
    steppermotortest.stopMoving()

def forwardTree2():
    reading= True
    # read until something is read
    while reading:
        ser.write(b'8F\n')
        ser.reset_input_buffer()
        line = ser.readline().decode('utf-8').rstrip()
        print(f'received from arduino: {line}')
        print(line)
        if line:
            break
    while line != "S":
        if line == "F":
            steppermotortest.forwards()
        else:
            # code should not be here
            print("Error: robot not moving as expected")
        line = ser.readline().decode('utf-8').rstrip()
    
    steppermotortest.stopMoving()

def forwardTo9():
    reading= True
    # read until something is read
    while reading:
        ser.write(b'9F\n')
        ser.reset_input_buffer()
        line = ser.readline().decode('utf-8').rstrip()
        print(f'received from arduino: {line}')
        print(line)
        if line:
            break
    while line != "S":
        if line == "F":
            steppermotortest.forwards()
        else:
            # code should not be here
            print("Error: robot not moving as expected")
        line = ser.readline().decode('utf-8').rstrip()
    
    steppermotortest.stopMoving()

def reverseTree2():
    reading= True
    # read until something is read
    while reading:
        ser.write(b'8B\n')
        ser.reset_input_buffer()
        line = ser.readline().decode('utf-8').rstrip()
        print(f'received from arduino: {line}')
        print(line)
        if line:
            break
    while line != "S":
        if line == "B":
            steppermotortest.backwards()
        else:
            # code should not be here
            print("Error: robot not moving as expected")
        line = ser.readline().decode('utf-8').rstrip()
    
    steppermotortest.stopMoving()

def reverseTo7():
    reading= True
    # read until something is read
    while reading:
        ser.write(b'7B\n')
        ser.reset_input_buffer()
        line = ser.readline().decode('utf-8').rstrip()
        print(f'received from arduino: {line}')
        print(line)
        if line:
            break
    while line != "S":
        if line == "B":
            steppermotortest.backwards()
        else:
            # code should not be here
            print("Error: robot not moving as expected")
        line = ser.readline().decode('utf-8').rstrip()
    
    steppermotortest.stopMoving()

def reverseTo5():
    reading= True
    # read until something is read
    while reading:
        ser.write(b'5B\n')
        ser.reset_input_buffer()
        line = ser.readline().decode('utf-8').rstrip()
        print(f'received from arduino: {line}')
        print(line)
        if line:
            break
    while line != "S":
        if line == "B":
            steppermotortest.backwards()
        else:
            # code should not be here
            print("Error: robot not moving as expected")
        line = ser.readline().decode('utf-8').rstrip()
    
    steppermotortest.stopMoving()

def turn2():
    reading= True
    # read until something is read
    while reading:
        ser.write(b'4B\n')
        ser.reset_input_buffer()
        line = ser.readline().decode('utf-8').rstrip()
        print(f'received from arduino: {line}')
        print(line)
        if line:
            break
    while line != "S":
        if line == "F":
            steppermotortest.forwards()
        elif line == "CC":
            steppermotortest.counterClockwise()
        line = ser.readline().decode('utf-8').rstrip()
    
    steppermotortest.stopMoving()

def reverseTo3():
    reading= True
    # read until something is read
    while reading:
        ser.write(b'3B\n')
        ser.reset_input_buffer()
        line = ser.readline().decode('utf-8').rstrip()
        print(f'received from arduino: {line}')
        print(line)
        if line:
            break
    while line != "S":
        if line == "B":
            steppermotortest.backwards()
        else:
            # code should not be here
            print("Error: robot not moving as expected")
        line = ser.readline().decode('utf-8').rstrip()
    
    steppermotortest.stopMoving()

def reverseTree1():
    reading= True
    # read until something is read
    while reading:
        ser.write(b'2B\n')
        ser.reset_input_buffer()
        line = ser.readline().decode('utf-8').rstrip()
        print(f'received from arduino: {line}')
        print(line)
        if line:
            break
    while line != "S":
        if line == "B":
            steppermotortest.backwards()
        else:
            # code should not be here
            print("Error: robot not moving as expected")
        line = ser.readline().decode('utf-8').rstrip()
    
    steppermotortest.stopMoving()

def reverseTo1():
    reading= True
    # read until something is read
    while reading:
        ser.write(b'1B\n')
        ser.reset_input_buffer()
        line = ser.readline().decode('utf-8').rstrip()
        print(f'received from arduino: {line}')
        print(line)
        if line:
            break
    while line != "S":
        if line == "B":
            steppermotortest.backwards()
        else:
            # code should not be here
            print("Error: robot not moving as expected")
        line = ser.readline().decode('utf-8').rstrip()
    
    steppermotortest.stopMoving()

def navigate(robot):
    reading= True
    # read until something is read
    stringToSend = ''
    if robot.next_location == 1:
        stringToSend += '1'
    elif robot.next_location == 2:
        stringToSend += '2'
    elif robot.next_location == 3:
        stringToSend += '3'
    elif robot.next_location == 4:
        stringToSend += '4'
    elif robot.next_location == 5:
        stringToSend += '5'
    elif robot.next_location == 6:
        stringToSend += '6'
    elif robot.next_location == 7:
        stringToSend += '7'
    elif robot.next_location == 8:
        stringToSend += '8'
    elif robot.next_location == 9:
        stringToSend += '9'

    if robot.forward:
        stringToSend += 'F'
    else:
        stringToSend += 'B'

    stringToSend += '\n'
    
    
    
    while reading:
        ser.write(stringToSend.encode('utf-8'))
        # ser.reset_input_buffer()
        line = ser.readline().decode('utf-8').rstrip()
        # print(f'received from arduino: {line}')
        # print(line)
        if line:
            break

    while line != "S":
        if line == "F":
            steppermotortest.forwards()
        elif line == "B":
            steppermotortest.backwards()
        elif line == "C":
            steppermotortest.clockwise()
        elif line == "CC":
            steppermotortest.counterClockwise()

        line = ser.readline().decode('utf-8').rstrip()
    
    steppermotortest.stopMoving()
