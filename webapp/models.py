from flask import Flask
import datetime
#from gpiozero import CPUTemperature   # RPi version
import socket
import platform
import time

class Platform():
    now = datetime.datetime.now()
    timeString = now.strftime("%H:%M %d-%m-%Y ")
    hostName = socket.gethostname()    # Function to display hostname & IP address
    hostIp = socket.gethostbyname(hostName)
    platformType = platform.system()
    #cpuTemp = CPUTemperature()  # To get CPU Temperature
    #CPUTemp = round(cpuTemp.temperature,1)

    def __repr__(self):
        return f"Platform('{self.timeString}', '{self.hostName}', '{self.hostIp}', '{self.platformType}')"


# class Message():
#     def __repr__(self):
#         return f"Platform('{self.msgTitle}', '{self.msgBody}')"
