#Method usially take the following syntax: object>>method>>parameter

#write a program that will append to list, the added number should be greater than the last nuber on the list

#while numbers > 50
numbers = [10,20,30,40,50]
numbers.append(60)
numbers.append(60)
print numbers



counted = numbers.count(60)
print counted




names = ['cate','kevin','christine','beatrice','stella']
extendfunc = names.extend(numbers)
print names

# print extendfunc- why does it print a none at the console?


#index() searches for the first occurance of a value in where in a list is
findindex = numbers.index(30)
print findindex
findstrindex = names.index('stella')
print findstrindex




#to insert elemnts in a list or sequence
towns = ['Nairobi','Kisumu','Kitale','Mombasa']
towns.insert(2,'Eldoret')
#userinput = input("please add town or city")
#towns.insert(2,userinput)>>>>ERROR
'''
please add town or cityTraceback (most recent call last):
  File "numbers.py", line 30, in <module>
    userinput = input("please add town or city")
  File "<string>", line 0

    ^
SyntaxError: unexpected EOF while parsing
'''
print towns

food = ['Ugali','Chapati','Beef','Chicken','Sukuma Wiki']
print food
popfood = food.pop(2)
print food
print popfood

#removing the first occurance of any word
animals = ['cow','dog','goat','sheep']
print animals
removeanimal = animals.remove('dog')
# print removeanimal ---ERROR>>prints out none
print animals


#reversing
country = ['kenya','uganda','tanzania','ethiopia']
print country
country.reverse()
print country

word ="Chapati".split()
print word.reverse()
