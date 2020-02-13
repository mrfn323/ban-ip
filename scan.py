#Imports
import os

#global variable needed
iplist = {}                                             #Holds ip address seen in the log files and counts how many times it appears
existingIPs = []                                        #Takes ufw rules ip address to be compared to later. 

#Functions needed
def ipInsert(ip):
    if ip in existingIPs != True:
        if iplist.has_key(ip):
            iplist[ip] += 1
        else:
            iplist[ip] = 1

#commands being done on the machine to get and create necessary files.
os.system("cp /var/log/auth.log ~/ban-ip")             #Copies Auth.log file to get ips that needs to be banned
os.system("ufw status | grep DENY >> denyrules")       #Copies ufw status to a file that scan ips that have already been banned

#Opens files. Needed for the program
logFile = open("auth.log", "r")                         #Opens auth.log file that was copied from the system location
existingIP = open("denyrules", "r")                     #Opens ufw rules file
count = 0

#Populate existingIPs array
with existingIP as ipFile:
    lines = ipFile.readlines()
    print(lines)

    for line in lines:
        words = line.split()
        existingIPs.append(words[2])

#Run through each line in the log file
with logFile as file:
    lines = file.readlines()

    #Spliting each line to a word list
    for line in lines:
        words = line.split()

        #Failed Key
        if words[5] == "Received" and words[6] == "disconnect":
            print("{}: Key Authentication Fail IP ADDRESS: " + words[8]).format(count)
            ip = words[8]
            ipInsert(ip)           

        #Failed Password logic
        elif words[5] == "Failed" and words[6] == "password":
            #failed password with invalid user
            if words[8] == "invalid":
                print("{}: Failed password for Invalid user USER: " + words[10] + " IP ADDRESS: " + words[12]).format(count)
                ip = words[12]
                ipInsert(ip)
            #just failed password
            else:
                print("{}: Password failed for " + "USER: " + words[8] + " IP ADDRESS: " + words[10]).format(count)
                ip = words[10]
                ipInsert(ip)
            
        count += 1

for key in iplist:
    if iplist.get(key) > 3:
       command = ("ufw deny from {}").format(key)
       print(command)

os.system("rm denyrules")

    

