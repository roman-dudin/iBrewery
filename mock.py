BOARD = "BOARD"
OUT = "OUT"
IN = "IN"
BCM = "BCM"
LOW = "LOW"
HIGH = "HIGH"


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
            print("Reading mock temperature...")
            return 340
    return A()
