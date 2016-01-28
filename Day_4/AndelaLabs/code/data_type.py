def data_type(i):
  if isinstance(i, str):
    return len(i)
  if i is None:
    return "no value"
  if isinstance(i, bool):
    return i
  if isinstance(i, int):
    if i >= 100:
      return "more than 100"
    else:
      return "less than 100" 
  if isinstance(i, list):
    #if the length of the list is greater than two then it's possible to access element 3 or i[2]
    if len(i) > 2:
      return i[2]
    return None
  