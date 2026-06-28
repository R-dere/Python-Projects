def bubble_sort(array):
  x = len(array)
  for i in range(x):
    sorted = False
    for j in range(0, x - i - 1):
      if array[j] > array[j+1]:
        array[j], array[j+1] = array[j+1],array[j]
        sorted = True
    if not sorted:
      break

def binary_search(array):
  search_no = float(input("what number are you looking for?"))
  if search_no not in array:
    print("not in the list")
    binary_search()
  found = False
  while not found:
    arrlen = len(array)
    i = arrlen // 2
    x = array[i]
    if x == search_no:
      found = True
    elif search_no > x:
      array = array[i:]
    else:
      array = array[:i]
  print("value found")

array = [78,43,952,83.7,100,5,7,67,42,58,603,82,72]
bubble_sort(array)
print(array)
binary_search(array)
