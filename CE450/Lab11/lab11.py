from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.led_matrix.device import max7219
from luma.core.legacy import text
from luma.core.legacy.font import proportional, CP437_FONT, LCD_FONT
import time

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, rotate=1)
virtual = viewport(device, width=200, height=400)


def displayLetter(letter: str):
    with canvas(device) as draw:
        text(draw, (0, 0), letter, fill="white", font=proportional(CP437_FONT))


def main():
    while True:
        displayLetter("A")
        time.sleep(2)
        displayLetter("B")
        time.sleep(2)


def destroy():
    pass


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        destroy()
