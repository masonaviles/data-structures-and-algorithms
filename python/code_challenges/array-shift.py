def insert(arr, num):
  counter = 0
  is_true = True
  new = []
  print(len(arr)/2)
  while is_true:
    if counter < round(len(arr)/2):
        new.append(arr[counter])
    elif counter == round(len(arr)/2):
      new.append(num)
    elif counter <= round(len(arr)):
      new.append(arr[counter - 1])     
    else:
      is_true = False
      print("send false")
      print(new)
      return new

    counter +=1

insert([1, 2, 3, 4, 5, 6], 8)
insert([1, 2, 3, 4, 5, 6, 7], 8)