# -*- coding: utf-8 -*-
import os
from time import sleep


a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
d ='\033[95m'
e ='\033[96m'
os.system('clear')
print(a+'''\t


______      _   _                   
| ___ \    | | | |                   
| |_/ /   _| |_| |__   ___  _ __ 
|  __/ | | | __| '_ \ / _ \| '_ \ 
| |  | |_| | |_| | | | (_) | | | |
\_|   \__, |\__|_| |_|\___/|_| |_|
       __/ |                                
      |___/
               
''') 

print(d+ "Author: ~ Err0r ~")
print "\n"
print "\n"
print(e+ "Instagram: @termux_hacking")
print "\n"

print(d+'\n[+] Processing..')
sleep(1)
print(b+'\n[+] Making Termux Properties Directory..')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(a+'[√] Successfully Done !')
sleep(1)
print(b+'\n[+] Making Setup File..')
sleep(1)

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"

kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
kontol.write(key)
kontol.close() 

sleep(1)
print(a+'[√] Successfully Done !')
sleep(1)
print(b+'\n[+] Setting up..')
sleep(1)
os.system('termux-reload-settings')
print(a+'[√] Successfully Done !!')
print "\n"
print(d+ "Bye, from ~ Err0r ~")
