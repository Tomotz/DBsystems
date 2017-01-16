import subprocess
from sys import argv



def main():
	user = ""
	if len(argv) != 2:
		print "usage:", argv[0], "nova username"
		if len(argv) == 1:
			print "using default user - tommottes"
			user = "tommottes"
		else:
			return
	else:
		user = argv[1]
	subprocess.call(["putty", "-N", "-L", "19821:mysqlsrv.cs.tau.ac.il:3306", user + "@nova.cs.tau.ac.il"])


if __name__ == "__main__":
	main()