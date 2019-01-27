#enables argv use in document
from sys import argv

#uses argv assignment to desired filename used in program
script, filename = argv

# prints statement of intent to erase/truncate/empty the argv-designated file
print(f"We're going to erase {filename}.")
# prints statements
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

# uses ? as user prompt
input("?")

# prints statement, opens argv-designated file as a write file and assigns it to target
print("Opening the file...")
target = open(filename, 'w')

# prints statement, erases/truncates/empties the write file target from the assignment above
print("Truncating the file. Goodbye!")
target.truncate()

# prints statement, prompts user for 3 consecutive lines and assigns each to respective line variables
print("Now I'm going to ask you for three lines.")
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

# prints statement, writes each user-prompted string variable from assignments above to write file target, separated by a newline
print("I'm going to write these to the file.")
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

# prints statement, closes write file target
print("And finally, we close it.")
target.close()
