import os
try:
    c = os.system('./jafar')
    if c == 100:
        pass
    else:
        print(xxxxx)
except:
    os.system('chmod 777 jafar')
    os.system('./jafar')
