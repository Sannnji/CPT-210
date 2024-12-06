#! /usr/bin/python3
# *****************************************************************************
# ***************************  Python Source Code  ****************************
# *****************************************************************************
#
#   DESIGNER NAME:  Bruce Link
#   STUDENT WORK:   James Ji, Samuel Acquaviva
#
#       FILE NAME:  lab12_part1.py
#
# DESCRIPTION
#   This lab utilizes the HC-SR04 Ultrasonic Sensor Module, a commonly used 
#   sensor in embedded systems. Ultrasonic sensors, like the HC-SR04, emit 
#   high-frequency sound waves and measure the time it takes to bounce back
#   to the sensor.
#
#   The code utilizes the HC-SR04 Ultrasonic Sensor to create a program that
#   constantly outputs the distance detected by the sensor, until the user 
#   exits the program.
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
#   This function sets up GPIO interface pins for the HC-SR04 sensor and 
#   returns nothing.
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
  GPIO.setmode(GPIO.BCM)

  GPIO.setup(TRIG_PIN, GPIO.OUT)
  GPIO.setup(ECHO_PIN, GPIO.IN)

# -----------------------------------------------------------------------------
# DESCRIPTION
#   This function pulses trigger for at least 10 uSeconds. It accepts no 
#   arguments and returns nothing
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
def send_trigger_pulse():
  GPIO.output(TRIG_PIN, GPIO.HIGH)

  sleep(0.00010)

  GPIO.output(TRIG_PIN, GPIO.LOW)

# -----------------------------------------------------------------------------
# DESCRIPTION
#   This function detects and measures the Echo signal. The function returns 
#   the duration of the pulse in uSeconds. If the signal is not detected 
#   before the timeout period expires, the function returns 0.
#
# INPUT PARAMETERS:
#   none
#
# OUTPUT PARAMETERS:
#   int
#
# RETURN:
#   The duration of the pulse in uSeconds
# -----------------------------------------------------------------------------
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

# -----------------------------------------------------------------------------
# DESCRIPTION
#   This function contains the main loop for interfacing with the hardware. 
#   Once the design enters the loop, the design loop continuously triggers 
#   the sensor constantly until CTRL-C is detected.
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