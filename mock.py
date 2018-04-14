BOARD = "BOARD"
OUT = "OUT"
IN = "IN"
BCM = "BCM"
LOW = "LOW"
HIGH = "HIGH"
debug_temp = 999.0


def setmode(a):
    print("setmode ", a)


def setup(a, b, initial="default"):
    print("setup ", a, " ", b, " ", initial)


def output(a, b):
    print("setup ", a, " ", b)


def cleanup():
    print("cleanup")


def setwarnings(a):
    print("setmode ", a)


def MCP3008(clk, cs, miso, mosi):
    print("MCP3008")

    class A:
        def read_adc(self, par):
            global debug_temp
            # print("Reading mock temperature...")
            return debug_temp
    return A()


def set_temp_debug(temp):
    global debug_temp
    debug_temp = temp
