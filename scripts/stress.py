import serial
import sys

ser = serial.Serial('COM2', 9600, timeout=3)
init = ser.readline().strip(' \t\n\r')

if init != "READY":
    print "Error in initialization: " + init
    sys.exit(1)

print "Initialized"

messages = ['^11315342,0,1$',
            '^11315342,1,1$',
            '^11315342,2,1$']

while True:
    for message in messages:
        print "Sending: " + message.strip(' \t\n\r')
        ser.write(message)
        #ser.flush()
        resp = ser.readline().strip(' \t\n\r')
        print "Response: " + resp

        if message.strip(' \t\n\r^$') != resp:
            print "---------------------- ERROR ----------------------"
