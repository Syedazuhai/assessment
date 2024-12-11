file = open("textfile.txt", "r")
words = file.readlines()[0].strip().split(",")
print(words)
file.close()
dct = {}
for word in words:
    word = word.strip()
    dct[word] = dct.get(word,0)+1
    print(dct)