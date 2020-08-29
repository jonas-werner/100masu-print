#!/usr/bin/python

from time import sleep
from gpiozero import LED
import subprocess 
import requests

def GetPDF(filenumber):
    url = 'http://dailywork.net/work/' + filenumber + '.pdf'
    print url
    r = requests.get(url)

    with open('/tmp/100masu.pdf', 'wb') as f:
        f.write(r.content)


def ConvertToImage():
    p = subprocess.Popen(["pdftoppm", "-jpeg", "/tmp/100masu.pdf", "/tmp/jpegFile"])


def PrintImage():
    p = subprocess.Popen(["lp", "-d", "Jonamiki-printer", "/tmp/jpegFile-1.jpg"])


def powerOffPi():
    p = subprocess.Popen(["sudo", "shutdown", "-h", "now"])


def PrinterPowerControl():
    sleep(2)
    led = LED(17)
    led.on()
    sleep(0.5)
    led.off()

    # Give printer time to initialize
    sleep(20)


### Main
#################################


PrinterPowerControl()

#filenumbers = ["91050", "91060", "91070", "91080", "91040"]
filenumbers = ["91040"]

for filenumber in filenumbers:
    output = GetPDF(filenumber)
    sleep(5)
    ConvertToImage()
    sleep(5)
    PrintImage()
    sleep(20)


sleep(100)
PrinterPowerControl()
powerOffPi()
