from flask import render_template, url_for, flash, redirect
from webapp import app
from webapp.models import Platform
#from webapp.models import Message
#import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BCM)

# Dictionary called pins to store the pin number, name, and pin state:
# pins = {
#     20 : {'name' : 'Go Left', 'state' : GPIO.LOW},
#     24 : {'name' : 'coffee maker', 'state' : GPIO.LOW},
#     25 : {'name' : 'lamp', 'state' : GPIO.LOW}
# } 

# # Set each pin as an output and make it low:
# for pin in pins:
#     GPIO.setup(pin, GPIO.OUT)
#     GPIO.output(pin, GPIO.LOW)
# for pin in pins:
#     pins[pin]['state'] = GPIO.input(pin)

@app.route("/")
def index():
# 
#     for pin in pins:
#         pins[pin]['state'] = GPIO.input(pin)
#         try:
#             if GPIO.input(pin) == True:
#                 response = "Pin number ", pin,  " is high!"
#             else:
#                 response = "Pin number ", pin, " is low!"
#         except:
#             response = "There was an error reading pin ", pin,  "."
#
    templateData = {
        'title' : 'Welcome to my World :)',
        'time': Platform.timeString,
        'hostname':Platform.hostName,
        'hostip': Platform.hostIp,
        'platform': Platform.platformType#,
        #'cputemp': Platform.CPUTemp,
	    #'response': response,
	    #'pins': pins
    }

    return render_template('index.html', **templateData)

@app.route("/temp")
def temperature():
    templateData = {
        'title' : 'Temperature',
        'time': Platform.timeString,
        'hostname':Platform.hostName,
        'hostip': Platform.hostIp,
        'platform': Platform.platformType,
        #'cputemp': Platform.CPUTemp,
        #'temp_c': TempHumid.temperature_c,
        #'humidity': TempHumid.humidity
    }

    return render_template('temperature.html', **templateData)


@app.route("/about")
def about():
    templateData = {
        'title' : 'About',
        'time': Platform.timeString,
        'hostname':Platform.hostName,
        'hostip': Platform.hostIp,
        'platform': Platform.platformType,
        #'cputemp': Platform.CPUTemp
    }

    return render_template('about.html', **templateData)

# @app.route("/<changePin>/<action>")
# def action(changePin, action):
#     changePin = int(changePin)   # Convert the pin from the URL into an integer:
#     deviceName = pins[changePin]['name'] # Get the device name for the pin being changed:

#     if action == "on":   # If the action part of the URL is "on," execute the code indented below:
#         GPIO.output(changePin, GPIO.HIGH) # Set the pin high:
#         message = "Turned " + deviceName + " on." # Save the status message to be passed into the template:
#     if action == "off":
#        GPIO.output(changePin, GPIO.LOW)
#        message = "Turned " + deviceName + " off."
#     if action == "toggle":
#        GPIO.output(changePin, not GPIO.input(changePin)) # Read the pin and toggle it:
#        message = "Toggled " + deviceName + "."

#     for pin in pins: # For each pin, read the pin state and store it in the pins dictionary:
#        pins[pin]['state'] = GPIO.input(pin)

#     templateData = {
#        'message' : message,
#        'pins' : pins
#     }

#     return render_template('main.html', **templateData)

#@app.route("/control/<action>")
@app.route("/control")
def control():
    # if action == "forwards":   # If the action part of the URL is "on," execute the code indented below:
    #     # I2C message forwards
    #     message = "Moving " + action # Save the status message to be passed into the template:
    # if action == "backwards":
    #    # I2C message forwards
    message = "My Message "

    templateData = {
        'title' : 'Control',
        'time': Platform.timeString,
        'hostname':Platform.hostName,
        'hostip': Platform.hostIp,
        'platform': Platform.platformType,
        #'cputemp': Platform.CPUTemp,
        'message' : message,
    }

    return render_template('control.html', **templateData)