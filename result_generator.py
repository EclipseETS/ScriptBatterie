#Create result file with random data
from random import randint

file=open('result.txt','w+')
file.read()
for i in range(1,10):
    for _ in range(1,601):
        file.write("salve "+str(i)+":cellule "+str(_)+":intRes "+str(randint(20,80))+":capacite "+str(randint(3200,3501))+"\n")
file.close()
