#! /usr/bin/python3

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
import os

#---------------------------------------------------
# Constants to be used in program
#---------------------------------------------------
IIC_BUS_NUMBER       = 1

MESSAGE_STRING_1     = "RPi CPU Temp"
MESSAGE_STRING_3     = (" " * LCD1602.MAX_CHAR_POSITION) + "Thank you CPT-210 :)"

def get_cpu_temp():
    cpu_temp_string = ""

    dev = os.popen('/usr/bin/vcgencmd measure_temp')

    cpu_temp_string = dev.read() [5:-3]

    return cpu_temp_string

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
  tmp_buffer = "is " + get_cpu_temp() + "\xDF" + "C"

  print()
  print("****************  PROGRAM IS RUNNING  ****************")
  print()
  print("Press CTRL-c to end the program.")
  print()

  try:

    LCD1602.init(LCD1602.LCD_IIC_ADDRESS, IIC_BUS_NUMBER)

    LCD1602.clear()

    LCD1602.write(LCD1602.LCD_CHAR_POSITION_3, LCD1602.LCD_LINE_NUM_1, MESSAGE_STRING_1)
    

    LCD1602.write(LCD1602.LCD_CHAR_POSITION_4, LCD1602.LCD_LINE_NUM_2, tmp_buffer)

  except KeyboardInterrupt:
    print()
    print("CTRL-c detected.")

  finally:
    print()
    print("**************** PROGRAM TERMINATED ****************")
    print()

# Call the main function.
main()