class exampleClass:
	name = "new class"
	age = "2"

	def thisIsMethod(self):
		return "this class has only one method"

	'''def county(self):
		country = ['kenya','uganda','tanzania','ethiopia']
        return country
#print country
        country.reverse()'''
        

#cretae an object to get data from the class
exampleObject = exampleClass()
print exampleObject.name
print exampleObject.age
#print exampleObject.county()
print exampleObject.thisIsMethod()