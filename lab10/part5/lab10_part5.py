import os
from bottle import route, run, template

MAIN_HTML_PATH      = "/media/yams/usb1/CPT210/lab10/part4/JustGage/main.html"
RAPHAEL_PATH        = "/media/yams/usb1/CPT210/lab10/part4/JustGage/raphael.2.1.0.min.js"
JUSTGAGE_PATH       = "/media/yams/usb1/CPT210/lab10/part4/JustGage/justgage.1.0.1.min.js"

@route('/')
def main_html():
    return template(MAIN_HTML_PATH)

@route('/temp')
def get_cpu_temp():
    cpu_temp_string = ""

    dev = os.popen('/usr/bin/vcgencmd measure_temp')

    cpu_temp_string = dev.read() [5:-3]

    return cpu_temp_string

@route('/raphael')
def raphael():
    return template(RAPHAEL_PATH)

@route('/justgage')
def gage():
    return template(JUSTGAGE_PATH)

def main():
    print()
    print("********************** PROGRAM IS RUNNING **********************")
    print()

    try:
        run(host='0.0.0.0', port=80)
    except Exception as Error:
        print(f"Unexpected error detected: {Error}")
    finally:
        print()
        print("********************** PROGRAM TERMINATED **********************")
        print()

if __name__ == '__main__':
    main()
