from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from text_on_LCD import LCD
from time import sleep

recentStatus = "unknown"
app = Flask(__name__)

try:
    print ('Display will be starting ... ')
    myLcd = LCD()
    print ('Display should be ON ... ')
except:
    print("Could not init LCD!")

@app.route('/status/<string:status>')
def status_message(status):
    global recentStatus
    print ("Status: " + status)
    if status.startswith("busy") and recentStatus != "busy":
        recentStatus = "busy"
        myLcd.setLoop(False)
        sleep(2)
        myLcd.setLoop(True)
        myLcd.busy()
    elif status == "offline" and recentStatus != "offline":
        recentStatus = "offline"
        myLcd.setLoop(False)
        sleep(2)
        myLcd.destroy()
        myLcd.setLoop(True)
    elif status == "presenting_act" and recentStatus != "presenting_act":
        recentStatus = "presenting_act"
        myLcd.setLoop(False)
        sleep(2)
        myLcd.setLoop(True)
        myLcd.presenting()
    elif status.startswith("dnd") and recentStatus != "dnd":
        recentStatus = "dnd"
        myLcd.setLoop(False)
        sleep(2)
        myLcd.setLoop(True)
        myLcd.dnd()
    elif status.startswith("inacall") and recentStatus != "inacall":
        recentStatus = "inacall"
        myLcd.setLoop(False)
        sleep(2)
        myLcd.setLoop(True)
        myLcd.inAcall()
    elif status.startswith("available") and recentStatus != "available":
        recentStatus = "available"
        myLcd.setLoop(False)
        sleep(2)
        myLcd.setLoop(True)
        myLcd.available()
    elif status.startswith("away") and recentStatus != "away":
        recentStatus = "away"
        myLcd.setLoop(False)
        sleep(2)
        myLcd.setLoop(True)
        myLcd.away()    
    elif status.startswith("brb") and recentStatus != "brb":
        recentStatus = "brb"
        myLcd.setLoop(False)
        sleep(2)
        myLcd.setLoop(True)
        myLcd.brb()        
    #return render_template('index.html', value = status)
    return "200 OK"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)