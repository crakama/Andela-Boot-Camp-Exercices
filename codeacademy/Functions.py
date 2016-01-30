Functions

'''A function is a reusable section of code written to 
perform a specific task in a program'''

def square(n):
    """Returns the square of a number."""
    squared = n**2
    print "%d squared is %d." % (n, squared)
    return squared
    
# Call the square function on line 9! Make sure to
# include the number 10 between the parentheses.

#calling the funtion by passing parameters to it
 '''the function in the editor, power. It should take two arguments,
  a base and an exponent, and raise the first to the power of the second
square(10)'''
def power(base, exponent):  # Add your parameters here!
    result = base**exponent
    print "%d to the power of %d is %d." % (base, exponent, result)

power(2, 4)  # Add your arguments here!


''' Functions Calling Functions
Change the body of deserves_another so that it always adds 2 to the output of one_good_turn.


'''
def one_good_turn(n):
    return n + 1
    
def deserves_another(n):
    return one_good_turn(n) + 2

    '''
    def shout(phrase):
    if phrase == phrase.upper():
        return "YOU'RE SHOUTING!"
    else:
        return "Can you speak up?"

shout("I'M INTERESTED IN SHOUTING")


First, def a function called cube that takes an argument called number. Don't forget the parentheses and the colon!
Make that function return the cube of that number (i.e. that number multiplied by itself and multiplied by itself once again).
Define a second function called by_three that takes an argument called number.
if that number is divisible by 3, by_three should call cube(number) and return its result. Otherwise, by_three should return False.
Don't forget that if and else statements need a : at the end of that line!

?
Stuck? Get a hint!
if n % 3 == 0:
    print "n is divisible by 3"
else:
    print "n is not"
Make sure both functions return their values rather than printing them.

Both branches of the if/else statement in by_three need to have return statements in them (that's three returns total, two for by_three and one for cube).
'''
def cube(number):
    return number **3
def by_three(number):
    if number % 3 == 0:
        return cube(number)
        
    else:
        return False


''' A module is a file that contains definitions—including
        variables and functions—that you can use once it is imported.
       syntax>>>> 
       generic import >>> import math
              implementation>>>math.sqrt()!
       funtional impot>>>>from module import function: from math import sqrt

              implementation>>>>sqrt()
       if we still want all of the variables and functions in a module but don't want to have to constantly type math.?
       Universal import>>>from module import *

       abs()
The abs() function returns the absolute value of the number it takes as an argument—that is, that number's distance from 0 on an imagined number line. For instance, 3 and -3 both have the same absolute value: 3. 
The abs() function always returns a positive value, and unlike max() and min(), it only takes a single number.

Instructions
Below your existing code, define a function called rental_car_cost with an argument called days.
Calculate the cost of renting the car:
Every day you rent the car costs $40.
if you rent the car for 7 or more days, you get $50 off your total.
Alternatively (elif), if you rent the car for 3 or more days, you get $20 off your total.
You cannot get both of the above discounts.
Return that cost.
Just like in the example above, this check becomes simpler if you make the 7-day check an if statement and the 3-day check an elif statement.


       '''

def hotel_cost(nights):
    cost = 140
    costs = cost * nights
    return costs
    
def plane_ride_cost(city):
    
    if city == "Charlotte":
        cost = 183
        return cost
    elif city == "Tampa":
        cost = 220
        return cost 
    elif city == "Pittsburgh":
        cost = 222
        return cost
    else:
        cost = 475
        return cost
        
def rental_car_cost(days):
    cost = 40 * days
    if days >= 7:
        cost -= 50
    elif days >= 3:
        cost -= 20
    return cost




    '''
    Python Lists and Dictionaries

Lists and dictionaries are powerful tools you can use to store, organize, and manipulate all kinds of information.
'''