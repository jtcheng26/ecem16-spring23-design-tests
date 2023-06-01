import random


def bitstostr(x):
    s = ""
    for i in range(16):
        s += "1" if ((x >> i) & 1) else "0"
    return s


def numones(x):
    y = 0
    for i in range(16):
        y += 1 if ((x >> i) & 1) else 0
    return y


def randnones(n):
    s = []
    for i in range(n):
        s.append("1")
    for i in range(16 - n):
        s.append("0")
    for i in range(n):
        temp = s[i]
        j = random.randrange(i, 16)
        s[i] = s[j]
        s[j] = temp
    return "".join(s)


print("A[16] B[16] AWON DOUT[16]")

for k in range(16):
    i = 2 ** 16 - 1 - 2 ** k
    j = 2 ** 16 - 1
    ni = 15
    nj = 16
    bi = bitstostr(i)
    bj = bitstostr(j)
    print(f"{bi} {bj} {'1' if ni >= nj else '0'} {bi if ni >= nj else bj}")
    print(f"{bj} {bi} {'1' if nj >= ni else '0'} {bj if nj >= ni else bi}")

for k in range(16):
    i = 0
    j = 2 ** k
    ni = 0
    nj = 1
    bi = bitstostr(i)
    bj = bitstostr(j)
    print(f"{bi} {bj} {'1' if ni >= nj else '0'} {bi if ni >= nj else bj}")
    print(f"{bj} {bi} {'1' if nj >= ni else '0'} {bj if nj >= ni else bi}")


for n in range(16):
    for m in range(16):
        for k in range(10 if n * m > 16 else n * m):
            i = randnones(n)
            j = randnones(m)
            print(f"{i} {j} {'1' if n >= m else '0'} {i if n >= m else j}")
            print(f"{j} {i} {'1' if m >= n else '0'} {j if m >= n else i}")

for k in range(500):
    i = random.randint(0, 2 ** 16 - 1)
    j = random.randint(0, 2 ** 16 - 1)
    ni = numones(i)
    nj = numones(j)
    bi = bitstostr(i)
    bj = bitstostr(j)
    print(f"{bi} {bj} {'1' if ni >= nj else '0'} {bi if ni >= nj else bj}")
