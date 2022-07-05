from io import BytesIO
from PIL import Image
import sys
import time
import os

"""
----------------------CONFIG---------------------------
"""

# Size of the OLED Screen
print("Screen width?")

screen_width = int(input())

print("Screen height?")
screen_height = int(input())

# Size of the images. NOTE: All must have the same height and width!
print("What width are the images?")
img_width = int(input())

print("What height are the images?")
img_height = int(input())

# Pins that are connected to the screen
print("On which Pin is SDA?")
SDA_pin = int(input())

print("On which Pin is SCL?")
SCL_pin = int(input())

print("What frequency should be used?")
frequency = int(input())  # default value

# Time between each frame
print("what delay between the images?")
delay = input()

# position where the image is going to be displayed
print("X on screen")
img_x_on_screen = int(input())

print("Y on screen")
img_y_on_screen = int(input())

# deletes all files in the "files" directory
print("Should I delete the images in the folder?")
self_destruction = bool(input())

start_time = time.time()



"""
-----------------------CONFIG---------------------------
"""

print("\n\n------------------------------------------------------\n\n")


print("\n")
print(
    "from machine import Pin, I2C\nfrom ssd1306 import SSD1306_I2C\nimport time\nimport framebuf\n\n")  # Import all needed libraries. NOTE: The SSD1306 library is default not installed.

print("WIDTH = " + str(screen_width) + "\nHEIGHT = " + str(screen_height))
print("\n\n")

print("i2c = I2C(0, scl = Pin(" + str(SCL_pin) + "), sda = Pin(" + str(SDA_pin) + "), freq=" + str(frequency) + ")")
print("oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)")
print("\n\n")
print("while True:")

files = os.listdir(os.getcwd() + "\\files")

step = 1

for file in files:
    path_to_image = str(os.getcwd() + "\\files\\" + file)
    x = img_width
    y = img_height

    im = Image.open(path_to_image).convert('1')
    im_resize = im.resize((x, y))
    buf = BytesIO()
    im_resize.save(buf, 'ppm')
    byte_im = buf.getvalue()
    temp = len(str(x) + ' ' + str(y)) + 4
    output = byte_im[temp::]

    print("    b" + str(step) + " = bytearray(" + str(output) + ")")

    print("    fb" + str(step) + " = framebuf.FrameBuffer(b" + str(step) + "," + str(img_width) + " , " + str(
        img_height) + ", framebuf.MONO_HLSB)")
    print("\n")

    print("    oled.fill(0)")
    print("    oled.blit(fb" + str(step) + ", " + str(img_x_on_screen) + " , " + str(img_y_on_screen) + ")")
    print("    oled.show()")
    print("    time.sleep(" + str(delay) + ")")
    print("\n\n")
    if self_destruction:
        os.system("del " + os.getcwd() + "\\files\\" + file)
    step += 1

print("\n\n------------------------------------------------------\n\n")
print("Finished")
print("took --- %s seconds ---" % (time.time() - start_time))
input()

