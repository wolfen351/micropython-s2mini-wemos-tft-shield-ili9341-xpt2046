"""ILI9341 demo (shapes)."""
from time import sleep
from ili9341 import Display, color565
from machine import Pin, SPI
from xpt2046 import Touch
from xglcd_font import XglcdFont

robotron = XglcdFont('fonts/ArcadePix9x11.c', 9, 11)

def start():
    """Test code."""
    # High speed SPI for graphics
    spi = SPI(1, baudrate=100000000, sck=Pin(7), mosi=Pin(11), miso=Pin(9))
    display = Display(spi, dc=Pin(12), cs=Pin(5), rst=Pin(0))
    display.clear(color565(64, 0, 255))

    # Low speed SPI for touch
    spi = SPI(1, baudrate=2000000, sck=Pin(7), mosi=Pin(11), miso=Pin(9))
    xpt = Touch(spi, cs=Pin(18))

    tt = 0
    while True: 
        t = xpt.get_touch()
        if (t is not None):
            tt += 1
            display.draw_text(40, 40, str(t), robotron, color565(255, 255, 255), background=color565(64, 0, 255))
            display.draw_text(40, 60, str(tt), robotron, color565(255, 255, 255), background=color565(64, 0, 255))

start()
