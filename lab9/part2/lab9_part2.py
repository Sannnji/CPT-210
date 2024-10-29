# Make the tkinter library available for use, and create an alias TK
import tkinter as TK
import RPi.GPIO as GPIO
import os

# GPIO number based on BCM GPIO numbering scheme
SERVO 	                = 18

SERVO_DELAY_SEC         = 0.5		# sec
PWM_FREQUENCY           = 50 		# hz

START_DUTY_CYCLE        = 100	    # percentage
STOP_DUTY_CYCLE         = 0	    	# percentage

# Define the size of the window and position, note that these are strings
WINDOW_SIZE             = "425x175"
X_OFFSET                = "+100" 
Y_OFFSET                = "+100"
WINDOW_OFFSET           = X_OFFSET + Y_OFFSET
WINDOW_GEOMETRY         = WINDOW_SIZE + WINDOW_OFFSET

if os.environ.get('DISPLAY','') == '':
	print('no display found. Using :0.0')
	os.environ.__setitem__('DISPLAY', ':0.0')

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
    GPIO.setup(SERVO, GPIO.OUT,)
    
    # set PWM frequency
    servo_pwm = GPIO.PWM(SERVO, PWM_FREQUENCY)

    return (servo_pwm)

#------------------------------------------------------------------------------
# DESCRIPTION
#   This function creates the GUI to control the motor
#
# INPUT PARAMETERS:
#   none
#
# OUTPUT PARAMETERS:
#   none
#
# RETURN:
#   none
#
#------------------------------------------------------------------------------
def create_gui(servo_pwm):
	global window 
	
	# Create the main window for the GUI control application
	# The variable window is a handle to the instance we can use to access the window
	window = TK.Tk()
	
	window.servo_pwm = servo_pwm

	# Use the title method to give the window a lab
	window.title("Lab 8: DC Motor Controller")

	# Create a frame in our window that holds the instructions	
	frame0 = TK.Frame(window)
	frame1 = TK.Frame(window)

	# Have tkinter pack the frame into the window and place it at the top
	frame0.pack(side=TK.TOP)
	frame1.pack(side=TK.BOTTOM)

	# Add directions to the frame assuming a simple 2x2 grid
	TK.Label(frame0, text="Directions: Move slider around to adjust the speed of the motor").grid(row=0, column=0)
	TK.Label(frame0, text="0 = fully off;   100 = fully on").grid(row=2, column=0)

	# Add labels for the frame
	TK.Label(frame1, text="Speed").grid(row=0, column=0)

	# Create a slider instance for the motor speed
	scale_motor = TK.Scale(frame1, from_=START_DUTY_CYCLE, to=STOP_DUTY_CYCLE, orient=TK.HORIZONTAL) # , command=update_motor_speed)
	scale_motor.grid(row=0, column=1)

	# Set the side and position for the window
	window.geometry(WINDOW_GEOMETRY)

	window.protocol("WM_DELETE_WINDOW", on_close)
	
	# Activate the window
	window.mainloop()
	
def on_close():
	window.destroy()
	
def main():
	try: 
		servo_pwm = setup_gpio()
		
		# motor_pwm.start(START_DUTY_CYCLE)

		create_gui(servo_pwm)
	except KeyboardInterrupt:
		pass
	finally:
		servo_pwm.stop()
		GPIO.cleanup()
		print("GPIO port have been cleaned up")
		
	
if __name__ == '__main__':
	main()
