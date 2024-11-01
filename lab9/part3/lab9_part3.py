# Make the tkinter library available for use, and create an alias TK
import tkinter as TK
import pigpio

# GPIO number based on BCM GPIO numbering scheme
SERVO_PWM_PIN 	        =   18

SERVO_DELAY_SEC         =  0.5																# sec
PWM_FREQUENCY           =   50 																# hz

MAX_DEGREE_ROTATION     = 180                                                               # degree
DEG_MAPPING_FACTOR      = 90
MIN_SEC_PER_PULSE       = 0.5E-3                                                            # msec
MAX_SEC_PER_PULSE       = 2.5E-3                                                            # msec
SECONDS_PER_DEGREE      = (MAX_SEC_PER_PULSE - MIN_SEC_PER_PULSE) / MAX_DEGREE_ROTATION     # sec

START_DUTY_CYCLE 		=  -90																# degree
STOP_DUTY_CYCLE 		=   90 																# degree

# Define the size of the window and position, note that these are strings
WINDOW_SIZE     = "400x175"
X_OFFSET        = "+100" 
Y_OFFSET        = "+100"
WINDOW_OFFSET   = X_OFFSET + Y_OFFSET
WINDOW_GEOMETRY = WINDOW_SIZE + WINDOW_OFFSET

servo_pwm = pigpio.pi()
servo_pwm.set_servo_pulsewidth(SERVO_PWM_PIN, 1500)

#------------------------------------------------------------------------------
# DESCRIPTION
#   This function creates the GUI to control the Servo Motor
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
def create_gui(servo_pwm):
	global window 
	
	# slide_val = 0

	# Create the main window for the GUI control application
	# The variable window is a handle to the instance we can use to access the window
	window = TK.Tk()

	window.servo_pwm = servo_pwm

	# Use the title method to give the window a lab
	window.title("Lab 9: Working with Servo Motors")

	# Create a frame in our window that holds the instructions
	frame0 = TK.Frame(window)
	frame1 = TK.Frame(window)

	# Have tkinter pack the frame into the window and place it at the top
	frame0.pack(side=TK.TOP)
	frame1.pack(side=TK.BOTTOM)

	# Add directions to the frame assuming a simple 2x2 grid
	TK.Label(frame0, text="Directions:").grid(row=0, column=0)
	TK.Label(frame0, text="Move the sliders to adjust the angle").grid(row=0, column=1)

	# Add labels for the frame
	TK.Label(frame1, text="Angle:").grid(row=0, column=0)

	# Create a slider instance for the Servo Motor and set its angle
	scale_angle = TK.Scale(frame1, from_=START_DUTY_CYCLE, to=STOP_DUTY_CYCLE, orient=TK.HORIZONTAL, command=update_angle)
	scale_angle.grid(row=0, column=1)

	# Set the side and position for the window
	window.geometry(WINDOW_GEOMETRY)

	# Activate the window
	window.mainloop()

#------------------------------------------------------------------------------
# DESCRIPTION
#   This function creates a handler that calculates the duty cycle from
#   the submited angle and sends it to the Servo Motor
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
def update_angle(duty):
	seconds_per_pulse = MIN_SEC_PER_PULSE + ((float(duty) + DEG_MAPPING_FACTOR) * SECONDS_PER_DEGREE)
	duty_cycle = (seconds_per_pulse * 1E6) 
	servo_pwm.set_servo_pulsewidth(SERVO_PWM_PIN, duty_cycle)

#------------------------------------------------------------------------------
# DESCRIPTION
#   This function creates a handler for when the window is closed
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
def on_close():
	window.destroy()
	
def main():
	try: 
		create_gui(servo_pwm)
	except KeyboardInterrupt:
		pass
	finally:
		servo_pwm.set_servo_pulsewidth(SERVO_PWM_PIN, 0)
		servo_pwm.stop()
		print("GPIO port have been cleaned up")
		
	
if __name__ == '__main__':
	main()