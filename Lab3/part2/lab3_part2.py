import os

file_path = "concurrent_write.txt"
file_descriptor = os.open(file_path, os.O_CREAT | os.O_WRONLY)

# Create a child process
child_pid = os.fork()

if child_pid == 0:
	# This code will be executed by the child process
	child_message = "Hello from the child process!\n"
	os.write(file_descriptor, child_message.encode())
else:
	# This code will be executed by the parent process
	parent_message = "Hello from the parent process!\n"
	os.write(file_descriptor, parent_message.encode())

# Close the file descriptor
os.close(file_descriptor)
