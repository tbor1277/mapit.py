#!python3

import webbrowser
import sys

if len(sys.argv) > 1:
	address = " ".join(sys.argv[1:])
else:
	print('Please type in an address to search in maps.')

webbrowser.open('https://www.google.com/maps/place/'+ address)
