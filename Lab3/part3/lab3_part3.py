import os
import time

# Create a child process
child_pid = os.fork()

if child_pid == 0:
	# This code will be executed by the child process
	print("Hello")
else:
	# This code will be executed by the parent process
	# We introduce a small delay here to force the order
	time.sleep(0.1)
	print("Goodbye")

