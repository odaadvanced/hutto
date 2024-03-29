# 08_light_meter.py
# From the code for the Box 1 kit for the Raspberry Pi by MonkMakes.com

#from guizero import App, Text
from PiAnalog import *
import time, math

p = PiAnalog()

multiplier = 2000 # increase to make more sensitive

def light_from_r(R):
    light = 1/math.sqrt(R) * multiplier
    if light > 100:
        light = 100
    # Sqareroot the reading to compress the range
    return light

# group together all of the GUI code
# Update the reading
# def update_reading():
#     light = light_from_r(p.read_resistance())
#     reading_str = "{:.0f}".format(light)
#     light_text.value = reading_str
#     light_text.after(200, update_reading)
#     return reading_str
# 
# app = App(title="Light Meter", width="400", height="300")
# Text(app, text="Light", size=32)
# light_text = Text(app, text="0", size=110)
# light_text.after(200, update_reading)
# app.display()