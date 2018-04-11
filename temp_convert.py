from scipy import interpolate

x = [0, 23, 25, 34, 35, 52, 53, 55, 68, 72, 75, 77, 84, 88, 99, 100]
y = [0, 341, 366, 461, 474, 644, 655, 670, 778, 800, 817, 830, 863, 880, 906, 910]
readout_to_celsius = interpolate.interp1d(y, x)
celsius_to_readout = interpolate.interp1d(x, y)


def convert_to_celsius(r):
    if r >= 910:
        return 100
    if r <= 0:
        return 0
    return readout_to_celsius(r).tolist()


def convert_to_readout(c):
    if c >= 100:
        return 910
    if c <= 0:
        return 0
    return celsius_to_readout(c).tolist()
