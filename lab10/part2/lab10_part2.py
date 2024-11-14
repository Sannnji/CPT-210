#! /usr/bin/python3
#------------------------------------------------------------------------------
#----------------------------- Python Source Code -----------------------------
#------------------------------------------------------------------------------
#
#   DESIGNERS: James Ji, Samuel Acquaviva
#   FILE NAME: lab10_part2.py
#   
#   DESCRIPTION: This code uses the Raspberry Pi as a web server in order to 
#   monitor the status of a switch and control 3 different LEDs.
#
#------------------------------------------------------------------------------

# Import Statements
from bottle import route, run
import RPi.GPIO as GPIO

#------------------------------------------------------------------------------
#                       Constants to be used in program
#------------------------------------------------------------------------------
# GPIO number based on BCM GPIO numbering scheme
BUTTON_PIN                  = 18 

RED_LED_PIN 	            = 23 
GRN_LED_PIN 	            = 24
BLU_LED_PIN 	            = 25

LED_INIT_CMD                = 0
LED_UPDATE_CMD              = 1
NUM_OF_LEDS                 = 3
BUTTON_GAP                  = "    "                                                        

LED_PINS                    = [RED_LED_PIN, GRN_LED_PIN, BLU_LED_PIN]
LED_STRINGS                 = ["Red LED", "Green LED", "Blue LED"]
BUTTON_COLOR                = ["Tomato", "Green", "DodgerBlue"]

# Define logic state to control LED (source current)
LED_OFF = GPIO.LOW
LED_ON  = GPIO.HIGH

#------------------------------------------------------------------------------
# DESCRIPTION
#   This function sets up the GPIO pins using the GPIO library
#------------------------------------------------------------------------------
def setup_gpio():
    # Use BCM GPIO numbering scheme
    GPIO.setmode(GPIO.BCM)

    # Set LED pin and Button pin to OUTPUT mode
    GPIO.setup(BUTTON_PIN, GPIO.IN)
    GPIO.setup(RED_LED_PIN, GPIO.OUT)
    GPIO.setup(GRN_LED_PIN, GPIO.OUT)
    GPIO.setup(BLU_LED_PIN, GPIO.OUT)

#------------------------------------------------------------------------------
# DESCRIPTION:
#   This function responds to the web request and builds the HTML reply string. 
#   This function accepts a string representing the LED button number and 
#   returns the HTML string for the web request.
#
# INPUT PARAMETERS:
#   led: String - Represents the LED button number
#
# OUTPUT PARAMETERS:
#   response: HTML String
#
# RETURN:
#   An HTML string for the web request.
#------------------------------------------------------------------------------
@route('/')
@route('/<led>')
def process_request(led="n"):
    #----------------------
    # Local Variables
    #----------------------
    led_num = 0
    response = ""

    # Determine if a button was pressed
    if (led != "n") and (led <str(NUM_OF_LEDS)):
        print()
        print(f"LED button {led} pressed")

        # Convert led button number to an integer
        led_num = int(led)

        # LED_UPDATE_CMD the LED based on the number
        update_leds(LED_UPDATE_CMD, led_num)
    else:
        print()
        print(f"Default call. No LED button pressed")
    
    # Build the HTML string
    response = "<script>"
    response += "function changed(led)"
    response += "{"
    response += "    window.location.href='/' + led"
    response += "}"
    response += "</script>"

    response += '<h1>CPT-210: GPIO Control</h1>'
    response += '<h2>Button=' + switch_status() + '</h2>'
    response += '<input type="button" onClick="changed('+\
                str(NUM_OF_LEDS)+')" value="Read Switch">'
    response += '<h2>LEDS</h2>'
    response += html_for_led(0)
    response += html_for_led(1)
    response += html_for_led(2)

    return response

#------------------------------------------------------------------------------
# DESCRIPTION:
#   This function updates the LEDs and keeps track of each LED’s status 
#   (i.e., on or off). This function accepts and validates two parameters.
#
# INPUT PARAMETERS:
#   command: int - Contains the command to be done to the LED
#       For example, if the command is LED_INIT_CMD, the function 
#       initializes the LEDs and status to off. If the command is 
#       LED_UPDATE_CMD, the function toggles the LED state and updates 
#       the output GPIOs accordingly to represent the updated LED state.
#   led_num: int - Represents the LED which the command will be done to.
#------------------------------------------------------------------------------
def update_leds(command, led_num):
    # This function creates a "static-like" variable to keep track of the
    # current state of the LEDs. If variable has not been initialized then
    # we need to create a list and initialize the LED state to off
    if not hasattr(update_leds, "status"):
        update_leds.status = []
        for idx in range(NUM_OF_LEDS):
            update_leds.status.append(LED_OFF)
    
    if (command == LED_INIT_CMD):
        for idx in range(NUM_OF_LEDS):
            update_leds.status[idx] = LED_OFF
            GPIO.output(LED_PINS[idx], update_leds.status[idx])

    elif (command == LED_UPDATE_CMD):
        if (led_num < NUM_OF_LEDS):
            update_leds.status[led_num] = not update_leds.status[led_num]
            GPIO.output(LED_PINS[led_num], update_leds.status[led_num])
        else:
            print(f"Invlaid LED NUM recieved (led_num = {led_num})")
    else:
        print(f"Invalid command recieved (command = {command})")

#------------------------------------------------------------------------------
# DESCRIPTION:
#   This function builds the HTML string for the LED button.
#
# INPUT PARAMETERS:
#   led_num: String - Represents the LED button number
#
# OUTPUT PARAMETERS:
#   result: HTML String
#
# RETURN:
#   An HTML string for the web request
#------------------------------------------------------------------------------
def html_for_led(led_num):
    #----------------------
    # Local Variables
    #----------------------
    led_num_string = ""
    result = ""

    # Convert led_num to a string
    led_num_string = str(led_num)

    # Build html code for each LED
    result = "<input type='button' style='background-color:"\
             + BUTTON_COLOR[led_num] + "'  onClick='changed("\
             + led_num_string + ")' value='" + LED_STRINGS[led_num] + "'/>"
    return result

#------------------------------------------------------------------------------
# DESCRIPTION:
#   This function reads the GPIO pin to determine the status of the switch.
#
# OUTPUT PARAMETERS:
#   String 
#
# RETURN:
#   The string 'Up' if the switch status GPIO pin is 1. Otherwise, 
#   the function returns 'Down' if the switch is 0.
#------------------------------------------------------------------------------
def switch_status():
    button_state = GPIO.input(BUTTON_PIN)
    if (button_state == GPIO.LOW):
        return "Down"
    else:
        return "Up"

#------------------------------------------------------------------------------
# DESCRIPTION
#	This function cleans up the GPIO ports
#------------------------------------------------------------------------------
def destroy():
    GPIO.cleanup()

#------------------------------------------------------------------------------
# DESCRIPTION:
#   The main program function
#------------------------------------------------------------------------------
def main():
    
    print()
    print("********************** PROGRAM IS RUNNING **********************")
    print()
    print("Press CTRL-C to end the program")
    print()

    try:
        # Setup the GPIO and start the web serving process on port 80
        setup_gpio()
        run(host='0.0.0.0', port=80)

    except Exception as Error:
        # Occurs when an unknown exception is detected, prints out an error message
        print(f"Unexpected error detected: {Error}")
        
    finally:
        destroy()
        print("GPIO ports have been cleaned up")
        print()
        print("********************** PROGRAM TERMINATED **********************")
        print()

# Call the main function  
if __name__ == '__main__':
    main()