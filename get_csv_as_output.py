# importing module 
import csv
# csv file
filename='./data/combined.csv'
openfilename='combined_wo_emptyEnd.csv'
# opening the file using "with"
# statement
hitList = [[] for _ in range(120746)]
count = 0
i = 0
with open(filename,'r', encoding='UTF8') as data:
   for line in csv.reader(data):
       hitList[i]=line
       i+=1
with open(openfilename, 'w', encoding='UTF8') as f:
    for eachHit in hitList[:-1]:
        for eachData in eachHit[:-3]:
            f.write(eachData+',')
        f.write(eachHit[-3]+'\n')
    for eachData2 in hitList[-1][:-3]:
        f.write(eachData2+',')
    f.write(hitList[-1][-3])