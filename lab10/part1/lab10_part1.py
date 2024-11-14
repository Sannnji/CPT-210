#! /usr/bin/python3
#------------------------------------------------------------------------------
#----------------------------- Python Source Code -----------------------------
#------------------------------------------------------------------------------
#
#   DESIGNERS: James Ji, Samuel Acquaviva
#   FILE NAME: lab10_part1.py
#   
#   DESCRIPTION: This code creates a simple web server which displays the 
#   current time as perceived by the host, which in this case is 
#   the Raspberry Pi.
#
#------------------------------------------------------------------------------

# Import Statements
from bottle import route, run, template
from datetime import datetime

#------------------------------------------------------------------------------
# DESCRIPTION:
#   This function is activated via the route once a web request is made. 
#   The function itself returns the current time on the Raspberry Pi.
#
# OUTPUT PARAMETERS:
#   String
#
# RETURN:
#   A formatted HTML string containing the current date and time according to
#   the Raspberry Pi.
#------------------------------------------------------------------------------
@route('/')
def get_time():
    #----------------------
    # Local Variables
    #----------------------
    date_time       = 0
    time            = 0
    html_string     = 0

    # Get the current date and time on the RPi
    date_time = datetime.now()

    # Format the date and time
    time = "{:%m-%d-%Y %H:%M:%S}".format(date_time)

    # Build the HTML string
    html_string = template('<b>Pi thinks the date/time is {{t}}<b>', t=time)

    return (html_string)

#------------------------------------------------------------------------------
# DESCRIPTION:
#   The main program function
#------------------------------------------------------------------------------
def main():

    print()
    print("********************** PROGRAM IS RUNNING **********************")
    print()

    try:
        # Starts the web serving process on port 80
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
