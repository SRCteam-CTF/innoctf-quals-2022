# Kazino writeup

Given: (vuln)[vuln] and (libc.so.6)[libccc]

Executable have three functions:
1. to increase win counter if `rand()` returns 0 or to exit program otherwise.  
2. to place `(char)0` at any user defined position
3. to exit program if user inputs `yes` or to print pointer to `puts` if user inputs `no` 

The goal of this task was to increase win counter 10 times using attack on random. We can only nullify any byte so we need to zero [randtbl](https://sourceware.org/git/?p=glibc.git;a=blob;f=stdlib/random.c;h=1ea7eed06cd2433a9187d99c7c0b06f29fef558c;hb=7f2ddf7400bb959897a5fe58f7fc5fbe5e57cfae)to get 0 at `rand` call. We can obtain pointer to `randtbl` using the third function and offset from `puts` to `randtbl`. After that we nullify `randtbl` and call the first function 10 times.

[solution srcipt](kazino.py)

Flag: `Ararat{h5Ck3D_r4Nd0M_345y_F14G_NuLl_00000}`