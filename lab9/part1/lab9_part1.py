import RPi.GPIO as GPIO
import time
from ADCDevice import *

#------------------------------------------------------------------------------
#                       Constants to be used in program
#------------------------------------------------------------------------------
# GPIO number based on BCM GPIO numbering scheme
SERVO 	                = 18

MAX_DEGREE_ROTATION     = 90                                                                # degree
MIN_SEC_PER_PULSE       = 0.5                                                               # sec
MAX_SEC_PER_PULSE       = 2.5                                                               # sec
SECONDS_PER_DEGREE      = (MAX_SEC_PER_PULSE - MIN_SEC_PER_PULSE) / MAX_DEGREE_ROTATION     # sec

# START_DUTY_CYCLE        = 100	    # percentage
# STOP_DUTY_CYCLE         = 0	    # percentage

SERVO_DELAY_SEC         = 0.5		                                                        # sec
PWM_FREQUENCY           = 50 		                                                        # hz

# define logic state to control LED (source current)
MOTOR_OFF = GPIO.LOW
MOTOR_ON  = GPIO.HIGH

DEBUG_ENABLE = False

#------------------------------------------------------------------------------
# DESCRIPTION
#   This function sets up the GPIO pins using the GPIO library
#
# INPUT PARAMETERS:
#   none
#
# OUTPUT PARAMETERS:
#   none
#
# RETURN:
#   instance of the PWM object
#------------------------------------------------------------------------------
def setup_gpio():
    # use BCM GPIO numbering scheme
    GPIO.setmode(GPIO.BCM)

    # set LED pin to OUTPUT mode
    GPIO.setup(SERVO, GPIO.OUT)
    
    # set PWM frequency
    servo = GPIO.PWM(SERVO, PWM_FREQUENCY)

    return (servo)

#------------------------------------------------------------------------------
# DESCRIPTION
#	This function represent the main loop that allows the continous control 
#   over the Micro Servo Motor.
#
# INPUT PARAMETERS:
#   motor_enable - the instance of the motor PWM
#
# OUTPUT PARAMETERS:
#   none
#
# RETURN:
#   none
#------------------------------------------------------------------------------
def loop(servo):
    continue_looping = True
    
    while (continue_looping):
        input_angle = get_user_choice()

        seconds_per_pulse = MIN_SEC_PER_PULSE + ((input_angle + MAX_DEGREE_ROTATION) * SECONDS_PER_DEGREE)
        
        duty_cycle = (seconds_per_pulse * PWM_FREQUENCY) * 100

        print(f"Angle: {angle}")
        servo(angle)
        
        time.sleep(SERVO_DELAY_SEC)
            

def get_user_choice():
    valid = False
    while (not valid):
        try:
            angle = float(input("Rotation Angle: "))
            valid = True
        except ValueError:
            print("Please enter a number.")
            print()
    return angle

#------------------------------------------------------------------------------
# DESCRIPTION
#	This function cleans up the GPIO ports and ADC
#
# INPUT PARAMETERS:
#   none
#
# OUTPUT PARAMETERS:
#   none
#
# RETURN:
#   none
#------------------------------------------------------------------------------
def destroy(servo):
    GPIO.cleanup()
    servo.stop()

    
def main():
    print()
    print("********************** PROGRAM IS RUNNING **********************")
    print()
    print("Press CTRL-C to end the program")
    print()

    if (DEBUG_ENABLE):
        print()
        print("*** DEBUG ENABLED ****")
        print(f"  Angle adjustment = {DEG_MAPPING_FACTOR}")
        print(f"SECONDS_PER_DEGREE = {SECONDS_PER_DEGREE:.3e}")
        print(f"     Angle entered = {angle_entered:.3f}")
        print(f" Seconds_per_pulse = {seconds_per_pulse:.3e}")
        print(f"        Duty Cycle = {duty_cycle:.3f}")
    
    try:
        servo = setup_gpio()
        # servo.start()
        loop(servo)

    except KeyboardInterrupt:
        print()
        print("CTRL-C detected")
        
    finally:
        destroy(servo)
        print("GPIO ports have been cleaned up")
        print()
        print("********************** PROGRAM TERMINATED **********************")
        print()
       
if __name__ == '__main__':
    main()
