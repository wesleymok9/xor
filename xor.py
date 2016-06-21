#!/usr/bin/env python
import sys
import getopt

def usage():
	print """Usage: python xor.py [option] [value] filename	
Options:
\n
\t-h, --help            show this help message and exit
\n
\t-d, --deci            lets you pass an argument to xor the file by the bytes provided in base 10
\n
\t-x, --hexi            lets you pass an argument to xor the file by the bytes provided in base 16"""	

def xor10(numBytes, file):
	b = bytearray(open(file, 'rb').read())
        for i in range(len(b)):
                b[i] ^= int(numBytes)
        open("xor'd_"+numBytes+"_"+file, 'wb').write(b)

def xor16(numBytes, file):
	b = bytearray(open(file, 'rb').read())
        for i in range(len(b)):
                b[i] ^= int(numBytes, 16)
        open("xor'd_"+numBytes+"_"+file, 'wb').write(b)

def main():
	try:
		opts, args = getopt.getopt(sys.argv[1:],"hd:x:", ["help", "deci=", "hexi="])

	except getopt.GetoptError:
		usage()
		sys.exit(2)

	for opt, arg in opts:
		if opt in ("-h", "--help"):
			usage()
			sys.exit()
		elif opt in ("-d", "--deci"):
			xor10(arg, args[0])
		elif opt in ("-x", "--hexi"):
			xor16(arg, args[0])

if __name__ == '__main__':
	main()

