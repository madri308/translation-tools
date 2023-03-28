from googletrans import Translator, constants #install using pip install googletrans==3.1.0a0
import os

f = open("es_CR.po", "r")
new_file = open("es_CR_translated.po", "w")

translator = Translator()
to_exclude = ["Senior","Intern", "Junior", "Junior+", "Lead", "Manager", "Medium", "N/D", "Padawan Design", "Padawan Development"]
body = ""
msg = ""
for line in f:
    line_to_write = line
    if line[:6] == "msgid ":
        msg = line[7:-2]
    elif line[:6] == "msgstr":
        if line[7:-1] == '""' and msg not in to_exclude: # If there is no tranlsation yet
            try:
                translation = translator.translate(msg, src="en", dest="es").text
                print(('msg:%s translation:%s')%(msg, translation))
            except:
                translation = ""
            line = 'msgstr "'+translation+'"\n'
    body += line
    
new_file.write(body)
new_file.close()
f.close()
print("done")
