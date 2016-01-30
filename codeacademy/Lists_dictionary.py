'''
Lists are a datatype you can use to store a collection of different 
pieces of information as a sequence under a single variable name
Lists are very similar to strings, but there are a few key differences.
Access by Index-You can access an individual item on the list by its index>>>

a statement that prints the result of adding the second and fourth items of the list.
numbers = [5, 6, 7, 8]
print numbers[1] + numbers[3] 

Lists can be used to access as well as assign values
A list doesn't have to have a fixed length. You can add items to the end of a list

letters = ['a', 'b', 'c']
letters.append('d')
print len(letters)
print letters

List Slicing

letters = ['a', 'b', 'c', 'd', 'e']
slice = letters[1:3]
print slice
print letters
start at the index before the colon and continue up to but not including the index after the colon
'''
#On line 4, create a list called middle containing only the two middle items from suitcase.
#On line 5, create a list called last made up only of the last two items from suitcase.
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

first  = suitcase[0:2]  # The first and second items (index zero and one)
middle = suitcase[2:4]
 # Third and fourth items (index two and three)
last   =  suitcase[4:]             # The last two items (index four and five)




'''Slicing Lists and Strings
You can slice a string exactly like a list! In fact, 
you can think of strings as lists of characters: 
each character is a sequential item in the list, starting from index 0

my_list[:2]
# Grabs the first two items
my_list[3:]
# Grabs the fourth through last items


If your list slice includes the very first or last item in a list (or a string),
 the index for that item doesn't have to be included.

Sometimes you need to search for an item in a list.

animals = ["ant", "bat", "cat"]
print animals.index("bat")


We can also insert items into a list.

animals.insert(1, "dog")
print animals





 '''


#Use the .index(item) function to find the index of "duck". Assign that result to a variable called duck_index.
#Then .insert(index, item) the string "cobra" at that index.
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")  # Use index() to find "duck"

# Your code here!
animals.insert(duck_index, "cobra")


print animals # Observe what prints after the insert operation


'''
for variable in list_name:
    # Do stuff!
A variable name follows the for keyword; it will be assigned the value of each list item in turn

'''

my_list = [1,9,3,8,5,7]

for number in my_list:
    # Your code here
    number = 2 * number
    print number
   ''' If your list is a jumbled mess, you may need to sort() it.

animals = ["cat", "ant", "bat"]
animals.sort()

for animal in animals:
    print animal'''



#First, we create a list called animals with three strings. The strings are not in alphabetical order.
#Then, we sort animals into alphabetical order. Note that .sort() modifies the list rather than returning a new list.
#Then, for each item in animals, we print that item out as "ant", "bat", "cat" on their own line each.
start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for lst in start_list:
    sq = lst ** 2
    square_list.append(sq)
    
    square_list.sort()
print square_list



######## A DICTIONARY

'''A dictionary is similar to a list, 
but you access values by looking up a key instead of an index. A key can be any string or number.
 Dictionaries are enclosed in curly braces, like so:
 d = {'key1' : 1, 'key2' : 2, 'key3' : 3}
 This is a dictionary called d with three key-value pairs. The key 'key1' points to the value 1, 'key2' to 2, and so on.
 Dictionaries are great for things like phone books (pairing a name with a phone number), 
 login pages (pairing an e-mail address with a username), and more!

 Print the values stored under the 'Sloth' and 'Burmese Python' keys.
  Accessing dictionary values by key is just like accessing list values by index:

 '''

# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}
 residents['Puffin']
# Gets the value 104


'''
Like Lists, Dictionaries are "mutable". This means they can be changed after they are created. 
One advantage of this is that we can add new key/value pairs to the dictionary after it is created like so:
dict_name[new_key] = new_value
The length len() of a dictionary is the number of key-value pairs it has. 
Each pair counts only once, even if the value is a list. (That's right: you can put lists inside dictionaries!)

'''

#Add at least three more key-value pairs to the menu variable, with the dish name (as a "string") for the key and the price (a float or integer) as the value. Here's an example:

#menu['Spam'] = 2.50
menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']

# Your code here: Add some dish-price pairs to menu!

menu['nyama'] = 292
menu['kuku'] = 9393
menu['ugali'] = 9393

print "There are " + str(len(menu)) + " items on the menu."
print menu


# key - animal_name : value - location 
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']
# Your code here!
zoo_animals['Rockhopper Penguin'] = 'hssbbb'




print zoo_animals
'''
dictionaries

my_dict = {
    "fish": ["c", "a", "r", "p"],
    "cash": -4483,
    "luck": "good"
}
print my_dict["fish"][0]
In the example above, we created a dictionary that holds many types of values.
The key "fish" has a list, the key "cash" has an int, and the key "luck" has a string.
Finally, we print the letter 'c'. When we access a value in the dictionary like my_dict["fish"],
 we have direct access to that value. So we can access the item at index '0' in the list stored by the key "fish" '''

#Instructions
#Add a key to inventory called 'pocket'
#Set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'
#.sort() the items in the list stored under the 'backpack' key
#Then .remove('dagger') from the list of items stored under the 'backpack' key
#Add 50 to the number stored under the 'gold' key

 inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 
inventory['backpack'].sort() 
inventory['backpack'].remove('dagger') 
inventory['gold'] += 50
#inventory.remove()
# Your code here

You can also use a for loop on a dictionary to loop through its keys with the following:

# A simple dictionary
d = {"foo" : "bar"}

for key in d: 
    print d[key]  # prints "bar" 
'''Note that dictionaries are unordered, meaning that any time you loop through a dictionary, 
you will go through every key, but you are not guaranteed to get them in any particular order.'''

#Use a for loop to go through the webster dictionary and print out all of the definitions.
webster = {
	"Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}

# Add your code below!
for k in webster:
    print webster[k]



#Instructions
#Like step 2 above, loop through each item in the list called a.
#Like step 3 above, if the number is even, print it out. You can test if the item % 2 == 0 to help you out.


    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for i in a:
    if i % 2 == 0:
        print i