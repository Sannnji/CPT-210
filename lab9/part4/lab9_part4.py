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
	TK.Label(frame0, text="Enter an angle to adjust the servo motor").grid(row=0, column=1)
	TK.Label(frame0, text="Fully CCW = -90  |  Fully CW = 90").grid(row=1, column=1)

	# Add labels for the frame
	TK.Label(frame1, text="Enter an angle:").grid(row=0, column=0)

	# Create a text field instance for the Servo Motor and set its angle
	window.angle_text_field = TK.Entry(frame1)
	window.angle_text_field.grid(row=0, column=1)
	
	# Button to apply the angle entered in the text field 
	apply_button = TK.Button(frame1, text="Apply", command=update_angle)
	apply_button.grid(row=1, column=0)

	# Button to quit the GUI and program
	quit_button = TK.Button(frame1, text="Quit", command=on_close)
	quit_button.grid(row=1, column=1)

	# Set the side and position for the window
	window.geometry(WINDOW_GEOMETRY)

	# Activate the window
	window.mainloop()

#------------------------------------------------------------------------------
# DESCRIPTION
#   This function creates a button handler that calculates the duty cycle from
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
def update_angle():
	try:
		t_field_val = int(window.angle_text_field.get())
		
		if (t_field_val >= -90 and t_field_val <= 90):
			seconds_per_pulse = MIN_SEC_PER_PULSE + ((float(t_field_val) + DEG_MAPPING_FACTOR) * SECONDS_PER_DEGREE)
			duty_cycle = (seconds_per_pulse * 1E6)
			servo_pwm.set_servo_pulsewidth(SERVO_PWM_PIN, duty_cycle)
		else:
			print("Please enter a number between -90 - 90.")
	except:
		print("Please enter a valid number!")
		print()

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