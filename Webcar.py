#Project Smart car functional control with the web application function 
from flask import Flask,render_template, request #  import flask for the web application control capability 
import pyfirmata # for hardware pins control functionality 
import sys 
import os 
import numpy as np 
import math 
import time 

app = Flask(__name__)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Try connect the hardware  
try:
    print("Serial hardware connect successfully !") 
    hardware = pyfirmata.ArduinoMega("/dev/ttyACM0") #USB serial connection hardware 
    #Setting up the pins GPIO 
    #//////////////////////////////////////////////////////////////////////////////////////
    #Back motor control
    m1 = hardware.get_pin('d:9:p') # using the pwm to control the speed of the motor 
    m2 = hardware.get_pin('d:10:p') 
    #Front motor for turning the whells 
    m3 = hardware.get_pin('d:6:p') 
    m4 = hardware.get_pin('d:11:p')
   
except:
     print("Searching for the second hardware serial ......")
     try: 
          print("Serial hardware connect successfully !")
          hardware  = pyfirmata.ArduinoMega("/dev/ttyACM1")
          #Setting up the pins GPIO 
          #//////////////////////////////////////////////////////////////////////////////////////
          #Back motor control
          m1 = hardware.get_pin('d:9:p') # using the pwm to control the speed of the motor 
          m2 = hardware.get_pin('d:10:p') 
          #Front motor for turning the whells 
          m3 = hardware.get_pin('d:6:p') 
          m4 = hardware.get_pin('d:11:p')
         
     except:
         print("All Serial error now rebooting.....")
         os.system("sudo reboot")  # Serial reboot 
#/////////////////////////////////////////////////////////////////////////////////////
@app.route("/")
def index():
    


    return render_template('index.html')


@app.route("/<deviceName>/<action>") 
def action(deviceName,action):
       if deviceName == 'motor1':   
           actuator = m4
       if deviceName == 'motor2': 
           actuator = m3            
       if deviceName == 'motor3':
           actuator = m1
       if deviceName == 'motor4': 
           actuator = m2
    #...............................................................................
             # turning action 
       if action == 'right':
            actuator.write(1)
            m3.write(0)
            time.sleep(0.5)
            actuator.write(0)
            m3.write(0)
               
       if action == 'left': 
            m4.write(0)
            actuator.write(1)
            time.sleep(0.5)
            m4.write(0)
            actuator.write(0)
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
               # Forward backward
       if action == 'forward': 
            actuator.write(0)
            m2.write(1)
            time.sleep(0.5)
            actuator.write(0)
            m2.write(0)
       if action == 'backward': 
            m1.write(1)
            actuator.write(0)
            time.sleep(0.5)
            m1.write(0)
            actuator.write(0)
       if action == 'rightforward': 
            m4.write(1)
            m3.write(0)
            actuator.write(0)
            m2.write(1)
            
            time.sleep(0.5)
            
            actuator.write(0)
            m2.write(0)
            m4.write(0)
            m3.write(0)
       if action == 'leftforward': 
            m4.write(0)
            m3.write(1)
            actuator.write(0)
            m2.write(1)
            
            time.sleep(0.5)
            
            actuator.write(0)
            m2.write(0)
            m4.write(0)
            m3.write(0)

       if action == 'leftbackward':
            m4.write(0)
            m3.write(1)
            m1.write(1)
            actuator.write(0)
        
            time.sleep(0.5)
        
            m1.write(0)
            actuator.write(0)
            m4.write(0)
            m3.write(0)
       if action == 'rightbackward':
            m4.write(1)
            m3.write(0)
            m1.write(1)
            actuator.write(0)
        
            time.sleep(0.5)

            m1.write(0)
            actuator.write(0)
            m4.write(0)
            m3.write(0)
 

       """
       else: 
           m1.write(0)
           m2.write(0)  
           m4.write(0)
           m3.write(0)
       """     
       return render_template('index.html')

if __name__ =="__main__": 

     app.run(debug=True)


