from tracemalloc import stop
import integration
import steppermotortest
import arm
import pigpio
import signal
import sys
# import oled
# import os
# import time

pi = pigpio.pi()

START_GPIO = 7
STOP_GPIO = 8

pi.set_mode(START_GPIO, pigpio.INPUT)
pi.set_pull_up_down(START_GPIO, pigpio.PUD_UP)


def stop_hander():
   steppermotortest.turnOffMotors()
   integration.stopCamera()
   arm.servosOff()
   print("\nCtrl-C pressed. Stopping PIGPIO and exiting...")
   print('motors off')
   sys.exit()


# declare handler for estop
signal.signal(signal.SIGINT, stop_hander)
cb1 = pi.callback(STOP_GPIO, pigpio.EITHER_EDGE, stop_hander)


arm.startPosition()
#oled.dispVT()

# wait for start button
buttonNotPressed = True
while buttonNotPressed:
   buttonState = pi.read(START_GPIO)
   if not buttonState:
      buttonNotPressed = False

print('STARTING INTEGRATION MAIN')
integration.main()
