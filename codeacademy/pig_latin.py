

# Start coding here!
original = raw_input("Enter a word:")

'''
We can check that the user's string actually has characters!

Write an if statement that verifies that the string has characters.

Add an if statement that checks that len(original) is greater than zero. Don't forget the : at the end of the if statement!
If the string actually has some characters in it, print the user's word.
Otherwise (i.e. an else: statement), please print "empty".
You'll want to run your code multiple times, testing an empty string and a string with characters.

empty_string = ""
if len(empty_string) > 0:
    # Run this block.
    # Maybe print something?
else:
    # That string must have been empty.'''

 print 'Welcome to the Pig Latin Translator!'

# Start coding here!
empty_str = ""
original = raw_input("Enter a word:")
if len(original) > 0:
    print original
else:
    print "empty"





    #x = "cate123"
#checks in the string if it contains characters alone or mix of characters and numbers
#x.isalpha()
print 'Welcome to the Pig Latin Translator!'

# Start coding here!
#empty_str = ""
original = raw_input("Enter a word:")
original.isalpha()
if len(original) > 0 and original.isalpha():
    print original
else:
    print "empty"



 '''to start translating to Pig Latin! Let's review the rules for translation:

You move the first letter of the word to the end and then append the suffix 'ay'.
Example: python -> ythonpay

Let's create a variable to hold our translation suffix.'''

pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    #returns a lowercase-version
    word = original.lower()
    '''grabs the first letter of the word
    '''
    first = word[0]
    print original
    print first
    
else:
    print 'empty'


    '''
    Now that we have the first letter stored, we need to add both 
    the letter and the string stored in pyg to the end of the original string

Move it on Back
Now that we have the first letter stored, we need to
 add both the letter and the string stored in pyg to the end of the original string.




    '''

pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    #returns a lowercase-version
    word = original.lower()
    
    #grabs the first letter of the word
    first = word[0]
    new_word = word + first + pyg
    print original
    print first
    
else:
    print 'empty'



     '''now we have the first letter showing up both at the beginning and near the end

     s = "Charlie"

print s[0]
# will print "C"

print s[1:4]
# will print "har"
Advanced Tip! When slicing until the end of the string, instead of providing len(new_word), you can also not supply the second index:

my_string = "Python"
my_string[1:] # "ython"'''
pyg = 'ay'
s = "Charlie"

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    #returns a lowercase-version
    word = original.lower()
    
    #grabs the first letter of the word
    first = word[0]
    new_word = word + first + pyg
    print len(new_word)
    x = original[0]
    new_word = original[1:len(new_word)] + x + pyg
    print original
    print first
    
else:
    print 'empty'