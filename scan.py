logFile = open("auth.log", "r")
count = 0

with logFile as file:
    lines = file.readlines()

    for line in lines:
        words = line.split()

        #Failed Key
        if words[5] == "Received" and words[6] == "disconnect":
            print("{}: Key Authentication Fail IP ADDRESS: " + words[8]).format(count)

        #Failed Password logic
        elif words[5] == "Failed" and words[6] == "password":
            #failed password with invalid user
            if words[8] == "invalid":
                print("{}: Failed password for Invalid user USER: " + words[10] + " IP ADDRESS: " + words[12]).format(count)
            #just failed password
            else:
                print("{}: Password failed for " + "USER: " + words[8] + " IP ADDRESS: " + words[10]).format(count)
            
        count += 1