from bottle import route, run, template
from datetime import datetime

@route('/')
def get_time():
    date_time       = 0
    time            = 0
    html_string     = 0

    date_time = datetime.now()

    time = "{:%m-%d-%Y %H:%M:%S}".format(date_time)

    html_string = template('<b>Pi thinks the date/time is {{t}}<b>', t=time)

    return (html_string)

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
