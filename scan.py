#Imports
import os

#global variable needed
iplist = {}

#Functions needed
def ipInsert(ip):
    if iplist.has_key(ip):
        iplist[ip] += 1
    else:
        iplist[ip] = 1


#Open log file. Path to log file here (may add copy to program directory later)
logFile = open("auth.log", "r")
count = 0

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
       os.system(command)

    

