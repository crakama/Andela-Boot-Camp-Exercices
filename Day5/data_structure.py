#Phone book
# (1)use a tuple
# 2 (use a dictionary 'dict')
#data will be stored as a nested list

class PhoneBookList(object):
	'''
	This class employs `list` datastructure in managing Phone contacts.

	'''
	def __init__(self):
	 	self.book = []
	def add_contact(self, username, phone_number):
	 	#record is a tupple
	 	#record = (username, phone_number)
	 	#changing fro tupples to use list cz tuples are imutable,
	 	# in tuple u cant modify cz u will have to oeveride them in future in case u come with a new list
	 	record = [username, phone_number] 
	 	self.book.append(record)
        #adds small list to layer two in the phone book
	 	#b = PhoneBookList()
	 	#b.add_contact('kate', '883993')

	 	#b.book  prints a nested list [[], []]
	def search(self, username):

	 ''' returns a `dict` with phone_number and number of loop count e.g {'count': 'austin', 'phone_number'}'''
	 count = 0
	 for usn, phn in self.book:
	   	    count += 1
	   	    if usn == username:
	   	    	result = {
	   	    	       'count': count,
	   	    	       'phone_number': phn
	   	    	}
#if record not found
	   	    	return result
	 result = {
	   	    	       'count': count,
	   	    	       'phone_number': None
	   	    	}
	 return result
	   	    	# a dictionary that has key (6) and value(9)



class PhoneBookDict(object):
	'''
	This class employs `dict` datastructure in managing Phone contacts.

	'''
	def __init__(self):
	 	self.book = {}
	def add_contact(self, username, phone_number):
	 	
	 pass
	def search(self, username):

	 ''' returns a `dict` with phone_number and number of loop count e.g {'count': 'austin', 'phone_number'}'''
	 
#if record not found
	   	    	return result
	 result = {
	   	    	       'count': count,
	   	    	       'phone_number': None
	   	    	}
	 return result
	   	    	# a dictionary that has key (6) and value(9)
