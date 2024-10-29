# Make the tkinter library available for use, and create an alias TK
import tkinter as TK
import RPi.GPIO as GPIO

# GPIO number based on BCM GPIO numbering scheme
MOTOR_OUTPUT   	 = 18
START_DUTY_CYCLE = 0        # percentage
STOP_DUTY_CYCLE  = 100      # percentage
PWM_FREQUENCY    = 100      # Hz

# define logic state to control LED (source current)
LED_OFF 		 = GPIO.LOW
LED_ON  		 = GPIO.HIGH

# Define the size of the window and position, note that these are strings
WINDOW_SIZE      = "425x175"
X_OFFSET         = "+100" 
Y_OFFSET         = "+100"
WINDOW_OFFSET    = X_OFFSET + Y_OFFSET
WINDOW_GEOMETRY  = WINDOW_SIZE + WINDOW_OFFSET

#------------------------------------------------------------------------------
# DESCRIPTION
#   This function setup_gpio the GPIO pins using the GPIO library. It will
#   also create an instance for a PWM for the GPIO pins.
#
# INPUT PARAMETERS:
#   none
#
# OUTPUT PARAMETERS:
#   none
#
# RETURN:
#------------------------------------------------------------------------------
def setup_gpio():
    # use BCM GPIO numbering scheme
    GPIO.setmode(GPIO.BCM)

    # set LED pin to OUTPUT mode
    GPIO.setup(MOTOR_OUTPUT, GPIO.OUT, initial=LED_ON)

    # set PWM frequency to 500Hz
    motor_pwm = GPIO.PWM(MOTOR_OUTPUT, PWM_FREQUENCY)

    return motor_pwm

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
def create_gui(motor_pwm):
	global window 
	
	# Create the main window for the GUI control application
	# The variable window is a handle to the instance we can use to access the window
	window = TK.Tk()
	
	window.motor_pwm = motor_pwm

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
	scale_motor = TK.Scale(frame1, from_=START_DUTY_CYCLE, to=STOP_DUTY_CYCLE, orient=TK.HORIZONTAL, command=update_motor_speed)
	scale_motor.grid(row=0, column=1)

	# Set the side and position for the window
	window.geometry(WINDOW_GEOMETRY)

	window.protocol("WM_DELETE_WINDOW", on_close)
	
	# Activate the window
	window.mainloop()

def on_close():
	window.destroy()
	
def update_motor_speed(duty):
	window.motor_pwm.ChangeDutyCycle(float(duty))

def main():
	try: 
		motor_pwm = setup_gpio()
		
		motor_pwm.start(START_DUTY_CYCLE)

		create_gui(motor_pwm)
	except KeyboardInterrupt:
		pass
	finally:
		motor_pwm.stop()
		GPIO.cleanup()
		print("GPIO port have been cleaned up")
		
	
if __name__ == '__main__':
	main()
