def find_max_min(args):
  #assumes that min number is element at inex 0 and maximum number is element at index 1
  min_number = args[0]
  max_number = args[1]
  
  for i in args:
    if i < min_number:
      min_number = i
    elif i > max_number:
      max_number = i
  if min_number != max_number:
    return [min_number, max_number]
  else:
    #returns the number of elements in the lists
    return [len(args)]


    
