import os

# Create a child process
child_pid = os.fork()

if child_pid == 0:
	# This code will be executed by the child process

	# Using execl ()
	#os.execl('/bin/ls', 'bin/ls', '-l')

	# Using execle()
	#os.execle('/bin/ls', '/bin/ls', '-l', os.environ)

	# Using execlp()
	#os.execlp('ls', 'ls', '-l')

	# Using execv()
	#os.execv('/bin/ls', ['/bin/ls', '-l'])

	# Using execvp()
	#os.execvp('ls', ['ls', '-l'])

	# Using execvpe()
	os.execvpe('ls', ['ls', '-l'], os.environ)

	print("This will not be printed")
else:
	# This code will be executed by the parent process

	# Wait for the child process to finish
	os.wait()
	print("Parent process")

