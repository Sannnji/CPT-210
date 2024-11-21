#! /usr/bin/python3
# *****************************************************************************
# ***************************  Python Source Code  ****************************
# *****************************************************************************
#
#   DESIGNER NAME:  Bruce Link
#   STUDENT WORK:   James Ji, Samuel Acquaviva
#
#       FILE NAME:  lab11_part3.py
#
# DESCRIPTION
#   This file is the source code that runs on Raspberry Pi 4 board and
#   utilizes the LCD1602.py I2C LCD Display Driver. The program displays a
#   simple two line greeting on the LCD for a predefined amount of time.
#   Then the LCD is cleared and the current RPi CPU temperature is displayed.
#
#   The purpose of this program is for consistent excecution via a crontab.
#
# *****************************************************************************

#---------------------------------------------------
# Import Statements
#---------------------------------------------------
import LCD1602
import time
import os

#---------------------------------------------------
# Constants to be used in program
#---------------------------------------------------
IIC_BUS_NUMBER       = 1

MESSAGE_STRING_1     = "RPi CPU Temp"
MESSAGE_STRING_3     = (" " * LCD1602.MAX_CHAR_POSITION) + "Thank you CPT-210 :)"

# -----------------------------------------------------------------------------
# DESCRIPTION
#   This function returns the temperature of the SoC as measured by its 
#   internal temperature sensor on the Raspberry Pi
#
# INPUT PARAMETERS:
#   none
#
# OUTPUT PARAMETERS:
#   String
#
# RETURN:
#   A String containing the current temperature of the SoC
# -----------------------------------------------------------------------------
def get_cpu_temp():
    cpu_temp_string = ""

    # Opens a pipe to the vcgencmd command to read the CPU's temperature.
    dev = os.popen('/usr/bin/vcgencmd measure_temp')

    cpu_temp_string = dev.read() [5:-3]

    return cpu_temp_string

#---------------------------------------------------------------------
# This is the main function for the program
#---------------------------------------------------------------------
def main ():
  #---------------------------------------------------
  # Variables to be used in main
  #---------------------------------------------------
  tmp_buffer = "is " + get_cpu_temp() + "\xDF" + "C"

  try:
    # Initializes the LCD via the specified I2C Bus
    LCD1602.init(LCD1602.LCD_IIC_ADDRESS, IIC_BUS_NUMBER)

    LCD1602.clear()

    # Writes the "RPi CPU Temp" header to the LCD
    LCD1602.write(LCD1602.LCD_CHAR_POSITION_3, LCD1602.LCD_LINE_NUM_1, MESSAGE_STRING_1)

    # Outputs the formatted current CPU temp to the LCD every 2 seconds
    LCD1602.write(LCD1602.LCD_CHAR_POSITION_4, LCD1602.LCD_LINE_NUM_2, tmp_buffer)

  finally:
    print()

# Call the main function.
main()