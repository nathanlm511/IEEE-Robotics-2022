import integration
import threading
import os
import time
import steppermotortest
import arm

global time_expired
global robot_activeS
start_time = time.time()

def OLED():
    # for i in range(20):
        # print("Display updated")
   RST = 4 # Reset gpio pin
   # 128x64 display with hardware I2C:
   disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
   # Initialize library.
   disp.begin()

   # Clear display.
   disp.clear()
   disp.display()

   # Create blank image for drawing.
   # Make sure to create image with mode '1' for 1-bit color.
   width = disp.width
   height = disp.height
   image = Image.new('1', (width, height))

   # Get drawing object to draw on image.
   draw = ImageDraw.Draw(image)

   # Draw a black filled box to clear the image.
   draw.rectangle((0,0,width,height), outline=0, fill=0)
   # Draw some shapes.
   # First define some constants to allow easy resizing of shapes.
   padding = 2
   shape_width = 20
   top = padding
   bottom = height-padding
   # Move left to right keeping track of the current x position for drawing shapes.
   x = padding
   # Draw an ellipse.
   draw.ellipse((x, top , x+shape_width, bottom), outline=255, fill=0)
   x += shape_width+padding
   # Draw a rectangle.
   draw.rectangle((x, top, x+shape_width, bottom), outline=255, fill=0)
   x += shape_width+padding
   # Draw a triangle.
   draw.polygon([(x, bottom), (x+shape_width/2, top), (x+shape_width, bottom)], outline=255, fill=0)
   x += shape_width+padding
   # Draw an X.
   draw.line((x, bottom, x+shape_width, top), fill=255)
   draw.line((x, top, x+shape_width, bottom), fill=255)
   x += shape_width+padding
   # Load default font.
   font = ImageFont.load_default()

   # Alternatively load a TTF font.
   # Some other nice fonts to try: http://www.dafont.com/bitmap.php
   #font = ImageFont.truetype('Minecraftia.ttf', 8)

   # Write two lines of text.
   draw.text((x, top),    'Hello',  font=font, fill=255)
   draw.text((x, top+20), 'World!', font=font, fill=255)

   # Display image.
   disp.image(image)
   disp.display()

   while not time_expired:
      # wait until time expires
      pass


class OLEDThread(threading.Thread):
   def __init__(self, name):
      threading.Thread.__init__(self)
      self.name = name

   def run(self):
      print("Starting " + self.name)
      # OLED()

class IntegrationThread(threading.Thread):
   def __init__(self, name):
      threading.Thread.__init__(self)
      self.name = name

   def run(self):
      print("Starting " + self.name)
      integration.main(time_expired, robot_active)
      print("Exiting "+ self.name)

robot_active=True
time_expired = False

# thread1 = IntegrationThread("integration thread")
# thread2 = OLEDThread("OLED thread")

# thread1.start()
# thread2.start()

# The timer probably wont work***********************
# currently set to 10 seconds for testing purposes
try:
   integration.main(time_expired, robot_active)
   while time.time() - start_time < 10 and robot_active:
      pass

   if robot_active and time.time() - start_time >= 10:
      time_expired = True
      print("Time expired!")

except:
   time_expired = True
#    arm.captapultSwingRight()
#    time.sleep(1)
#    arm.startPosition()
#    arm.deinitialize()
   steppermotortest.turnOffMotors()
   print("\nCtrl-C pressed. Stopping PIGPIO and exiting...")
   print('motors off')

# thread1.join()
# thread2.join()
