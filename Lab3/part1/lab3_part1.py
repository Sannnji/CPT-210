import os


# Initialize the variable x
x = 100

print("Original process - x:", x)

# Create a child process
child_pid = os.fork()

if child_pid == 0:
	# This code will be executed by the child process
	x = 200 # Change the vale of x in the child process
	print("Child process - x:", x)

elif child_pid > 0:
	# This code will be executed by the parent process
	x = 300 # Change the value of x in the parent process
	print("Parent process - x:", x)

else:
	# Forking failed
	print("Forking failed")

# This code will be executed by the parent and child processess
print("After changes - x:", x)

