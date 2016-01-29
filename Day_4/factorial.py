def factorial(number):
  #initialize the
  fnumber = 1
  while number > 0:
      fnumber = fnumber * number
      number = number - 1
  return fnumber
  
  Create a function fizz_buzz to return 'Fizz', 'Buzz', 'FizzBuzz', or the argument it receives, all depending on the argument of the function, a number that is divisible by, 3, 5, or both 3 and 5, respectively.

When the number is not divisible by 3 or 5, the number itself should be returned.