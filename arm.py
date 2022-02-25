import time
from board import SCL, SDA
import busio

from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

i2c = busio.I2C(SCL, SDA)

pca = PCA9685(i2c)

pca.frequency = 50

# settings for MG955S servos (numbered from top to bottom of arm)
servos = []
servos.append(servo.Servo(pca.channels[0], min_pulse = 500, max_pulse = 2500))
servos.append(servo.Servo(pca.channels[1], min_pulse = 500, max_pulse = 2500))
servos.append(servo.Servo(pca.channels[2], min_pulse = 500, max_pulse = 2500))
servos.append(servo.Servo(pca.channels[3], min_pulse = 500, max_pulse = 2500))
servos.append(servo.Servo(pca.channels[4], min_pulse = 500, max_pulse = 2500))

# settings for MG955S servos
baseServo = servo.Servo(pca.channels[5], min_pulse = 500, max_pulse = 2500)
armServo = servo.Servo(pca.channels[6], min_pulse = 500, max_pulse = 2500)

# settings for SG90 servos
holdServo = servo.Servo(pca.channels[7], min_pulse = 500, max_pulse = 2500)

# position_now = [1,110,100,110,15]
# startPosition= [0,120,120,120,20]
# straightUp = [0,120,85,90,20]
# lineUpTree = [0,120,85,90,125]


def servoTest(servoNum, startAngle, stopAngle):
    servoNum = int(servoNum)
    start = int(startAngle)
    stop = int(stopAngle)
    diff = abs(start - stop)
    numSteps = round(diff/5)
    servos[servoNum].angle = start
    newAngle = start
    if start < stop:
        for i in range(numSteps):
            newAngle = start + (i * 5)
            servos[servoNum].angle = newAngle
            time.sleep(0.06)
            print(newAngle)
        if newAngle != stop:
            servos[servoNum].angle = stop
            print(stop)
    elif start > stop:
        for i in range(numSteps):
            newAngle = start - (i * 5)
            servos[servoNum].angle = newAngle
            time.sleep(0.06)
            print(newAngle)
        if newAngle != stop:
            servos[servoNum].angle = stop
            print(stop)
# def move_angle(servoNum, startAngle, stopAngle):
#     Angle_now = startAngle
#     i = 1
#     if startAngle>stopAngle:
#         i=-1
#     while Angle_now != stopAngle:
#         Angle_now = Angle_now + i
#         servos[servoNum].angle = Angle_now
#         time.sleep(0.1)
#     print (Angle_now)
#             
# def move(position_now, pos):
#     for i in range(5):
#         if position_now[4-i] != pos[4-i]:
#             move_angle(4-i,position_now[4-i],pos[4-i])
#             time.sleep(0.5)
#     position_now = pos

def startPosition():
    servoTest(4, 15, 20)
    time.sleep(1)
    servoTest(3, 110, 120)
    servoTest(2, 100, 80)
    servoTest(1, 110, 165)
    servoTest(0, 1, 0)
    servoTest(3, 120, 135)
    
def straightUp():
    servoTest(4, 20, 20)
    servoTest(3, 135, 80)
    servoTest(2, 80, 85)
    servoTest(1, 165, 105)
    servoTest(0, 0, 0)
    
def lookLeft():
    servoTest(4, 20, 125)
    servoTest(3, 80, 30)
    servoTest(2, 85, 135)
    servoTest(1, 90, 180)
    servoTest(0, 0, 0)    

def lineUpBracelets():
    servoTest(4, 125, 125)
    servoTest(2, 135, 90)
    servoTest(3, 30, 60)
    servoTest(1, 180, 180)
    servoTest(0, 0, 0)
    
def intoBracelets():
    servoTest(0, 0, 0)   
    servoTest(2, 90, 80)
    servoTest(3, 60, 65)
    time.sleep(0.5)
    servoTest(1, 180, 175)
    time.sleep(0.5)
    servoTest(3, 65, 75)
    time.sleep(0.5)
    servoTest(1, 175, 170)
    time.sleep(0.5)
    servoTest(3, 75, 80)
    time.sleep(0.5)
    servoTest(1, 170, 165)
    time.sleep(0.5)
    servoTest(3, 80, 85)
    time.sleep(0.5)
    servoTest(1, 165, 165)
    time.sleep(0.5)
    servoTest(3, 85, 90)
    time.sleep(0.5)
    servoTest(1, 165, 150)
    
def grabBracelets():
    servoTest(4, 125, 125)
    servoTest(2, 80, 80)
    servoTest(3, 90, 90)
    servoTest(1, 150, 150)
    servoTest(0, 0,100)   

def removeBracelets():
    servoTest(4, 125, 125)
    servoTest(2, 80, 80)
    servoTest(3, 90, 75)
    servoTest(1, 150, 150)
    servoTest(0, 100,100)

def rotateToCatapult():
    servoTest(4, 125, 60)
    servoTest(2, 80, 80)
    #servoTest(3, 75, 75)
    #servoTest(1, 150, 150)
    #servoTest(0, 100,100)

def dropToCatapultStage1():
    #servoTest(4, 60, 60)
    servoTest(2, 80, 65)
    servoTest(3, 75, 90)
    servoTest(1, 150, 120)
    #servoTest(0, 100,100)
    
def dropToCatapultStage2():
    #servoTest(4, 60, 60)
    servoTest(2, 65, 125)
    #servoTest(3, 90, 90)
    #servoTest(1, 120, 120)
    #servoTest(0, 100,100)
    
def dropToCatapultStage3():
    #servoTest(4, 60, 60)
    servoTest(2, 65, 160)
    servoTest(3, 90, 70)
    #servoTest(1, 120, 120)
    #servoTest(0, 100,100)

def dropToCatapultStage4():
    #servoTest(4, 60, 60)
    #servoTest(2, 65, 160)
    #servoTest(3, 90, 70)
    servoTest(1, 120, 145)
    #servoTest(0, 100,100)

def releaseBracelets():
    servoTest(0, 100,0)
    time.sleep(1)
    servoTest(2, 160, 65)
    
def launchBracelets():
    complete = False

    while not complete:
        direction = input("Enter which side to launch from (L or R): ")

        if direction == "L":
            baseServo.angle = 0
            time.sleep(1)
            complete = True
        elif direction == "R":
            baseServo.angle = 180
            time.sleep(1)
            complete = True
        else:
            print("Invalid side. Try again.")

    complete = False
    while not complete:
        ready = input("Enter Y to launch: ")
        if ready == "Y":
            holdServo.angle = 0
            time.sleep(1)
            armServo.angle = 20
            time.sleep(1.5)
            holdServo.angle = 90
            print("Bracelets have launched...returning to rest state")
            time.sleep(1)
            armServo.angle = 135
            time.sleep(5)
            holdServo.angle = 0
            complete = True
        else:
            print("Invalid response. Try again.")

# again = 'Y'
# while again == 'Y':
#     servoNum = input('Enter the servo numbe you want to move (0-4): ')
#     startAngle = input(f'Enter the start angle of servo {servoNum} (0-180): ')
#     stopAngle = input(f'Enter the stop angle of servo {servoNum} (0-180): ')
#     servoTest(servoNum, startAngle, stopAngle)
#     print(f'Moving servo {servoNum}...')
#     again = input('Enter Y to continue or N to stop: ')

armServo.angle = 135
holdServo.angle = 0
baseServo.angle = 180
time.sleep(1)

def retrieveBracelets():
    startPosition()
    time.sleep(1)
    straightUp()
    time.sleep(1)
    lookLeft()
    time.sleep(1)
    lineUpBracelets()
    time.sleep(1)
    intoBracelets()
    time.sleep(1)
    grabBracelets()
    time.sleep(1)
    removeBracelets()
    time.sleep(1)
    rotateToCatapult()
    time.sleep(1)
    dropToCatapultStage1()
    time.sleep(1)
    dropToCatapultStage2()
    time.sleep(1)
    dropToCatapultStage3()
    time.sleep(1)
    dropToCatapultStage4()
    time.sleep(1)
    releaseBracelets()
    time.sleep(1)
    lookLeft()
    time.sleep(1)
#    startPosition()
# 
# time.sleep(3)

# launch()


# move(position_now, startPosition)
# time.sleep(1)
# move(position_now, straightUp)
# time.sleep(1)
# move(position_now, lineUpTree)
def deinitialize():
    pca.deinit()
    print('Deinitializing PCA and ending program...')


# Start position
# Servo 4 = 20
# Servo 3 (actually 2 wired) = 120
# Servo 2 (actually 3 wired) = 110
# Servo 1 = 120
# Servo 0 = 0 (OPEN)


# Straight up
# Servo 4 = 20
# Servo 3 (actually 2 wired) = 90
# Servo 2 (acutally 3 wired) = 85
# Servo 1 = 120
# Servo 0 = 0 (OPEN)

# Line up with tree
# Servo 4 = 125
# Servo 3 (actually 2 wired) = 90
# Servo 2 (acutally 3 wired) = 85
# Servo 1 = 120
# Servo 0 = 0 (OPEN)

# Line up with bracelets
# Servo 4 = 125
# Servo 3 (actually 2 wired) = 90
# Servo 2 (acutally 3 wired) = 85
# Servo 1 = 120
# Servo 0 = 0 (OPEN)

# Into the bracelets
# Servo 4 = 125
# Servo 3 (actually 2 wired) = 95
# Servo 2 (acutally 3 wired) = 75
# Servo 1 = 120
# Servo 0 = 0 (OPEN)

# Grab bracelets
# Servo 4 = 125
# Servo 3 (actually 2 wired) = 95
# Servo 2 (acutally 3 wired) = 75
# Servo 1 = 120
# Servo 0 = 100?

# Remove bracelets from tree
# Servo 4 = 125
# Servo 3 (actually 2 wired) = 90
# Servo 2 (acutally 3 wired) = 65
# Servo 1 = 120
# Servo 0 = 100?

# Rotate to catapult
# Servo 4 = 60
# Servo 3 (actually 2 wired) = 90
# Servo 2 (acutally 3 wired) = 65
# Servo 1 = 120
# Servo 0 = 100?

# Drop to catapult Stage 1
# Servo 4 = 60
# Servo 3 (actually 2 wired) = 65
# Servo 2 (acutally 3 wired) = 100
# Servo 1 = 120
# Servo 0 = 100?

# Drop to catapult Stage 2
# Servo 4 = 60
# Servo 3 (actually 2 wired) = 45
# Servo 2 (acutally 3 wired) = 125
# Servo 1 = 120
# Servo 0 = 100?

# Drop to catapult Stage 3
# Servo 4 = 60
# Servo 3 (actually 2 wired) = 70
# Servo 2 (acutally 3 wired) = 160
# Servo 1 = 120
# Servo 0 = 100?

# Release bracelets into catapult
# Servo 4 = 60
# Servo 3 (actually 2 wired) = 70
# Servo 2 (acutally 3 wired) = 160
# Servo 1 = 120
# Servo 0 = 0

# Go to camera rest position
# Servo 4 = 60
# Servo 3 (actually 2 wired) = 30
# Servo 2 (acutally 3 wired) = 135
# Servo 1 = 170
# Servo 0 = 0

# Look left
# Servo 4 = 125
# Servo 3 (actually 2 wired) = 30
# Servo 2 (acutally 3 wired) = 135
# Servo 1 = 180
# Servo 0 = 0

# Look right
# Servo 4 = 0
# Servo 3 (actually 2 wired) = 30
# Servo 2 (acutally 3 wired) = 135
# Servo 1 = 180
# Servo 0 = 0



