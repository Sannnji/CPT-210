# Import necessary modules
import os
import signal

# Define constants for custom signals
CHILD_SIGNAL = signal.SIGUSR1
PARENT_SIGNAL = signal.SIGUSR2

# Define signal handlers for the child and parent processes
def child_handler(signum, frame):
	print("Child process recieved signal:", signum)

def parent_handler(signum, frame):
	print("Parent process recieved signal:", signum)

# Set signal handlers
signal.signal(CHILD_SIGNAL, child_handler)
signal.signal(PARENT_SIGNAL, parent_handler)

#Create a child process using os.fork()
child_pid = os.fork()

if child_pid == 0:
	# Inside the child process
	print("Hello")
	# Send a signal to the parent process
	os.kill(os.getppid(), CHILD_SIGNAL)

else: 
	# Inside the parent process
	print("Goodbye")
	os.kill(child_pid, PARENT_SIGNAL)
	# Wait for the child process to complete
	os.wait()

