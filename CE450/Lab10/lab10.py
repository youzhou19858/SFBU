#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

# ne555 pin3 connect to BCM GPIO17
SigPin = 17    # BCM 17

g_count = 0


def print_msg():
    print("========================================")
    print("|                  Ne555               |")
    print("|    ------------------------------    |")
    print("| Output pin of ne555 connect to gpio0;|")
    print("|                                      |")
    print("|  Count the pluses procude by NE555.  |")
    print("|                                      |")
    print("|                            SunFounder|")
    print("========================================\n")
    print('Program is running...')
    print('Please press Ctrl+C to end the program...')
    raw_input("Press Enter to begin\n")


def count(ev=None):
    global g_count
    g_count += 1


def setup():
    GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
    # Set Pin's mode is input, and pull up to high level(3.3V)
    GPIO.setup(SigPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(SigPin, GPIO.RISING,
                          callback=count)  # wait for rasing


def main():
    print_msg()
    while True:
        print(f'g_count = {g_count}')
        time.sleep(0.001)


def destroy():
    GPIO.cleanup()    # Release resource


if __name__ == '__main__':     # Program start from here
    setup()
    try:
        main()
    # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    except KeyboardInterrupt:
        destroy()
