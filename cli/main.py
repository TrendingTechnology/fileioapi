import getopt, sys
import fileioapi

argumentList = sys.argv[1:]
options = "::: "
long_options = ["Help", "upload", "download"]

try:
	arguments, values = getopt.getopt(argumentList, options, long_options)
	for currentArgument, currentValue in arguments:

		if currentArgument in ("-h", "--Help"):
			print ("Displaying Help")
		elif currentArgument in ("-upload", "--upload"):
			fileioapi.upload("image.png", expiry="12w")
		elif currentArgument in ("-download", "--download"):
			fileioapi.download(resp['link'], filename='downloaded.png')
		elif currentArgument in ("-o", "--Output"):
			print (("Enabling special output mode (% s)") % (currentValue))
			
except getopt.error as err:
	# output error, and return with an error code
	print (str(err))
