from bottle import route, run, template
import RPi.GPIO as GPIO
import time


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
SERVO_DELAY_SEC             = 0.5		                                                        
PWM_FREQUENCY               = 50 		                                                        

LED_PINS                    = [RED_LED_PIN, GRN_LED_PIN, BLU_LED_PIN]
LED_STRINGS                 = ["Red LED", "Green LED", "Blue LED"]
BUTTON_COLOR                = ["Tomato", "Green", "DodgerBlue"]

# define logic state to control LED (source current)
LED_OFF = GPIO.LOW
LED_ON  = GPIO.HIGH


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

    # set LED pin and Button pin to OUTPUT mode
    GPIO.setup(BUTTON_PIN, GPIO.OUT)
    GPIO.setup(RED_LED_PIN, GPIO.OUT)
    GPIO.setup(GRN_LED_PIN, GPIO.OUT)
    GPIO.setup(BLU_LED_PIN, GPIO.OUT)

    
    # set PWM frequency
    button = GPIO.PWM(BUTTON_PIN, PWM_FREQUENCY)
    red_led = GPIO.PWM(RED_LED_PIN, PWM_FREQUENCY)
    grn_led = GPIO.PWM(RED_LED_PIN, PWM_FREQUENCY)
    blu_led = GPIO.PWM(GRN_LED_PIN, PWM_FREQUENCY)

    return (red_led)

@route('/')
@route('/<led>')
def process_request(led="n"):
    led_num = 0
    response = ""

    if (led != "n"):
        print()
        print(f"LED button {led} pressed")

        led_num = int(led)

        update_leds(LED_UPDATE_CMD, led_num)
    else:
        print()
        print(f"Default call. No LED button pressed")
    
    # build HTML string
    response = "<script>"
    response += "function changed(led)"
    response += "{"
    response += "    window.location.href='/' + led"
    response += "}"
    response += "</script>"

    response += '<h1>CPT-210: GPIO Control</h1>'
    response += '<h2>Button=' + switch_status() + '</h2>'
    response += '<input type="button" onclick="changed('+\
                str(NUM_OF_LEDS)+')" value="Read Switch">'
    response += '<h2>LEDS</h2>'
    response += html_for_led(0)
    response += html_for_led(1)
    response += html_for_led(2)

    return response

def update_leds(command, led_num):
    # This function creates a "static-like" cariable to keep track of the
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

def html_for_led(led_num):
    led_num_string = ""
    result = ""

    led_num_string = str(led_num)

    result = "<input type='button' style='background-color:"\
             + BUTTON_COLOR[led_num] + "'  onClick='changed("\
             + led_num_string + ")' value='" + LED_STRINGS[led_num] + "'/>"
    return result

def switch_status():
    return "Up"

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
def destroy():
    GPIO.cleanup()

    
def main():
    print()
    print("********************** PROGRAM IS RUNNING **********************")
    print()
    print("Press CTRL-C to end the program")
    print()

    try:
        red_led = setup_gpio()
        run(host='0.0.0.0', port=80)

    except Exception as Error:
        print(f"Unexpected error detected: {Error}")
        
    finally:
        destroy()
        print("GPIO ports have been cleaned up")
        print()
        print("********************** PROGRAM TERMINATED **********************")
        print()
       
if __name__ == '__main__':
    main()