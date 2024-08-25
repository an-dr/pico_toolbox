# https://www.tomshardware.com/how-to/raspberry-pi-pico-joystick

from machine import Pin, ADC
import stepper
import utime

xAxis = ADC(Pin(27))
yAxis = ADC(Pin(26))
button = Pin(16,Pin.IN, Pin.PULL_UP)

# Define the stepper motor pins
IN1 = 21
IN2 = 20
IN3 = 19
IN4 = 18

# Initialize the stepper motor
stepper_motor = stepper.HalfStepMotor.frompins(IN1, IN2, IN3, IN4)

# Set the current position as position 0
stepper_motor.reset()


while True:
    xValue = xAxis.read_u16()
    yValue = yAxis.read_u16()
    buttonValue = button.value()
    # xStatus = "middle"
    # yStatus = "middle"
    # buttonStatus = "not pressed"
    if xValue <= 600:
        # xStatus = "left"
        print("Moving left")
        stepper_motor.step(-100)
    elif xValue >= 60000:
        # xStatus = "right"
        print("Moving right")
        stepper_motor.step(100)
    if yValue <= 600:
        # yStatus = "up"
        print("Moving up")
    elif yValue >= 60000:
        # yStatus = "down"
        print("Moving down")
    if buttonValue == 0:
        # buttonStatus = "pressed"
        print("Button pressed")
        stepper_motor.reset()
            
    # print("X: " + xStatus + ", Y: " + yStatus + " -- button " + buttonStatus)
    # utime.sleep(0.1)
