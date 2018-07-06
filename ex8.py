formatter = "{} {} {} {}" # instantiate and assign 4 bracket placeholders to variable formatter

print(formatter.format(1, 2, 3, 4)) # format variable formatter with integers 1-4 and print it
print(formatter.format("one", "two", "three", "four")) # format variable formatter with strings one-four and print it
print(formatter.format(True, False, False, True)) # format variable formatter with four booleans and print it
print(formatter.format(formatter, formatter, formatter, formatter)) # format variable formatter with its initial instantiation and print it
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
)) # format variable formatter with four independent strings and print it
