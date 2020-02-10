with open("auth.log", "r") as f:
    data = f.readlines()
    count = 1
    for line in data:
        print(count , " " , line)
        count += 1

