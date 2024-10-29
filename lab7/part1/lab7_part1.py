import RPi.GPIO as GPIO
import time

#------------------------------------------------------------------------------
#                       Constants to be used in program
#------------------------------------------------------------------------------
# GPIO number based on BCM GPIO numbering scheme
LED_OUTPUT = 18

START_DUTY_CYCLE = 0		# percentage
STOP_DUTY_CYCLE = 100		# percentage
DUTY_CYCLE_DELAY = 0.01		# sec
TURNAROUND_TIME = 0.5		# sec
PWM_FREQUENCY = 500 		# hz

# define logic state to control LED (source current)
LED_OFF = GPIO.LOW
LED_ON  = GPIO.HIGH

INC_RATE =  1
DEC_RATE = -1

#------------------------------------------------------------------------------
# DESCRIPTION
#   This function setup_gpio the GPIO pins using the GPIO library
#
# INPUT PARAMETERS:
#   none
#
# OUTPUT PARAMETERS:
#   none
#
# RETURN:
#   Handle or instance of the PWM object
#------------------------------------------------------------------------------
def setup_gpio():
    # global pwm_handle
    
    # use BCM GPIO numbering scheme
    GPIO.setmode(GPIO.BCM)
    
    #set LED pin to OUTPUT mode
    GPIO.setup(LED_OUTPUT, GPIO.OUT, initial=LED_OFF)
    
    #set PWM Frequency to 500hz
    pwm_handle = GPIO.PWM(LED_OUTPUT, PWM_FREQUENCY)
    
    return (pwm_handle)

#------------------------------------------------------------------------------
# DESCRIPTION
#	This function represent the main loop that ramps the duty cycle of the 
#	PWM from 0 to 100. After each change in the duty cycle, a delay is 
#	issued. Once the duty cycle reaches it maximum value, we enter another
#	loop to ramp the duty cycle back down to 0
#
#	Between each ramping loop, we have a delay before turning the ramp around
#
# INPUT PARAMETERS:
#   pwm_handle - the instance of the PWM
#
# OUTPUT PARAMETERS:
#   none
#
# RETURN:
#   none
#------------------------------------------------------------------------------
def loop(pwm_handle):
    while True:
        # loop for making LED brighter
        print("Making LED brighter")
        for duty_cycle in range(START_DUTY_CYCLE, STOP_DUTY_CYCLE+1, INC_RATE):
            pwm_handle.ChangeDutyCycle(duty_cycle)
            time.sleep(DUTY_CYCLE_DELAY)
            
        time.sleep(TURNAROUND_TIME)
        
        # loop for making LED darker
        print("Making LED darker")
        for duty_cycle in range(STOP_DUTY_CYCLE, START_DUTY_CYCLE, DEC_RATE):
            pwm_handle.ChangeDutyCycle(duty_cycle)
            time.sleep(DUTY_CYCLE_DELAY)
        
        time.sleep(TURNAROUND_TIME)

def main():
	#--------------------------------------------------------------------------
    #                   Variables to be used in main 
    #--------------------------------------------------------------------------
    pwm_handle = 0
    
    print()
    print("********************** PROGRAM IS RUNNING **********************")
    print()
    print("Press CNTRL-c to end the program")
    print()
    
    try:
        # get a handle to the pwm
        pwm_handle = setup_gpio()
        
        # set the initial duty cycle
        pwm_handle.start(START_DUTY_CYCLE)
        
        loop(pwm_handle)
        
    except KeyboardInterrupt:
        print()
        print("CTRL-c detected")
        
    finally:
        pwm_handle.stop()
        GPIO.cleanup()
        print("GPIO Port have been cleaned up")
        print()
        print("********************** PROGRAM TERMINATED **********************")
        print()
       
if __name__ == '__main__':
	main()
