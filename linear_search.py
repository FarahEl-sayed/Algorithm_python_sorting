def linearSearch(arr, targted_value):
  for i in range(len(arr)):
    if arr[i] == targted_value:
      return i
  return -1

list = [3, 7, 2, 9, 5, 1, 8, 4, 6]
x = 4

#implmentation example
result = linearSearch(list, x)
if result != -1:
  print("Found at index", result)
else:
  print("Not found")