import os

f = open("es_CR.po", "r")
words = []
msg = ""
check_next_line = False
line_index = 1
for line in f:
    if line.strip() == "":
        line_index += 1
        check_next_line = True
        continue
    elif check_next_line and line[:9] !=  "#. module":
        print(line_index)
    check_next_line = False
    line_index += 1
    
f.close()
print("done")
