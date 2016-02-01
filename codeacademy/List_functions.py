def count_samll(numbers):
	total = 0
	for n in numbers:
		if n < 10:
			total = total + 1
	return total

lost = [4, 8, 15, 16, 23, 42]
small = count_samll(lost)
print small

#
#Write a function that counts how many times the string "fizz" appears in a list.
#1.	Write a function called fizz_countthat takes a list x as input.
#2.	Create a variable count to hold the ongoing count. Initialize it to zero.
#3.	for each item in x:, if that item is equal to the string "fizz" then increment the count variable.
#4.	After the loop, please return thecount variable.
#For example,fizz_count(["fizz","cat","fizz"])should return 2.

def fizz_count(x):
	count = 0
	for i in x:
		if i =="fizz":
			count += 1
	return count
y = ["fizz","cat","fizz"]
c = fizz_count(y)
print c





#String Looping
once  = {'a': 1, 'b': 2}
twice = {'a': 2, 'b': 4}
for key in once:
    print "Once: %s" % once[key]
    print "Twice: %s" % twice[key]




prices = {"banana": 4,"apple": 2,
"orange": 1.5,
"pear": 3
}
stock = {"banana": 6, 
"apple": 0,
"orange": 32,
"pear": 15
}

#Let's determine how much money you would make if you sold all of your food.
#1.	Create a variable called total and set it to zero.
#2.	Loop through the pricesdictionaries.
#3.	For each key in prices, multiply the number in prices by the number in stock. Print that value into the console and then add it to total.
#4.	Finally, outside your loop, printtotal.

for key in prices:
	print "price: %s" % prices[key]
	print "stock: %s" % stock[key]

total = 0
for key in prices:
	s = prices[key] * stock[key]
	print s
	total = total + s
print total

#Shopping at the Market
'''def sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
n = [1, 2, 5, 10, 13]
print sum(n)'''

'''
1.	Define a function compute_billthat takes one argument food as input.
2.	In the function, create a variabletotal with an initial value of zero.
3.	For each item in the food list, add the price of that item to total.
4.	Finally, return the total.
Ignore whether or not the item you're billing for is in stock
'''

shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

groceries = ["banana", "orange", "apple"]

def compute_bill(food):
	totalz = 0
	#1.	While you loop through each item of food, only add the price of the item to total if the item's stock count is greater than zero
	for i in food:
		#print prices[i]
		#print stock[i]
		if stock[i] > 0:
		    totalz = prices[i] + totalz
		   # 2.	If the item is in stock and after you add the price to the total, subtract one from the item's stock count.
		    stock[i] = stock[i] - 1
		    print stock[i]
	#return total
	print totalz
foodsum = compute_bill(groceries)
'''Stocking Out
Now you need your compute_billfunction to take the stock/inventory of a particular item into account when computing the cost
Ultimately, if an item isn't in stock, then it shouldn't be included in the total. You can't buy or sell what you don't have!
'''


