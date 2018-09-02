#makes argv available for use in this script
from sys import argv

#assigns the argv inputs, left to right, to script and then filename
script, filename = argv

#opens [filename] and assigns that open file to txt
txt = open(filename)

#prints a [filename]-seeded string-line, then read-prints out [filename]
print(f"Here's your file {filename}:")
print(txt.read())
txt.close()

"""prints a request for the user to again input [filename]
with a > prompt
and assigns that to [file_again]"""

print("Type the filename again:")
file_again = input("> ")

#opens [file_again], assigns it to [txt_again], and read-prints it
txt_again = open(file_again)
print(txt_again.read())
txt_again.close()
