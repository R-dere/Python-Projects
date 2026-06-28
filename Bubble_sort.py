def bubble_sort(array):
  x = len(array)
  for i in range(x):
    sorted = False
    for j in range(0, x - i - 1):
      if array[j] < array[j+1]:
        array[j], array[j+1] = array[j+1],array[j]
        print(array)
        sorted = True
    if not sorted:
      break
array = [78,43,952,100,5,7]
bubble_sort(array)
print(array)
