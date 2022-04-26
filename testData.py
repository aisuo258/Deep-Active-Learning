import csv


fpath="D:/work/Project/mozilla/"

with open(fpath+"label_s.csv",'r') as label_s:
    cont=csv.reader(label_s)
    i=0
    for line in cont:
        print(line[0])
        i+=1
        if i>10:
            break