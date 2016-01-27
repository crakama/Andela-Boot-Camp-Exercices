def add(x,y):
	return x + y
y = lambda x,y: x + y

print add(10,2)

print y(10,2)


def make_incrementor(n):
	def inc(x):
		return x + n
	return inc
z = make_incrementor(10)

print z(20)

#f(x,x + 8)

def make_inc_lambda(n):
	return lambda x: x + n

a = make_inc_lambda(100)

print a(500)

def is_even(n):
	if n % 2 == 0:
		return true
	return false


def is_even(n):
	return n % 2 == 0
l = [2,10,4,5,6,11,12]
new_list = filter(is_even,l)


l = [2,10,4,5,6,11,12]
new_list = filter(lambda n: n % 2== 0, l)
print new_list


f = lambda (x: x **2)(20)

