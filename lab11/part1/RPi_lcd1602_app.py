# *****************************************************************************
# ***************************  Python Source Code  ****************************
# *****************************************************************************
#
#   DESIGNER NAME:  Bruce Link
#
#       FILE NAME:  RPi_lc1602_app.py
#
# DESCRIPTION
#   This file is the source code that runs on Raspberry Pi 4 board and
#   utilizes the LCD1602.py I2C LCD Display Driver. The program display a
#   simple two line greeting on the LCD for a predefined amount of time.
#   Then the LCD is cleared and a 1 line greeting is scrolled across the LED.
#
#   You can use this as a template for displaying messages to the LCD display
#
#   The program will continue in this look until the user hits the CTRL-C,
#   at which time the loops exits and the program ends.
#
# *****************************************************************************

import LCD1602
import time

#---------------------------------------------------
# Constants to be used in program
#---------------------------------------------------
IIC_BUS_NUMBER       = 1

GREETING_1_HOLD_TIME = 3     # seconds
LCD_SCROLL_DELAY     = 0.3   # seconds

MESSAGE_STRING_1     = "Greetings!!"
MESSAGE_STRING_2     = "CPT 210 Folks"
MESSAGE_STRING_3     = (" " * LCD1602.MAX_CHAR_POSITION) + "Thank you CPT-210 :)"



# -----------------------------------------------------------------------------
# DESCRIPTION
#   This function cleans up the peripheral before the program terminates.
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
def destroy():
  LCD1602.clear()
  LCD1602.display_off()

#---------------------------------------------------------------------
# This is the main function for the program
#---------------------------------------------------------------------
def main ():
  #---------------------------------------------------
  # Variables to be used in main
  #---------------------------------------------------
  tmp_buffer = ""

  print()
  print("****************  PROGRAM IS RUNNING  ****************")
  print()
  print("Press CTRL-c to end the program.")
  print()

  try:

    LCD1602.init(LCD1602.LCD_IIC_ADDRESS, IIC_BUS_NUMBER)

    LCD1602.clear()

    # Display static welcome message on LCD
    LCD1602.write(LCD1602.LCD_CHAR_POSITION_1, LCD1602.LCD_LINE_NUM_1,
                  MESSAGE_STRING_1)

    LCD1602.write(LCD1602.LCD_CHAR_POSITION_2, LCD1602.LCD_LINE_NUM_2,
                  MESSAGE_STRING_2)

    time.sleep(GREETING_1_HOLD_TIME)

    LCD1602.clear()

    while True:
      tmp_buffer = MESSAGE_STRING_3

      # display scrolling message across the LCD
      for i in range(0, len(MESSAGE_STRING_3)):
        LCD1602.write(LCD1602.LCD_CHAR_POSITION_1, LCD1602.LCD_LINE_NUM_1,
                      tmp_buffer)

        time.sleep(LCD_SCROLL_DELAY)

        # shift message over 1 character
        tmp_buffer = tmp_buffer[1:]
        LCD1602.clear()

  except KeyboardInterrupt:
    print()
    print("CTRL-c detected.")

  finally:
    destroy()
    print()
    print("**************** PROGRAM TERMINATED ****************")
    print()




# Call the main function.
main()
