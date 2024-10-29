import RPi.GPIO as GPIO
import time 
import random

#------------------------------------------------------------------------------
#                       Constants to be used in program
#------------------------------------------------------------------------------
# GPIO number based on BCM GPIO numbering scheme
RED_LED_OUTPUT   = 25
GRN_LED_OUTPUT   = 24
BLU_LED_OUTPUT   = 23

START_DUTY_CYCLE = 0        # percentage
STOP_DUTY_CYCLE  = 100      # percentage
DUTY_CYCLE_DELAY = 0.01     # sec
TURNAROUND_TIME  = 0.5      # sec
PWM_FREQUENCY    = 500      # Hz

# define logic state to control LED (sinking current)
LED_OFF          = GPIO.HIGH
LED_ON           = GPIO.LOW

#------------------------------------------------------------------------------
# DESCRIPTION
#   This function setup_gpio the GPIO pins using the GPIO library. It will
#   also create an instance for a PWM for each of the GPIO pins.
#
# INPUT PARAMETERS:
#   none
#
# OUTPUT PARAMETERS:
#   none
#
# RETURN:
#   Handle or instance of the red channel's PWM object
#   Handle or instance of the green channel's PWM object
#   Handle or instance of the blue channel's PWM object
#------------------------------------------------------------------------------
def setup_gpio():
    # use BCM GPIO numbering scheme
    GPIO.setmode(GPIO.BCM)

    # set LED pin to OUTPUT mode
    GPIO.setup(RED_LED_OUTPUT, GPIO.OUT, initial=LED_OFF)
    GPIO.setup(GRN_LED_OUTPUT, GPIO.OUT, initial=LED_OFF)
    GPIO.setup(BLU_LED_OUTPUT, GPIO.OUT, initial=LED_OFF)

    # set PWM frequency to 500Hz
    red_pwm = GPIO.PWM(RED_LED_OUTPUT, PWM_FREQUENCY)
    grn_pwm = GPIO.PWM(GRN_LED_OUTPUT, PWM_FREQUENCY)
    blu_pwm = GPIO.PWM(BLU_LED_OUTPUT, PWM_FREQUENCY)

    return (red_pwm, grn_pwm, blu_pwm)

#------------------------------------------------------------------------------
# DESCRIPTION
#   This function generates a random number of each channel that will be 
#   used to update the duty cycle to the PWM.
#
# INPUT PARAMETERS:
#   Handle or instance of the red channel's PWM object
#   Handle or instance of the green channel's PWM object
#   Handle or instance of the blue channel's PWM object
#
# OUTPUT PARAMETERS:
#   none
#
# RETURN:
#   none
#------------------------------------------------------------------------------
def loop(red_pwm, grn_pwm, blu_pwm):
    #--------------------------------------------------------------------------
    #                   Variables to be used in function 
    #--------------------------------------------------------------------------
    red_duty_cycle = 0 
    grn_duty_cycle = 0
    blu_duty_cycle = 0

    while True:
        # generate a random duty cycle for each channel
        red_duty_cycle = random.randint(START_DUTY_CYCLE, STOP_DUTY_CYCLE)
        grn_duty_cycle = random.randint(START_DUTY_CYCLE, STOP_DUTY_CYCLE)
        blu_duty_cycle = random.randint(START_DUTY_CYCLE, STOP_DUTY_CYCLE)

        # output the duty cycle for each channel for debugging
        print(f"red={red_duty_cycle}; grn={grn_duty_cycle}; blu={blu_duty_cycle}")

        # update the duty cycle for each channel
        red_pwm.ChangeDutyCycle(red_duty_cycle)
        grn_pwm.ChangeDutyCycle(grn_duty_cycle)
        blu_pwm.ChangeDutyCycle(blu_duty_cycle)

        time.sleep(TURNAROUND_TIME)

def main():
    #--------------------------------------------------------------------------
    #                   Variables to be used in function 
    #--------------------------------------------------------------------------
    red_pwm = 0
    grn_pwm = 0
    blu_pwm = 0

    print()
    print("********************** PROGRAM IS RUNNING **********************")
    print()
    print("Press CTRL-c to end the program.")
    print()

    try:
        # get a handle to the pwm
        red_pwm, grn_pwm, blu_pwm = setup_gpio()

        # set the initial duty cycle
        red_pwm.start(START_DUTY_CYCLE)
        grn_pwm.start(START_DUTY_CYCLE)
        blu_pwm.start(START_DUTY_CYCLE)

        loop(red_pwm, grn_pwm, blu_pwm)

    except KeyboardInterrupt:
        print()
        print("CTRL-c detected")
        print()

    finally:
        red_pwm.stop()
        grn_pwm.stop()
        blu_pwm.stop()
        GPIO.cleanup()

        print("GPIO port have been cleaned up")
        print()
        print("********************** PROGRAM IS RUNNING **********************")
        print()

if __name__ == '__main__':
	main()
