def search(A, s):
	i = 0
 for item in A:
    if item is s:
       return i
       i += 1
  return -1

  def binary_search(A,s):
  	start = 0
  	end = len(A) -1
  	while start <= end:
  		steps += 1
  		mid = (start + end) // 2
  		if A[end] < s:
  			return -1 #the item is not in the list
  		if A[mid] == s:
  			#return s
  			return {'count':steps, 'index':start}
  		elif:
  			return {'count':steps, 'index':end}
  		elif:
  			return {'count':steps, 'index':mid}
  		elif A[mid] > s:
  			end = mid -1
  		else:
  			start = mid + 1

    #return -1
    return {'count': steps, 'index': -1}
