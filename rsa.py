import numpy as np


def enc(m, e, N):
    return pow(m, e, N)


def dec(c, d, N):
    return pow(c, d, N)


def trial_division(N: int) -> list[int]:
    a = []
    while N % 2 == 0:
        a.append(2)
        N //= 2
    f = 3
    while f * f <= N:
        if N % f == 0:
            a.append(f)
            N //= f
        else:
            f += 2
    if N != 1: a.append(N)
    return a


if __name__ == '__main__':
    print(dec(c=17, d=2321638369, N=4294967317))
    print(enc(m=1372559486, e=65537, N=4294967317))
    print(trial_division(4294967317))
    print(dec(c=17**2, d=2321638369, N=4294967317))