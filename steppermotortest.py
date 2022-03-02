from time import sleep
import pigpio
# import serial
# from arm import *

# ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
# ser.reset_input_buffer()

# define digital IO pins
STEP1 = 12 # PWM signal

# direction pins
DIR1 = 6
DIR2 = 17
DIR3 = 16
DIR4 = 26

# Define directions
CW = 1
CCW = 0

# Driver Enable Pins (active low)
EN1 = 27
EN2 = 22
EN3 = 23
EN4 = 24

# Set up microstepping
MODE = (20, 5, 21) # Microstep resolution GPIO pins
RESOLUTION = {'Full': (0, 0, 0),
			  'Half': (1, 0, 0),
			  '1/4': (0, 1, 0),
			  '1/8': (1, 1, 0),
			  '1/16': (1, 0, 1),
			  '1/32': (1, 0, 1)}

# Conect the pigpiod daemon
pi = pigpio.pi()


# Disable all motor drivers
pi.write(EN1, 1)
pi.write(EN2, 1)
pi.write(EN3, 1)
pi.write(EN4, 1)
sleep(1)

# set microstep value
for i in range(3):
	pi.write(MODE[i], RESOLUTION['1/32'][i])

# Enable motor drivers one at a time
pi.write(EN1, 0)
sleep(1)
pi.write(EN2, 0)
sleep(1)
pi.write(EN3, 0)
sleep(1)
pi.write(EN4, 0)


def forwards():
	frequency = 1500
	duty_cycle = 500000
	pi.hardware_PWM(STEP1, frequency, duty_cycle)

	pi.write(DIR1, 0)
	pi.write(DIR2, 1)
	pi.write(DIR3, 0)
	pi.write(DIR4, 1)

def stopMoving():
	frequency = 0
	duty_cycle = 0
	pi.hardware_PWM(STEP1, frequency, duty_cycle)
	
def forwardSmall():
    forwards()
    sleep(0.25)
    stopMoving()

def clockwise():
	frequency = 1000
	duty_cycle = 500000
	pi.hardware_PWM(STEP1, frequency, duty_cycle)

	pi.write(DIR1, 0)
	pi.write(DIR2, 0)
	pi.write(DIR3, 0)
	pi.write(DIR4, 0)

def counterClockwise():
	frequency = 1000
	duty_cycle = 500000
	pi.hardware_PWM(STEP1, frequency, duty_cycle)

	pi.write(DIR1, 1)
	pi.write(DIR2, 1)
	pi.write(DIR3, 1)
	pi.write(DIR4, 1)

def backwards():
	frequency = 1500
	duty_cycle = 500000
	pi.hardware_PWM(STEP1, frequency, duty_cycle)

	pi.write(DIR1, 1)
	pi.write(DIR2, 0)
	pi.write(DIR3, 1)
	pi.write(DIR4, 0)

def backwardsSmall():
    backwards()
    sleep(0.25)
    stopMoving()
# 	frequency = 500 # 0 (off) to 1-125M
# 	duty_cycle = 0 # 0 (off) to 1M (fully on)
# 	pi.hardware_PWM(STEP1, frequency, duty_cycle)
# 	# Disable all motor drivers
# 	pi.write(EN1, 1)
# 	pi.write(EN2, 1)
# 	pi.write(EN3, 1)
# 	pi.write(EN4, 1)
# 	sleep(1)
# 	pi.stop()

# turns off motors
def turnOffMotors():
	frequency = 500 # 0 (off) to 1-125M
	duty_cycle = 0 # 0 (off) to 1M (fully on)
	pi.hardware_PWM(STEP1, frequency, duty_cycle)
	# Disable all motor drivers
	pi.write(EN1, 1)
	pi.write(EN2, 1)
	pi.write(EN3, 1)
	pi.write(EN4, 1)
	sleep(1)
	pi.stop()

# try:
# 	while True:

# 		try:
# 			line = ser.readline().decode('utf-8').rstrip()
# 			print(line)
# 			if line == "F":
# 				forwards()
# 			elif line == "S":
# 				print("STOP!")
# 				stopMoving()
# 			elif line == "A":
# 				print("Executing arm code")
# 				arm()
# 				launch()
# 				deinitialize()
# 			elif line == "C":
# 				clockwise()
# 			elif line == "Fl":
# 				ser.reset_input_buffer()
# 		except:
# 			pass
# 		sleep(0.025)
#        ser.reset_input_buffer()
#try:
#    while True:
#        direction = input("Enter a direction (F, B, L, R, CW, CCW, S): ")
#        if direction == "S":
#            frequency = 0 # 0 (off) to 1-125M
#            duty_cycle = 500000 # 0 (off) to 1M (fully on)
#            pi.hardware_PWM(STEP1, frequency, duty_cycle)
#        else:
#            frequency = 1000 # 0 (off) to 1-125M
#            duty_cycle = 500000 # 0 (off) to 1M (fully on)
#            pi.hardware_PWM(STEP1, frequency, duty_cycle)
#            
#        if direction == "F":
#            pi.write(DIR1, 0)
#            pi.write(DIR2, 1)
#            pi.write(DIR3, 0)
#            pi.write(DIR4, 1)
#        elif direction == "B":
#            pi.write(DIR1, 1)
#            pi.write(DIR2, 0)
#            pi.write(DIR3, 1)
#            pi.write(DIR4, 0)
#        elif direction == "L":
#            pi.write(DIR1, 1)
#            pi.write(DIR2, 1)
#            pi.write(DIR3, 0)
#            pi.write(DIR4, 0)
#        elif direction == "R":
#            pi.write(DIR1, 0)
#            pi.write(DIR2, 0)
#            pi.write(DIR3, 1)
#            pi.write(DIR4, 1)
#        elif direction == "CW":
#            pi.write(DIR1, 0)
#            pi.write(DIR2, 0)
#            pi.write(DIR3, 0)
#            pi.write(DIR4, 0)
#        elif direction == "CCW":
#            pi.write(DIR1, 1)
#            pi.write(DIR2, 1)
#            pi.write(DIR3, 1)
#            pi.write(DIR4, 1)
#        else:
#            pass
# except KeyboardInterrupt:
# 	print('\nCtrl-C pressed. Stopping PIGPIO and exiting...')
# finally:
# 	frequency = 500 # 0 (off) to 1-125M
# 	duty_cycle = 0 # 0 (off) to 1M (fully on)
# 	pi.hardware_PWM(STEP1, frequency, duty_cycle)
# 	# Disable all motor drivers
# 	pi.write(EN1, 1)
# 	pi.write(EN2, 1)
# 	pi.write(EN3, 1)
# 	pi.write(EN4, 1)
# 	sleep(1)
# 	pi.stop()
