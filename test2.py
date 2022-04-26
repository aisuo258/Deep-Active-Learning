import csv


fpath="D:/work/Project/mozilla/"

with open(fpath+"code_CE.csv",'r') as label_s:
    cont=csv.reader(label_s)
    i=0
    for line in cont:
        print(line)
        i+=1
        if i>1:
            break