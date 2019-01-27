# defines primary function with cheese and crackerbox input variables
# prints a series of embedded strings
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# prints string, calls function with specific integer inputs
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# prints string, assigns integer values to new variables
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

# calls function using new variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# prints string, calls function with arithmetic variable inputs
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# prints string, calls function with arithmetic variable inputs that combine integer and new variables
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
