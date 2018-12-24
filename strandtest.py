#!/usr/bin/env python3
# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import time
from neopixel import *
import argparse
import random

# LED strip configuration:
LED_COUNT      = 125      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53



# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i+j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, wheel((i+j) % 255))
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def rain(strip, wait_s=0.075, iterations=25):
        pickedNumbers = []
        column = random.randint(0,24)

        for x in range(iterations):
                while column in pickedNumbers:
                        column = random.randint(0,24) #Stop the same collum getting choosen twice

                pickedNumbers.append(column)

                colour = Color(random.randint(0,255), random.randint(0,255), random.randint(0,255))

                strip.setPixelColor(100 + column, colour)
                strip.show()
                time.sleep(wait_s)

                for i in range(1,5):
                        strip.setPixelColor((100+column)-(25*i), colour)
                        strip.setPixelColor((100+column)-(25*(i-1)), Color(0,0,0))
                        strip.show()
                        time.sleep(wait_s)

def randfill(strip, wait_s=0.1):
        pickedNumbers = []
        light = random.randint(0,124)
        colour = Color(255,255,255)

        for x in range(25):
                while light in pickedNumbers:
                        light = random.randint(0,124) #Stop the same collum getting choosen twice

                pickedNumbers.append(light)
                strip.setPixelColor(light, colour)
                time.sleep(wait_s)
                strip.show()

def randfill_top(strip, wait_s=0.05):
        pickedNumbers = []
        light = random.randint(0,24)
        colour = Color(255,255,255)

        for x in range(25):
                while light in pickedNumbers:
                        light = random.randint(0,24) #Stop the same collum getting choosen twice

                pickedNumbers.append(light)
                strip.setPixelColor(light + 100, colour)
                time.sleep(wait_s)
                strip.show()

def stripClear(strip):
        for i in range(LED_COUNT):
                strip.setPixelColor(i, Color(0,0,0))
        strip.show()

def singleColorWipe(strip, color, wait_ms=25):
        strip.setPixelColor(0, color)
        for i in range(1,strip.numPixels()):
                strip.setPixelColor(i, color)
                strip.setPixelColor(i-1, Color(0,0,0))
                strip.show()
                time.sleep(wait_ms/1000.0)
        stripClear(strip)

def singleColorWipeDown(strip, color, wait_ms=500):
        strip.setPixelColor(strip.numPixels(), color)
        for i in range(strip.numPixels()-1, 0, -1):
                strip.setPixelColor(i, color)
                #strip.setPixelColor(i+1, Color(0,0,0))
                strip.show()
                time.sleep(wait_ms/1000.0)

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')


    print(strip.numPixels())
    try:
                stripClear(strip)
                while True:
                        singleColorWipe(strip, Color(255,0,0))
                        singleColorWipe(strip, Color(0,255,0))
                        singleColorWipe(strip, Color(0,0,255))
                        singleColorWipe(strip, Color(255,255,255))
                        randfill_top(strip)
                        time.sleep(1)
                        rain(strip)
                        time.sleep(1)
                        stripClear(strip)
                        time.sleep(1)
                        theaterChase(strip, Color(127, 127, 127))  # White theater chase
                        theaterChase(strip, Color(127,   0,   0))  # Red theater chase
                        theaterChase(strip, Color(  0,   0, 127))  # Blue theater chase
                        theaterChase(strip, Color(  0, 127,   0))
                        time.sleep(1)
                        stripClear(strip)
                        time.sleep(2)
                        colorWipe(strip, Color(255, 0, 0))  # Red wipe
                        colorWipe(strip, Color(0, 255, 0))  # Red wipe
                        colorWipe(strip, Color(0, 0, 255))  # Red wipe
                        time.sleep(1)
                        stripClear(strip)
                        time.sleep(1)
                        rainbowCycle(strip, wait_ms=200, iterations=1)
                        time.sleep(1)
                        stripClear(strip)
                        time.sleep(1)



    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0,0,0), 0.1)
