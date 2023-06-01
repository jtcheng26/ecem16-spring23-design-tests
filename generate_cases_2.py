import random
import math

ASCII_ZERO_START = 48
ASCII_TEN_END = 58


def to_ascii(x):
    return x + ASCII_ZERO_START


def to_digit(ascii):
    return ascii - ASCII_ZERO_START


def bitstostr(x):
    s = ""
    for i in range(7):
        s = ("1" if ((x >> i) & 1) else "0") + s
    return s


def to2s(x):
    s = ""
    for i in range(7):
        s = ("1" if ((x >> i) & 1) else "0") + s
    s = ("1" if (x != 0 and x * (-1) == abs(x)) else "0") + s
    return s


print("SIGN[7] D1[7] D0[7] TC[8] NAN")

for i in range(-99, 100):
    sign = i * (-1) == abs(i)
    d1 = math.floor(abs(i) / 10)
    d0 = abs(i) % 10
    bits1 = bitstostr(to_ascii(d1))
    bits0 = bitstostr(to_ascii(d0))
    print(f"{'0101101' if sign else '0101011'} {bits1} {bits0} {to2s(i)} 0")
    for j in range(128):
        if random.randint(0, 63) == 0:
            if j != 43 and j != 45:
                print(f"{bitstostr(j)} {bits1} {bits0} 11111111 1")
            if j < 48 or j > 57:
                print(
                    f"{'0101101' if sign else '0101011'} {bitstostr(j)} {bits0} 11111111 1")
                print(
                    f"{'0101101' if sign else '0101011'} {bits1} {bitstostr(j)} 11111111 1")
                print(
                    f"{'0101101' if sign else '0101011'} {bitstostr(j)} {bitstostr(j)} 11111111 1")


print("0101011 0110000 0110000 00000000 0")
