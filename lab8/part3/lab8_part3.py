import RPi.GPIO as GPIO
import time
from ADCDevice import *

#------------------------------------------------------------------------------
#                       Constants to be used in program
#------------------------------------------------------------------------------
# GPIO number based on BCM GPIO numbering scheme
MOTOR_ENABLE 	     = 17
MOTOR_PIN1			 = 27
MOTOR_PIN2			 = 22

START_DUTY_CYCLE     = 100	    # percentage
STOP_DUTY_CYCLE      = 0	    # percentage

TIME_BETWEEN_SAMPLES = 0.5		# sec
PWM_FREQUENCY = 1000 			# hz

# define logic state to control LED (source current)
MOTOR_OFF = GPIO.LOW
MOTOR_ON  = GPIO.HIGH

adc = ADCDevice()

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
    GPIO.setup(MOTOR_ENABLE, GPIO.OUT, initial=MOTOR_ON)
    GPIO.setup(MOTOR_PIN1, GPIO.OUT, initial=MOTOR_OFF)
    GPIO.setup(MOTOR_PIN2, GPIO.OUT, initial=MOTOR_OFF)

    # set PWM frequency to 1000Hz
    motor_enable = GPIO.PWM(MOTOR_ENABLE, PWM_FREQUENCY)

    return (motor_enable)

#------------------------------------------------------------------------------
# DESCRIPTION
#   This function assigns the desired ADC module
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
def setup_adc():
    global adc
    
    if (adc.detectI2C(0x48)):
        adc = PCF8591()
    elif (adc.detectI2C(0x4B)):
        adc = ADS7830()
    else:
        print("""No correct I2C addresss found, \n""")
        exit(-1)

#------------------------------------------------------------------------------
# DESCRIPTION
#   This function returns the threshold values for the speed of the motor
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
def mapNUM(value, fromLow, fromHigh, toLow, toHigh):
	return (toHigh - toLow) * (value - fromLow) / (fromHigh - fromLow) + toLow

#------------------------------------------------------------------------------
# DESCRIPTION
#	This function represent the main loop that allows the continous control 
#   over the motor.
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
def loop(motor_enable):
    continue_looping = True
    
    while (continue_looping):
        try:
            value = adc.analogRead(0)
        except OSError:
            print()
            print()
            print("Remote I/O Error. Setting ADC VALUE to 128")
            value = 128
        except Exception as Error:
            print(f"Unexpected error detected {Error}")
            continue_looping = False
        
        print(f"ADC Value: {value}")
        motor_control(value, motor_enable)
        
        time.sleep(TIME_BETWEEN_SAMPLES)
            
#------------------------------------------------------------------------------
# DESCRIPTION
#	This function toggles which motor pin to enable to configure the direction 
#   of the spin and utilizes mapNUM to determin the speed.
#
# INPUT PARAMETERS:
#   motor_enable - the instance of the motor PWM
#   ADC          - the adc value
#
# OUTPUT PARAMETERS:
#   none
#
# RETURN:
#   none
#------------------------------------------------------------------------------
def motor_control(ADC, motor_enable):
    value = ADC - 128
    if (value > 0):
        GPIO.output(MOTOR_PIN1, MOTOR_ON)
        GPIO.output(MOTOR_PIN2, MOTOR_OFF)
        print("Turn Forward")
    elif (value < 0):
        GPIO.output(MOTOR_PIN1, MOTOR_OFF)
        GPIO.output(MOTOR_PIN2, MOTOR_ON)
        print("Turn Backward")
    else:
        GPIO.output(MOTOR_PIN1, MOTOR_OFF)
        GPIO.output(MOTOR_PIN2, MOTOR_OFF)
        print("Motor Stop")
        
    b = mapNUM(abs(value), 0, 128, 0, 100)
    motor_enable.ChangeDutyCycle(b)
    
    print("The PWM duty cycle is %d%%\n"%(abs(value)*100/127))
    
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
def destroy():
    GPIO.cleanup()
    adc.close()
    

def main():
    print()
    print("********************** PROGRAM IS RUNNING **********************")
    print()
    print("Press CNTRL-c to end the program")
    print()
    
    try:
        motor_enable = setup_gpio()
        setup_adc()
        motor_enable.start(START_DUTY_CYCLE)
        loop(motor_enable)

    except KeyboardInterrupt:
        print()
        print("CTRL-c detected")
        
    finally:
        destroy(motor_enable)
        print("GPIO Port have been cleaned up")
        print()
        print("********************** PROGRAM TERMINATED **********************")
        print()
       
if __name__ == '__main__':
    main()

