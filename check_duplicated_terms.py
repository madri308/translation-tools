import os

f = open("es_CR.po", "r")
words = []
msg = ""
for line in f:
    if line[:6] == "msgid ":
        msg = line[7:-2]
        if msg in words and msg != "":
            print(msg)
        else:
            words.append(msg)
    
f.close()
print("done")
