from cv2 import stereoCalibrate
import steppermotortest
import serial

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.reset_input_buffer()

# def centreOnTrack():
#     pass


def forwardTree1():
    ser.write(b"2F\n")
    ser.reset_input_buffer()
    line = ser.readline().decode('utf-8').rstrip()
   
    while line != "S":
        if line == "F":
            steppermotortest.forwards()
        else:
            # code should not be here
            print("Error: robot not moving as expected")
        ser.reset_input_buffer()
        line = ser.readline().decode('utf-8').rstrip()
    
    steppermotortest.stopMoving()

def forwardTo3():
    ser.write(b"3F\n")
    ser.reset_input_buffer()
    line = ser.readline().decode('utf-8').rstrip()
   
    while line != "S":
        if line == "F":
            steppermotortest.forwards()
        else:
            # code should not be here
            print("Error: robot not moving as expected")
        ser.reset_input_buffer()
        line = ser.readline().decode('utf-8').rstrip()
    
    steppermotortest.stopMoving()


def turn1():
    ser.write(b"4F\n")
    ser.reset_input_buffer()
    line = ser.readline().decode('utf-8').rstrip()
   
    while line != "S":
        if line == "F":
            steppermotortest.forwards()
        elif line == "C":
            steppermotortest.clockwise()
        ser.reset_input_buffer()
        line = ser.readline().decode('utf-8').rstrip()
    
    steppermotortest.stopMoving()


def forwardTo5():
    ser.write(b"5F\n")
    ser.reset_input_buffer()
    line = ser.readline().decode('utf-8').rstrip()
   
    while line != "S":
        if line == "B":
            steppermotortest.backwards()
        else:
            # code should not be here
            print("Error: robot not moving as expected")
        ser.reset_input_buffer()
        line = ser.readline().decode('utf-8').rstrip()
    
    steppermotortest.stopMoving()


def forwardTo6():
    ser.write(b"6F\n")
    ser.reset_input_buffer()
    line = ser.readline().decode('utf-8').rstrip()
   
    while line != "S":
        if line == "F":
            steppermotortest.forwards()
        else:
            # code should not be here
            print("Error: robot not moving as expected")
        ser.reset_input_buffer()
        line = ser.readline().decode('utf-8').rstrip()
    
    steppermotortest.stopMoving()

def forwardTree2():
    ser.write(b"8F\n")
    ser.reset_input_buffer()
    line = ser.readline().decode('utf-8').rstrip()
   
    while line != "S":
        if line == "F":
            steppermotortest.forwards()
        else:
            # code should not be here
            print("Error: robot not moving as expected")
        ser.reset_input_buffer()
        line = ser.readline().decode('utf-8').rstrip()
    
    steppermotortest.stopMoving()

def forwardTo9():
    ser.write(b"9F\n")
    ser.reset_input_buffer()
    line = ser.readline().decode('utf-8').rstrip()
   
    while line != "S":
        if line == "F":
            steppermotortest.forwards()
        else:
            # code should not be here
            print("Error: robot not moving as expected")
        ser.reset_input_buffer()
        line = ser.readline().decode('utf-8').rstrip()
    
    steppermotortest.stopMoving()

def reverseTree2():
    ser.write("8B")
    ser.reset_input_buffer()
    line = ser.readline().decode('utf-8').rstrip()
   
    while line != "S":
        if line == "B":
            steppermotortest.backwards()
        else:
            # code should not be here
            print("Error: robot not moving as expected")
        ser.reset_input_buffer()
        line = ser.readline().decode('utf-8').rstrip()
    
    steppermotortest.stopMoving()

def reverseTo7():
    ser.write("7B")
    ser.reset_input_buffer()
    line = ser.readline().decode('utf-8').rstrip()
   
    while line != "S":
        if line == "B":
            steppermotortest.backwards()
        else:
            # code should not be here
            print("Error: robot not moving as expected")
        ser.reset_input_buffer()
        line = ser.readline().decode('utf-8').rstrip()
    
    steppermotortest.stopMoving()

def reverseTo5():
    ser.write("5B")
    ser.reset_input_buffer()
    line = ser.readline().decode('utf-8').rstrip()
   
    while line != "S":
        if line == "B":
            steppermotortest.backwards()
        else:
            # code should not be here
            print("Error: robot not moving as expected")
        ser.reset_input_buffer()
        line = ser.readline().decode('utf-8').rstrip()
    
    steppermotortest.stopMoving()

def turn2():
    ser.write("4B")
    ser.reset_input_buffer()
    line = ser.readline().decode('utf-8').rstrip()
   
    while line != "S":
        if line == "F":
            steppermotortest.forwards()
        elif line == "CC":
            steppermotortest.counterClockwise()
        ser.reset_input_buffer()
        line = ser.readline().decode('utf-8').rstrip()
    
    steppermotortest.stopMoving()

def reverseTo3():
    ser.write("3B")
    ser.reset_input_buffer()
    line = ser.readline().decode('utf-8').rstrip()
   
    while line != "S":
        if line == "B":
            steppermotortest.backwards()
        else:
            # code should not be here
            print("Error: robot not moving as expected")
        ser.reset_input_buffer()
        line = ser.readline().decode('utf-8').rstrip()
    
    steppermotortest.stopMoving()

def reverseTree1():
    ser.write("2B")
    ser.reset_input_buffer()
    line = ser.readline().decode('utf-8').rstrip()
   
    while line != "S":
        if line == "B":
            steppermotortest.backwards()
        else:
            # code should not be here
            print("Error: robot not moving as expected")
        ser.reset_input_buffer()
        line = ser.readline().decode('utf-8').rstrip()
    
    steppermotortest.stopMoving()

def reverseTo1():
    ser.write("1B")
    ser.reset_input_buffer()
    line = ser.readline().decode('utf-8').rstrip()
   
    while line != "S":
        if line == "B":
            steppermotortest.backwards()
        else:
            # code should not be here
            print("Error: robot not moving as expected")
        ser.reset_input_buffer()
        line = ser.readline().decode('utf-8').rstrip()
    
    steppermotortest.stopMoving()