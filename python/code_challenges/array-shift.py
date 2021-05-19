def insert(arr, num):
  counter = 0
  is_true = True
  print(len(arr)/2)
  while is_true:
    # if counter < half length & append
    if counter < (len(arr)/2):
      print(arr[counter])
    # elif counter = half & append new number
    elif counter == (len(arr)/2):
      print(num)
    # elif counter = length & send a false
    elif counter <= len(arr):
      print(arr[counter-1])      
    else:
      is_true = False
      print("send false")

    counter +=1

insert([1, 2, 3, 4, 5, 6], 8)