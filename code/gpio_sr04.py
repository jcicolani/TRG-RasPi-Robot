# GPIO example using an NC-SR04 ultrasonic range finder

# import the GPIO and time libraries
import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM mode and disable warnings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define pins
trig = 20
echo = 21

GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)

print("Distance measurement in progress")

# Begin while loop
while True:
    # Set trigger pin low got 1/10 second
    GPIO.output(trig,False)
    time.sleep(0.1)

    # Send a 10uS pulse
    GPIO.output(trig,True)
    time.sleep(0.00001)
    GPIO.output(trig,False)
    print("ping")

    # Get the start and end times of the return pulse
    while GPIO.input(echo)==0:
        pulse_start = time.time()
        print("pulse start: " + str(pulse_start), end = "\r")

    while GPIO.input(echo)==1:
        pulse_end = time.time()
        print("pulse end: " + str(pulse_end), end = "\r")

    pulse_duration = pulse_end - pulse_start
    print("duration: " + str(pulse_duration))

    # Calculate the distance in centimeters
    distance = pulse_duration * 17150
    distance = round(distance, 2)

    # Display the results. end = '\r' forces the output to the same line
    print("Distance: " + str(distance) + "cm      ", end = '\r')
