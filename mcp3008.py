# Import SPI library (for hardware SPI) and MCP3008 library.

import os
if os.name == 'posix':
    import Adafruit_GPIO.SPI as SPI
    import Adafruit_MCP3008
    print("USE: ORIGINAL Adafruit_GPIO.SPI")
else:
    import mock as SPI
    import mock as Adafruit_MCP3008
    print("USE: MOCK Adafruit_GPIO.SPI")


# Software SPI configuration:
CLK = 18
MISO = 23
MOSI = 24
CS = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)


def get_temp():
    return mcp.read_adc(0)
