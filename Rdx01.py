import os,platform
os.system('git pull')
 
Rdx=platform.architecture()[0]
if Rdx=="32bit":
    print('Sorry 32 Bit Not Supported...')
elif Rdx=="64bit":

    __import__("Rdx")
