file = open("file.txt",'r')
lines = file.readlines()
for line in lines:
    for text in line.split(","):
        print("CONTENT: ", text)
file.close()