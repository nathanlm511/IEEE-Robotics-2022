import integration
import threading
import os
import time
from pygame import mixer

def Speaker():
    # for i in range(20):
        # print("Play sound")
       
   mixer.init()
   sound = mixer.Sound('TechTriump.wav')
   sound.play()

def OLED():
    for i in range(20):
        print("Display updated")

class OLEDThread(threading.Thread):
   def __init__(self, name):
      threading.Thread.__init__(self)
      self.name = name

   def run(self):
      print("Starting " + self.name)
      OLED()
      print("Exiting "+ self.name)

class SpeakerThread(threading.Thread):
   def __init__(self, name):
      threading.Thread.__init__(self)
      self.name = name

   def run(self):
      print("Starting " + self.name)
      Speaker()
      print("Exiting "+ self.name)

class IntegrationThread(threading.Thread):
   def __init__(self, name):
      threading.Thread.__init__(self)
      self.name = name

   def run(self):
      print("Starting " + self.name)
      integration.main()
      print("Exiting "+ self.name)

thread1 = IntegrationThread("integration thread")
thread2 = OLEDThread("OLED thread")
thread3 = SpeakerThread("speaker thread")

thread1.start()
thread2.start()
thread3.start()