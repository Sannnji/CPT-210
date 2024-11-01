import pigpio 
import time

#------------------------------------------------------------------------------
#                       Constants to be used in program
#------------------------------------------------------------------------------
# GPIO number based on BCM GPIO numbering scheme
SERVO_PWM_PIN 	        = 18

MAX_DEGREE_ROTATION     = 180                                                               # degree
DEG_MAPPING_FACTOR      = 90
MIN_SEC_PER_PULSE       = 0.5E-3                                                            # msec
MAX_SEC_PER_PULSE       = 2.5E-3                                                            # msec
SECONDS_PER_DEGREE      = (MAX_SEC_PER_PULSE - MIN_SEC_PER_PULSE) / MAX_DEGREE_ROTATION     # sec

SERVO_DELAY_SEC         = 0.5		                                                        # sec
PWM_FREQUENCY           = 50 		                                                        # hz

DEBUG_ENABLE            = True

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
    servo_pwm = pigpio.pi()
    servo_pwm.set_servo_pulsewidth(SERVO_PWM_PIN, 1500)
    
    return (servo_pwm)

#------------------------------------------------------------------------------
# DESCRIPTION
#	This function represent the main loop that allows the continous control 
#   over the Servo Motor.
#
# INPUT PARAMETERS:
#   servo_pwm - the instance of the Servo PWM
#
# OUTPUT PARAMETERS:
#   none
#
# RETURN:
#   none
#------------------------------------------------------------------------------
def loop(servo_pwm):
    continue_looping = True
    
    while (continue_looping):
        input_angle = get_user_choice()

        seconds_per_pulse = MIN_SEC_PER_PULSE + ((input_angle + DEG_MAPPING_FACTOR) * SECONDS_PER_DEGREE)
        
        duty_cycle = (seconds_per_pulse * 1E6) 
        
        if (DEBUG_ENABLE):
            print()
            print("*** DEBUG ENABLED ****")
            print(f"  Angle adjustment = {DEG_MAPPING_FACTOR}")
            print(f"SECONDS_PER_DEGREE = {SECONDS_PER_DEGREE:.3e}")
            print(f"     Angle entered = {input_angle:.3f}")
            print(f" Seconds_per_pulse = {seconds_per_pulse:.3e}")
            print(f"        Duty Cycle = {duty_cycle:.3f}")

        servo_pwm.set_servo_pulsewidth(SERVO_PWM_PIN, duty_cycle)
        time.sleep(SERVO_DELAY_SEC)

#------------------------------------------------------------------------------
# DESCRIPTION
#	This function handles user input through the console and checks for a valid
#   input to return
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
def get_user_choice():
    valid = False
    while (not valid):
        try:
            angle = float(input("Rotation Angle: "))
            if (angle > 90 or angle < -90):
                print("Please enter a number between -90 - 90.")
            valid = True

        except:
            print("Please enter a valid number!")
            print()
    return angle

#------------------------------------------------------------------------------
# DESCRIPTION
#	This function cleans up the GPIO ports and stops the Servo Motor PWM
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
def destroy(servo_pwm):
    servo_pwm.set_servo_pulsewidth(SERVO_PWM_PIN, 0)
    servo_pwm.stop()

    
def main():
    print()
    print("********************** PROGRAM IS RUNNING **********************")
    print()
    print("Press CTRL-C to end the program")
    print()

    try:
        servo_pwm = setup_gpio()
        loop(servo_pwm)

    except KeyboardInterrupt:
        print()
        print("CTRL-C detected")
        
    finally:
        destroy(servo_pwm)
        print("GPIO ports have been cleaned up")
        print()
        print("********************** PROGRAM TERMINATED **********************")
        print()
       
if __name__ == '__main__':
    main()
