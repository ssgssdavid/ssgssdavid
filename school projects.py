print("this is my first program")

# A cookie recipe calls for the following ingredients:
# 1.5 cups of sugar
# 1 cup of butter
# 2.75 cups of flour
# The recipe produces 48 cookies. Design a program that asks the user how many cookies he or she wants to make, and then displays the number of cups of each ingredient needed for the specified number of cookies.

print("Davids cookie recipe calculator")

# setup constants for our recipe that wont change
COOKIES = 48
SUGAR = 1.5
FLOUR = 2.75
BUTTER = 1

# get input from the user for how many cookies they would like to make
req_cookies = int(input("how many cookies would you like to make?\t"))

#calculate ingredient amount
# we do this by reducing the recipe to a per cookie basis, the multiplying by the number of cookie the use would like to make.

sugar_req = (SUGAR / COOKIES) * req_cookies
butter_req = (BUTTER / COOKIES) * req_cookies
flour_req = (FLOUR / COOKIES) * req_cookies

# get input from the user for how many cookie they would like to make

print("you will need:")
print("\t",sugar_req,"cups of sugar")
print("\t",butter_req,"cups of butter")
print("\t",flour_req,"cups of flour")

