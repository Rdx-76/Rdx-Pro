import os,platform
os.system('git pull')
 
Rdx=platform.architecture()[0]
if Rdx=="32bit":
    print('Sorry 32 Bit Not Supported...')
elif Rdx=="64bit":
    #print('Command is in update wait we will fix it soon !')
    __import__("Rdx")