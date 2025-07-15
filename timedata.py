import datetime
import random
import time


while True:
    with open ("data2.txt","a") as f:
        x = datetime.datetime.now()
        rand = random.randint(15,30)
        f.write(x.strftime("%d/%m/%Y %H:%M")+","+str(rand)+"\n")
        print(x.strftime("%d/%m/%Y %H:%M"))
        time.sleep(60)#updates about every minute

