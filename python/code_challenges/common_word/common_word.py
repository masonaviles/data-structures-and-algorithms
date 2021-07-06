from collections import Counter

# function which returns
# most frequeent word
def mostFrequentWord(words):
   
    # Takig empty list
    list = []
    for word in words:
       
        # Getting all words
        for j in word.split():
            list.append(j)
             
    # Calculating frequency of all words
    freq = Counter(list)
     
    # find max count and print that key
    max = 0
    for i in freq:
        if(freq[i] > max):
            max = freq[i]
            word = i
            return word