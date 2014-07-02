import serial
import sys
import rabbitpy

QUEUE = 'ardustick'

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=3)
#ser = serial.Serial('COM2', 9600, timeout=3)
init = ser.readline().strip(' \t\n\r')

if init != "READY":
    print "Error in initialization: " + init
    sys.exit(1)

print "Initialized"

with rabbitpy.Connection('amqp://ardustick:ardustick@192.168.0.12:5672/%2f') as conn:
    with conn.channel() as channel:
        queue = rabbitpy.Queue(channel, QUEUE)
        print "Listening on queue: " + QUEUE

        # Exit on CTRL-C
        try:
            # Consume the message
            for message in queue:
                body = message.json()
                message.ack()
                command = "^%d,%d,%d$" % (
                    body['remote'],
                    body['device'],
                    body['status']
                )

                print "Sending:", command
                ser.write(command)
                ser.flush()
                result = ser.readline().strip(' \t\n\r')
                print "Response:", result

        except KeyboardInterrupt:
            print 'Exited consumer'

ser.close()
