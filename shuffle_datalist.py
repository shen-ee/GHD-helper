import random
import datetime

homepath = "/Users/shenyi/Documents/GitHub/ghds/"
infiles = ["117_list.txt","119_list.txt","120_list.txt"]

trainrate = 0.9

now_time = datetime.datetime.now().strftime('%Y-%m-%d-%H')

list = []
for infile in infiles:
    with open(homepath+infile,"r") as input:
        for line in input:
            list.append(line.strip())

random.shuffle(list)
number_train = int(len(list)*trainrate)
list_train = list[:number_train]
list_test = list[number_train:]

with open("./"+now_time+"train.txt","w") as outfile_train:
    [outfile_train.write(i+"\n") for i in list_train]

with open("./"+now_time+"test.txt","w") as outfile_test:
    [outfile_test.write(i+"\n") for i in list_test]

