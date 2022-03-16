import integration
import os
import time
import steppermotortest
import arm
import oled
# import arm

start_time = time.time()


try:
   oled.dispVT()
   integration.main()

except:
   steppermotortest.turnOffMotors()
   integration.stopCamera()
   arm.servosOff()
   print("\nCtrl-C pressed. Stopping PIGPIO and exiting...")
   print('motors off')

# thread1.join()
# thread2.join()
