#! /usr/bin/python3
# *****************************************************************************
# ***************************  Python Source Code  ****************************
# *****************************************************************************
#
#   DESIGNER NAME:  Bruce Link
#   STUDENT WORK:   James Ji, Samuel Acquaviva
#
#       FILE NAME:  lab11_part2.py
#
# DESCRIPTION
#   This file is the source code that runs on Raspberry Pi 4 board and
#   utilizes the LCD1602.py I2C LCD Display Driver. The program displays a
#   simple two line greeting on the LCD for a predefined amount of time.
#   Then the LCD is cleared and the current RPi CPU temperature is displayed
#   and subsequently updated every 2 seconds.
#
#   The program will continue in this loop until the user hits the CTRL-C,
#   at which time the loops exits and the program ends.
#
# *****************************************************************************

#---------------------------------------------------
# Import Statements
#---------------------------------------------------
import RPi.GPIO as GPIO
import time
from time import sleep

#---------------------------------------------------
# Constants to be used in program
#---------------------------------------------------
TRIG_PIN = 23
ECHO_PIN = 24
TIMEOUT = .05
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
def setup_gpio():
  GPIO.setmode(GPIO.BCM)

  GPIO.setup(TRIG_PIN, GPIO.OUT)
  GPIO.setup(ECHO_PIN, GPIO.IN)

def send_trigger_pulse():
  GPIO.output(TRIG_PIN, GPIO.HIGH)

  sleep(0.00010)

  GPIO.output(TRIG_PIN, GPIO.LOW)

def measure_return_echo():
  start_time = time.time()
  while GPIO.input(ECHO_PIN) == 0:
    current_time = time.time()
    if(current_time - start_time) > TIMEOUT:
      return 0
  start_time = current_time
  while GPIO.input(ECHO_PIN) == 1:
    current_time = time.time()
    if(current_time - start_time) > TIMEOUT:
      return 0
  
  return current_time - start_time

def loop():
  while True:
      send_trigger_pulse()
      distance =  (measure_return_echo() * 34300) / 2
      print("Distance: ", distance, "cm")


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
  GPIO.cleanup()

#---------------------------------------------------------------------
# This is the main function for the program
#---------------------------------------------------------------------
def main ():
  print()
  print("****************  PROGRAM IS RUNNING  ****************")
  print()
  print("Press CTRL-c to end the program.")
  print()

  try:
    setup_gpio()
    loop()

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