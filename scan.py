logFile = open("auth.log", "r")
count = 0

with logFile as file:
    lines = file.readlines()

    for line in lines:
        words = line.split()

        if words[5] == "Received" and words[6] == "disconnect":
            print "Key Authentication Fail " + words[8]
        elif words[5] == "Failed" and words[6] == "password":
            print "Password failed for " + "USER: " + words[8] + " IP ADDRESS: " + words[10]  
        count += 1