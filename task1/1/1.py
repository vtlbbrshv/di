from typing import Dict

filename ='text_1_var_83'
with open(filename) as file:
    lines = file.readlines()

word_stat = dict()


for line in lines:
    row = (line.strip()
           .replace("!", " ")
           .replace(".", " ")
           .replace(",", " ")
           .replace("?", " ")
           .strip())

    words = row.split(" ")

    for word in words:
       if word in word_stat:
           word_stat[word] +=1
       else:
           word_stat[word] = 1

word_stat = (dict(sorted(word_stat.items(), reverse=True, key=lambda item: item[1])))

with open('res.txt','w') as result:
   for key, value in word_stat.items():
       result.write(key + ":" + str(value) + "\n")