from collections import Counter 
  
def firstRepeat(input): 
      
    # first split given string separated by space 
    # into words 
    words = input.split(' ') 
      
    # now convert list of words into dictionary 
    dict = Counter(words) 
  
    # traverse list of words and check which first word 
    # has frequency > 1 
    for key in words: 
        if dict[key]>1: 
            print (key) 
            return