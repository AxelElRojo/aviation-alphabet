#!/bin/python
from sys import argv
letters = {
	'a' : 'Alfa',
	'b' : 'Bravo',
	'c' : 'Charlie',
	'd' : 'Delta',
	'e' : 'Echo',
	'f' : 'Foxtrot',
	'g' : 'Golf',
	'h' : 'Hotel',
	'i' : 'India',
	'j' : 'Juliett',
	'k' : 'Kilo',
	'l' : 'Lima',
	'm' : 'Mike',
	'n' : 'November',
	'o' : 'Oscar',
	'p' : 'Papa',
	'q' : 'Quebec',
	'r' : 'Romeo',
	's' : 'Sierra',
	't' : 'Tango',
	'u' : 'Uniform',
	'v' : 'Victor',
	'w' : 'Whiskey',
	'x' : 'X-ray',
	'y' : 'Yankee',
	'z' : 'Zulu'
}
def joinArguments(argVector : list):
	message = ""
	for arg in argVector:
		message += arg + ' '
	return message[:-1]
def calculateResult(message : str):
	string = ""
	for letter in message:
		if letter.isalpha():
			string += letters[ letter.lower() ] + ' '
		elif letter != ' ':
			string += letter + ' '
	return string[:-1]
def main(arguments : list):
	size = len(arguments)
	if size == 0:
		exit("Not enough arguments")
	elif size > 1:
		message = joinArguments(arguments)
	else:
		message = arguments[0]
	print( calculateResult(message) )
if __name__ == '__main__':
	argv.pop(0)
	main(argv)