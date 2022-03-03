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

# initialize servos to starting positions
armServo.angle = 135
holdServo.angle = 0
baseServo.angle = 180
time.sleep(1)

# moves a servo from a start angle to a stop angle
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

def startPosition():
#     servos[4].angle = 15
#     servos[3].angle = 120
#     servos[2].angle = 120
    servoTest(4, 25, 15)
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
    servoTest(4, 20, 105)
    servoTest(3, 80, 40)
    servoTest(2, 85, 135)
    servoTest(1, 90, 180)
    servoTest(0, 0, 0)  

def lookRight():
    servoTest(4, 20, 0)
    servoTest(3, 80, 30)
    servoTest(2, 85, 135)
    servoTest(1, 90, 180)
    servoTest(0, 0, 0)

def lineUpBracelets():
    servoTest(4, 125, 125)
    servoTest(2, 135, 100)
    servoTest(3, 30, 60)
    servoTest(1, 180, 180)
    servoTest(0, 0, 0)
    
def intoBracelets():
    servoTest(0, 0, 0)   
    servoTest(2, 100, 80)
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
    #servoTest(1, 165, 150)
    
def grabBracelets():
    servoTest(4, 125, 115)
    servoTest(2, 80, 80)
    servoTest(3, 90, 90)
    servoTest(1, 150, 150)
    servoTest(0, 0,100)   

def removeBracelets():
    servoTest(4, 115, 115)
    servoTest(2, 80, 80)
    servoTest(3, 90, 75)
    servoTest(1, 150, 150)
    servoTest(0, 100,100)

def rotateToCatapult():
    servoTest(4, 115, 50)
    servoTest(2, 80, 80)

# def dropToCatapultStage1():
#     #servoTest(4, 60, 60)
#     servoTest(2, 80, 65)
#     servoTest(3, 75, 90)
#     servoTest(1, 150, 120)
# 
# def dropToCatapultStage2():
#     #servoTest(4, 60, 60)
#     servoTest(2, 65, 125)
 
def dropToCatapult():
    #servoTest(4, 60, 60)
    servoTest(2, 80, 160)
    #servoTest(3, 90, 70)

# def dropToCatapultStage4():
#     #servoTest(4, 60, 60)
#     #servoTest(2, 65, 160)
#     #servoTest(3, 90, 70)
#     servoTest(1, 120, 145)
    

# drop braclets into the catapult
def releaseBracelets():
    servoTest(0, 100,0)
    time.sleep(1)
    servoTest(2, 160, 80)

# swing catapult to launch left
def catapultSwingLeft():
    baseServo.angle = 0
    time.sleep(1)

# swing catapult to launch right
def captapultSwingRight():
    baseServo.angle = 180
    time.sleep(1)

# launch bracelets into the net   
def launchBracelets():
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

# Arm sequence to retreive bracelets
def retrieveBraceletsPreCam():
    startPosition()
    time.sleep(1)
    straightUp()
    time.sleep(1)
    lookLeft()
    time.sleep(1)
    lineUpBracelets()
    time.sleep(1)
    
def retrieveBraceletsPostCam():
    intoBracelets()
    time.sleep(1)
    grabBracelets()
    time.sleep(1)
    removeBracelets()
    time.sleep(1)
    rotateToCatapult()
    time.sleep(1)
    dropToCatapult()
#     time.sleep(1)
#     dropToCatapultStage2()
#     time.sleep(1)
#     dropToCatapultStage3()
#     time.sleep(1)
#     dropToCatapultStage4()
    time.sleep(1)
    releaseBracelets()
    time.sleep(1)
    lookLeft()
    time.sleep(1)
    
def retrieveBracelets2PreCam():    
    lookLeft()
    time.sleep(1)
    lineUpBracelets()
    time.sleep(1)
    
def retrieveBracelets2PostCam():
    intoBracelets()
    time.sleep(1)
    grabBracelets()
    time.sleep(1)
    removeBracelets()
    time.sleep(1)
    rotateToCatapult()
    time.sleep(1)
    dropToCatapult()
    time.sleep(1)
    releaseBracelets()
    time.sleep(1)
    lookLeft()
    time.sleep(1)

# deinitialize the i2c PCA9685
def deinitialize():
    pca.deinit()
    print('Deinitializing PCA and ending program...')
