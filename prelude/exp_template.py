from pwn import *
import uuid

binary = "{binary}"
dbg_script = '''
'''


def pwn_remote(ip, port, *args, **kargs):
    '''pwn remote gamebox [ip]:[port], return flag and io'''
    p = remote(ip, port)


    '''put payload in it'''


    spliter = str(uuid.uuid1())
    command = "cat /flag"
    command_warpper = '\necho {} ; {} ; echo {}\n'.format(
        spliter, command, spliter)
    p.send(command_warpper)
    p.recvuntil(spliter + '\n')
    flag = p.recvuntil(spliter, drop=True)

    if not kargs.get('keep_alive'):
        p.close()

    return flag, p

if __name__ == '__main__':
    pass
