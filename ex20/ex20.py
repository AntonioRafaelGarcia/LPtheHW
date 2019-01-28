# makes argv available in this script
from sys import argv

# uses argv to assign user input when calling script
script, input_file = argv

# defines function to read and print input variable file
def print_all(f):
    print(f.read())

# defines function to go to very first line of inputted variable file
def rewind(f):
    f.seek(0)

# defines a function to take designated count and file variables and print the count and associated line
def print_a_line(line_count, f):
    print(line_count, f.readline())

# opens and assigns the argv-designated file variable to a new variable
current_file = open(input_file)

# prints string and newline escape sequence
print("First let's print the whole file:\n")

# calls function print_all using the opened argv-designated file variable
print_all(current_file)

# prints string
print("Now let's rewind, kind of like a tape.")

# calls function rewind using the opened argv-designated file variable
rewind(current_file)

# prints string
print("Let's print three lines:")

# thrice calls function print_a_line using the opened argv-designated file variable, iterating up from 1
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
