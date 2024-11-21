#! /usr/bin/python3

#------------------------------------------------------------------------------
#----------------------------- Python Source Code -----------------------------
#------------------------------------------------------------------------------
#
#   DESIGNERS: James Ji, Samuel Acquaviva
#   FILE NAME: lab11_part3.py
#   
#   DESCRIPTION: This code uses the Raspberry Pi and LCD1602.py file to obtain
#                the CPU temperature and displays it onto a LCD display 
#                connected to the Raspberry Pi 
#
#------------------------------------------------------------------------------

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
#   This function runs the vcgencmd command to retrieve the CPU temp and then
#   slices the string to return only the temperature string ex: (21.2)
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
def get_cpu_temp():
    cpu_temp_string = ""

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