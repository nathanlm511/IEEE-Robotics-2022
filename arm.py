from time import sleep
from board import SCL, SDA
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

i2c = busio.I2C(SCL, SDA)

#pca = PCA9685(i2c)
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
baseServo = servo.Servo(pca.channels[8], min_pulse = 500, max_pulse = 2500)
armServo = servo.Servo(pca.channels[6], min_pulse = 500, max_pulse = 2500)

# settings for SG90 servos
holdServo = servo.Servo(pca.channels[7], min_pulse = 500, max_pulse = 2500)

# initialize servos to starting positions
armServo.angle = 135
holdServo.angle = 0
baseServo.angle = 180
sleep(1)

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
            sleep(0.06)
            #print(newAngle)
        if newAngle != stop:
            servos[servoNum].angle = stop
            #print(stop)
    elif start > stop:
        for i in range(numSteps):
            newAngle = start - (i * 5)
            servos[servoNum].angle = newAngle
            sleep(0.06)
            #print(newAngle)
        if newAngle != stop:
            servos[servoNum].angle = stop
            #print(stop)

def startPosition():
#     servos[4].angle = 15
#     servos[3].angle = 120
#     servos[2].angle = 120
    #servoTest(4, 25, 15)
    #sleep(1)
    #servoTest(3, 110, 120)
    #servoTest(2, 100, 80)
    #servoTest(1, 110, 165)
    #servoTest(0, 1, 0)
    #servoTest(3, 120, 135)
    
    servos[4].angle = 10
    servos[3].angle = 80
    servos[2].angle = 85
    servos[1].angle = 165
    servos[0].angle = 0
    servoTest(0, 0, 90)
    servoTest(4, 10, 15)
    servoTest(1, 165, 180)
    servoTest(2, 85, 125)
    servoTest(3, 80, 110)
    servoTest(2, 125, 120)
    servoTest(3, 110, 130)
    
def straightUp():
    servoTest(3, 90, 80)
    sleep(0.5)
    servoTest(2, 120, 85)
    servoTest(1, 180, 165)
    servoTest(0, 90, 0)
    servoTest(4, 15, 20)
    #servoTest(4, 20, 20)
    #servoTest(3, 135, 80)
    #servoTest(2, 80, 85)
    #servoTest(1, 165, 165)
    #servoTest(0, 0, 0)
    
def lookLeft():
    servoTest(4, 20, 105)
    servoTest(3, 80, 40)
    servoTest(2, 85, 135)
    servoTest(1, 90, 180)
    servoTest(0, 0, 0)  

def lookLeftInstant():
    servos[4].angle = 105
    servos[3].angle = 40
    servos[2].angle = 135
    servos[1].angle = 180
    servos[0].angle = 0

def lookRight():
    servoTest(4, 20, 0)
    servoTest(3, 80, 30)
    servoTest(2, 85, 135)
    servoTest(1, 90, 180)
    servoTest(0, 0, 0)

def lookRightInstant():
    servos[4].angle = 10
    servos[3].angle = 40
    servos[2].angle = 135
    servos[1].angle = 180
    servos[0].angle = 0

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
    sleep(0.5)
    servoTest(1, 180, 175)
    sleep(0.5)
    servoTest(3, 65, 75)
    sleep(0.5)
    servoTest(1, 175, 170)
    sleep(0.5)
    servoTest(3, 75, 80)
    sleep(0.5)
    servoTest(1, 170, 165)
    sleep(0.5)
    servoTest(3, 80, 85)
    sleep(0.5)
    servoTest(1, 165, 165)
    sleep(0.5)
    servoTest(3, 85, 90)
    
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
 
def dropToCatapult():
    servoTest(2, 80, 160)
    
# drop braclets into the catapult
def releaseBracelets():
    servoTest(0, 100,0)
    sleep(1)
    servoTest(2, 160, 80)

# swing catapult to launch left
def catapultSwingLeft():
    baseServo.angle = 0
    sleep(1)
    
def catapultSwingPos5():
    baseServo.angle = 20
    sleep(1)

# swing catapult to launch right
def catapultSwingRight():
    baseServo.angle = 180
    sleep(1)

# launch bracelets into the net   
def launchBracelets():
    holdServo.angle = 0
    sleep(1)
    armServo.angle = 20
    sleep(1.5)
    holdServo.angle = 90
    print("Bracelets have launched...returning to rest state")
    sleep(1)
    armServo.angle = 135
    sleep(5)
    holdServo.angle = 0

# Arm sequence to retreive bracelets
def retrieveBraceletsPreCam():
    straightUp()
    sleep(0.5)
    lookLeftInstant()
    sleep(0.5)
    lineUpBracelets()
    sleep(0.5)
    
def retrieveBraceletsPostCam():
    intoBracelets()
    sleep(0.5)
    grabBracelets()
    sleep(0.5)
    removeBracelets()
    sleep(0.5)
    rotateToCatapult()
    sleep(0.5)
    dropToCatapult()
    sleep(0.5)
    releaseBracelets()
    sleep(0.5)
    lookLeft()
    
def retrieveBracelets2PreCam():
    lookLeftInstant()
    sleep(0.5)
    lineUpBracelets()
    sleep(0.5)
    
def retrieveBracelets2PostCam():
    intoBracelets()
    sleep(1)
    grabBracelets()
    sleep(1)
    removeBracelets()
    sleep(1)
    rotateToCatapult()
    sleep(1)
    dropToCatapult()
    sleep(1)
    releaseBracelets()
    sleep(1)
    lookLeft()

# turn off the servos
def servosOff():
    for i in range(8):
        pca.channels[i].duty_cycle = 0

# deinitialize the i2c PCA9685
def deinitialize():
    pca.deinit()
    print('Deinitializing PCA and ending program...')
