import string

str1 = string.ascii_lowercase
str2 = ''.join([char*2 for i,char in enumerate(string.ascii_lowercase) if i %2 == 0])



dictionary1 = {char:char for char in str1}
dictionary2 = {char:str2[i+1]+char for i,char in enumerate(str2) if i%4 == 0}
dictionary3 = {'a': 'a', 'e': 'e', 'i': 'i', 'm': 'mm', 'q': 'qq', 'u': 'uu', 'y': 'yy'}


def left_join(dictionary1, dictionary2):
  # ret = []
  # keys = dictionary1.keys()
  # for key in keys:
  #   if key in dictionary2:
  #     ret.append([key, dictionary1[key],dictionary2[key]])
  #     continue

  #   ret.append([key, dictionary1[key], None])
  # return ret



  return [[key, dictionary1[key], dictionary2[key]] if key in dictionary2 else [key, dictionary1[key], None] for key in dictionary1]


print(left_join(dictionary1, dictionary2))
print(left_join(dictionary1, dictionary3))