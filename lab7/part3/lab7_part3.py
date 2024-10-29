# Make the tkinter library available for use, and create an alias TK
import tkinter as TK
import RPi.GPIO as GPIO

# GPIO number based on BCM GPIO numbering scheme
RED_LED_OUTPUT   = 25
GRN_LED_OUTPUT   = 24
BLU_LED_OUTPUT   = 23
START_DUTY_CYCLE = 0        # percentage
STOP_DUTY_CYCLE  = 100      # percentage
PWM_FREQUENCY    = 500      # Hz

# define logic state to control LED (source current)
LED_OFF 		 = GPIO.HIGH
LED_ON  		 = GPIO.LOW

# Define the size of the window and position, note that these are strings
WINDOW_SIZE      = "400x175"
X_OFFSET         = "+100" 
Y_OFFSET         = "+100"
WINDOW_OFFSET    = X_OFFSET + Y_OFFSET
WINDOW_GEOMETRY  = WINDOW_SIZE + WINDOW_OFFSET

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
#   This function updates the blue channels PWM based on the slider value.
#
# INPUT PARAMETERS:
#   duty - represents the value of the duty cycle from slider as a string
#
# OUTPUT PARAMETERS:
#   none
#
# RETURN:
#   none
#
#------------------------------------------------------------------------------
def create_gui(red_pwm, grn_pwm, blu_pwm):
	global window 
	
	# Create the main window for the GUI control application
	# The variable window is a handle to the instance we can use to access the window
	window = TK.Tk()
	
	window.red_pwm = red_pwm
	window.grn_pwm = grn_pwm
	window.blu_pwm = blu_pwm
	
	# Use the title method to give the window a lab
	window.title("Lab 7: RBG LED Control")

	# Create a frame in our window that holds the instructions	
	frame0 = TK.Frame(window)
	frame1 = TK.Frame(window)

	# Have tkinter pack the frame into the window and place it at the top
	frame0.pack(side=TK.TOP)
	frame1.pack(side=TK.BOTTOM)

	# Add directions to the frame assuming a simple 2x2 grid
	TK.Label(frame0, text="Directions:").grid(row=0, column=0)
	TK.Label(frame0, text="Move the sliders to adjust the colors").grid(row=0, column=1)
	TK.Label(frame0, text="0 = Off, 100 = color fully on").grid(row=2, column=1)

	# Add labels for the frame
	TK.Label(frame1, text="Red").grid(row=0, column=0)
	TK.Label(frame1, text="Green").grid(row=1, column=0)
	TK.Label(frame1, text="Blue").grid(row=2, column=0)

	# Create a slider instance for the red channel and set its position within the frame
	scale_red = TK.Scale(frame1, from_=START_DUTY_CYCLE, to=STOP_DUTY_CYCLE, orient=TK.HORIZONTAL, command=updateRed)
	scale_red.grid(row=0, column=1)

	# Create a slider instance for the green channel and set its position within the frame
	scale_grn = TK.Scale(frame1, from_=START_DUTY_CYCLE, to=STOP_DUTY_CYCLE, orient=TK.HORIZONTAL, command=updateGreen)
	scale_grn.grid(row=1, column=1)

	# Create a slider instance for the blue channel and set its position within the frame
	scale_blu = TK.Scale(frame1, from_=START_DUTY_CYCLE, to=STOP_DUTY_CYCLE, orient=TK.HORIZONTAL, command=updateBlue)
	scale_blu.grid(row=2, column=1)

	# Set the side and position for the window
	window.geometry(WINDOW_GEOMETRY)

	window.protocol("WM_DELETE_WINDOW", on_close)
	
	# Activate the window
	window.mainloop()

def on_close():
	window.destroy()
	
def updateBlue(duty):
	# get the sider value and convert to an integer value
	# we must subtract from the STOP DUTY CYCLE which is 100
	# because 0 duty cycle represents 0 volts which turns the LED on 
	window.blu_pwm.ChangeDutyCycle(STOP_DUTY_CYCLE - int(duty))

def updateRed(duty):
	# get the sider value and convert to an integer value
	# we must subtract from the STOP DUTY CYCLE which is 100
	# because 0 duty cycle represents 0 volts which turns the LED on 
	window.red_pwm.ChangeDutyCycle(STOP_DUTY_CYCLE - int(duty))
	
def updateGreen(duty):
	# get the sider value and convert to an integer value
	# we must subtract from the STOP DUTY CYCLE which is 100
	# because 0 duty cycle represents 0 volts which turns the LED on 
	window.grn_pwm.ChangeDutyCycle(STOP_DUTY_CYCLE - int(duty))

def main():
	try: 
		red_pwm, grn_pwm, blu_pwm = setup_gpio()
		
		red_pwm.start(STOP_DUTY_CYCLE)
		grn_pwm.start(STOP_DUTY_CYCLE)
		blu_pwm.start(STOP_DUTY_CYCLE)
		
		create_gui(red_pwm, grn_pwm, blu_pwm)
	except KeyboardInterrupt:
		pass
	finally:
		red_pwm.stop()
		grn_pwm.stop()
		blu_pwm.stop()
		GPIO.cleanup()
		print("GPIO port have been cleaned up")
		
	
if __name__ == '__main__':
	main()
