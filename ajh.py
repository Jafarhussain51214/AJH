import os
os.system('pkg install pyDes')
os.system('pkg install requests')
os.system('pkg install bs4')
try:
    c = os.system('./jafar')
    if c == 100:
        pass
    else:
        print(xxxxx)
except:
    os.system('chmod 777 jafar')
    os.system('./jafar')
