#!/usr/bin/env python 3

def commandpush(devicecmd):
    
    for ip in devicecmd.keys():
        print(f'Handshaking. .. ... connecting with {ip}')
        for mycmds in devicecmd[ip]:
            print(f'Attmpting to send command --> {mycmds}')

    return None

def main():
    
    devicecmd = {'10.0.0.1":["interface eth1/2', 'no shutdown'], 
