# *****************************************************************************
# ***************************  Python Source Code  ****************************
# *****************************************************************************
#
#   DESIGNER NAME:  
#
#       FILE NAME:  lab6_part1.py
#
# DESCRIPTION
#    This code provides ... <== FINISH ADDING DESCRIPTION OF WHAT THE CODE DOES
#
# *****************************************************************************
import RPi.GPIO as GPIO
import time

#---------------------------------------------------
# Constants to be used in program
#---------------------------------------------------
# GPIO number based on BCM GPIO numbering scheme
BUTTON_INPUT   =  18

# constants for delays
READ_DELAY_200MS = 0.2
READ_DDELAY_1SEC = 1

# -----------------------------------------------------------------------------
# DESCRIPTION
#   This function setup the RPi GPIO pins using the GPIO library. 
#
# INPUT PARAMETERS:
#   none
#
# OUTPUT PARAMETERS:
#   none
#
# RETURN:
#   none
# -----------------------------------------------------------------------------
def setup_gpio():
  # use BCM GPIO numbering scheme
  GPIO.setmode(GPIO.BCM)
  
  #set buttonPin to PULL UP INPUT mode
  GPIO.setup(BUTTON_INPUT, GPIO.IN, pull_up_down = GPIO.PUD_UP)

#---------------------------------------------------------------------
#  main() function
#---------------------------------------------------------------------
def main ():
  #-------------------------------------
  # Variables local to this function
  #-------------------------------------
  button_press_counter = 0

  print()
  print("************************ PROGRAM IS RUNNING ************************")
  print()
  print("Press CTRL-C to end the program.")
  print()

  try:
    setup_gpio()

    while True:
      # read the state of the input pin
      input_state = GPIO.input(BUTTON_INPUT)

      if (input_state == GPIO.LOW):
        button_press_counter = button_press_counter + 1

        print("Button has been pressed {button_pressed_counter} times.")

        # wait for button to be released
        while (input_state == GPIO.LOW):
          input_state = GPIO.input(BUTTON_INPUT)

          # add a small delay top slow loop down
          time.sleep(READ_DELAY_200MS)

  except KeyboardInterrupt:
    print()
    print("CTRL-c detected.")
  
  finally:
    GPIO.cleanup()
    print("GPIO Port have been cleaned up.")
    print()
    print("************************ PROGRAM TERMINATED ************************")
    print()

# if file execute standalone then call the main function.
if __name__ == '__main__':
  main()