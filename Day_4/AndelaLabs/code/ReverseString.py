'''def swap(list_,i,j):
    list_[i],list_[j] = list_[i],list_[j]

def reverse_string(string):
	new_string = list(string)
	lenght = len(new_string)
	for i in range(lenght // 2):
		#temp = new_s[i]
		swap(new_string, i,lenght -i -1)
		#new_s[lenght -i -1] = temp
		 #x, y = y , x
        return "".join(new_string)
        
if new_string == string:
  return True'''
def reverse_string(n):
  if n == "":
    return None
  else:
    return n[::-1]
  if n[::-1] == n:
   return True
 
    