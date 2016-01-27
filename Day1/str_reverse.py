import unittest

def reverse(s):
  return s[::-1]
  
words = "andela"
print reverse(words)


#def reverse_x(s):
	#new_s list(s)
	#lenght = len(new_s)
	#for i in range(lenght // 2):
		#temp = new_s[i]
		#new_s[i] = new_s[lenght -i -1]
		#new_s[lenght -i -1] = temp
		
		#temp = y
		#y = x
		#x = temp
def swap(list_,i,j):
    list_[i],list_[j] = list_[i],list_[j]

def reverse_x(s):
	new_s = list(s)
	lenght = len(new_s)
	for i in range(lenght // 2):
		#temp = new_s[i]
		swap(new_s, i,lenght -i -1)
		#new_s[lenght -i -1] = temp
		 #x, y = y , x
        return "".join(new_s)

class reverse_s(unittest.TestCase):

  	def test_reverse_andela(self):
  		s = "andela"
		self.assertEqual(reverse(s),"aledna")

unittest.main()
 