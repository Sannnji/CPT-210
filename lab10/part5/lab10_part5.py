#! /usr/bin/python3
#------------------------------------------------------------------------------
#----------------------------- Python Source Code -----------------------------
#------------------------------------------------------------------------------
#
#   DESIGNERS: James Ji, Samuel Acquaviva
#   FILE NAME: lab10_part4.py
#   
#   DESCRIPTION: This lab part creates a web server page that displays the 
#   Raspberry Pi temperature using the built temperature sensor. 
#
#------------------------------------------------------------------------------

# Import Statements
import os
from bottle import route, run, template

# Local File Paths
MAIN_HTML_PATH      = "/media/yams/usb1/CPT210/lab10/part4/JustGage/main.html"
RAPHAEL_PATH        = "/media/yams/usb1/CPT210/lab10/part4/JustGage/raphael.2.1.0.min.js"
JUSTGAGE_PATH       = "/media/yams/usb1/CPT210/lab10/part4/JustGage/justgage.1.0.1.min.js"

#------------------------------------------------------------------------------
# DESCRIPTION:
#   This function accepts no parameters and returns the corresponding file path
#   (i.e., a Python constant ending with PATH that defines path to your JustGage 
#   files) using the bottle template object.  
#------------------------------------------------------------------------------
@route('/')
def main_html():
    return template(MAIN_HTML_PATH)

#------------------------------------------------------------------------------
# DESCRIPTION:
#   This function accepts no parameters and returns the CPU temperature as a 
#   string.
#
# OUTPUT PARAMETERS:
#   String
#
# RETURN:
#   The current CPU temperature
#------------------------------------------------------------------------------
@route('/temp')
def get_cpu_temp():
    cpu_temp_string = ""

    dev = os.popen('/usr/bin/vcgencmd measure_temp')

    cpu_temp_string = dev.read() [5:-3]

    return cpu_temp_string

#------------------------------------------------------------------------------
# DESCRIPTION:
#   These two functions are similar to the main_html function but use 
#   different URL paths and Python constants.
#------------------------------------------------------------------------------
@route('/raphael')
def raphael():
    return template(RAPHAEL_PATH)

@route('/justgage')
def gage():
    return template(JUSTGAGE_PATH)

#------------------------------------------------------------------------------
# DESCRIPTION:
#   The main program function
#------------------------------------------------------------------------------
def main():
    print()
    print("********************** PROGRAM IS RUNNING **********************")
    print()

    try:
        # Setup the GPIO and start the web serving process on port 80
        run(host='0.0.0.0', port=80)

    except Exception as Error:
        # Occurs when an unknown exception is detected, prints out an error message
        print(f"Unexpected error detected: {Error}")

    finally:
        print()
        print("********************** PROGRAM TERMINATED **********************")
        print()

# Call the main function 
if __name__ == '__main__':
    main()
