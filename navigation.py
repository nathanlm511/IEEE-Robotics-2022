from cv2 import stereoCalibrate
import steppermotortest
import serial

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.reset_input_buffer()

# def centreOnTrack():
#     pass


def forwardTree1():
    ser.write("2F")
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
    ser.write("3F")
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
    pass


def forwardTo5():
    pass


def forwardTo6():
    ser.write("6F")
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
    ser.write("8F")
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
    ser.write("9F")
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
    pass

def reverseTo3():
    pass

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