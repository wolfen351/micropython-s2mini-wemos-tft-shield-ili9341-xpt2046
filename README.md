# Thanks

Thanks to rdagger for the excellent starting point. Thanks to the author(s) - rdagger of the xpt2046.py and ili9341.py drivers! Thanks to the author of the fonts and font code.

# Description

This is the minimum starting point you need to start using a Wemos TFT 2.4 Touch Shield https://www.wemos.cc/en/latest/d1_mini_shield/tft_2_4.html with micropython on the S2 Mini. The program simply wipes the screen blue, and writes the coordinates of the touch onto the screen.

I have figured out the pins and the SPI interface, so you don't have to. The touch library automatically translates the touch co-ords, and does some simple debouncing.

* Note: You MUST update the micropython firmware on the board. I've included the firmware and a script to flash it on both linux (bash) and windows (powershell)

# Known issues

These are problems I know about, but havent been able to fix yet:

* The print() command does not seem to output anything to serial
* The touch screen sometimes seems to be a little unresponsive
* Graphics are really slow after the touch screen is initialized (because the touch screen needs much slower SPI baud)

Any contributions or pull requests are welcome! :)

