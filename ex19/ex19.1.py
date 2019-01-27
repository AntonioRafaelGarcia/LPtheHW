def new_function(*args):
    a, b, c = args
    print(a, b, c)

new_function(1, 2, 3)

var1 = 1 + 2
var2 = 3 + 4

new_function(var1, var2, var1 + var2)

new_function('a', 'b', 'c')

first_var = 1
second_var = 'b'

new_function(first_var + 2, 'a' + second_var, 'c')

another_var = int(input("Your input? "))
next_var = another_var + 35

new_function(next_var, next_var + 1, next_var + 2)
