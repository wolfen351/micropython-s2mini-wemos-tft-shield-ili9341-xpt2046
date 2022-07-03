# Thanks

Thanks to rdagger for the excellent starting point. Thanks to the author(s) - rdagger of the xpt2046.py and ili9341.py drivers! Thanks to the author of the fonts and font code.

# Description

This is the minimum starting point you need to start using a Wemos TFT 2.4 Touch Shield https://www.wemos.cc/en/latest/d1_mini_shield/tft_2_4.html with micropython on the S2 Mini. The program simply wipes the screen blue, and writes the coordinates of the touch onto the screen.

I have figured out the pins and the SPI interface, so you don't have to. The touch library automatically translates the touch co-ords, and does some simple debouncing.

* Note: You MUST update the micropython firmware on the board. I've included the firmware and a script to flash it on both linux (bash) and windows (powershell)

The key code is:

```
    # High speed SPI for graphics
    spi = SPI(1, baudrate=100000000, sck=Pin(7), mosi=Pin(11), miso=Pin(9))
    display = Display(spi, dc=Pin(12), cs=Pin(5), rst=Pin(0))
    display.clear(color565(64, 0, 255))

    # Low speed SPI for touch
    spi = SPI(1, baudrate=2000000, sck=Pin(7), mosi=Pin(11), miso=Pin(9))
    xpt = Touch(spi, cs=Pin(18))
```

# How to use

First time preparation:
* simply wipe the board clean (the first time)
* flash the Micropython updated firmware using the `flash_python_s2mini.ps1` file (update the port). 
* call `sync.ps1 --force` to copy all the files to the board

Subsequent loads:
* Make code changes, then call `sync.ps1` to send only the files that have changed to the board.

This works by maintaining a version file, and pushing that and a lastupdated file to the board. When you call sync again, it pulls the version and lastupdate time from the board and only sends files to the board that have changed.

# Structure

Code files:

* main.py - The main code that inits the display and touch screen and renders the co-ordinates (also does the pin assignments)
* ili9341.py - Display driver (thanks rdagger)
* xpt2046.py - Touch driver  (thanks rdagger)
* xglcd_font.py - Font driver 

Sync files:

* bump_version.* - Code to bump the version number each time you sync new files to the board
* flash_python_s2mini.* - Code to flash the board to latest micropython binary
* sync.* - Code to sync the file changes locally to the board via serial (usb)
* version - The version of the code
* lastedit.dat - The last edit datetime

# Known issues

These are problems I know about, but havent been able to fix yet:

* The print() command does not seem to output anything to serial
* The touch screen sometimes seems to be a little unresponsive
* Graphics are really slow after the touch screen is initialized (because the touch screen needs much slower SPI baud)
* It doesn't make the `fonts` folder on the board on first sync. Call `ampy --port COM3 mkdir fonts` to make it manually

Any contributions or pull requests are welcome! :)

