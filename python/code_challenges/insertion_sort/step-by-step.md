```
( takes in an array of integers )
InsertionSort(int[] arr)
  
    ( For i in range(1, len(arr)) )
    FOR i = 1 to arr.length
    
        ( j = i -1 )
        int j <-- i - 1
        ( temp = arr[i] )
        int temp <-- arr[i]
      

        WHILE j >= 0 AND temp < arr[j]
            arr[j + 1] <-- arr[j]
            j <-- j - 1
        
        arr[j + 1] <-- temp
```

`the FOR is walking`
`the WHILE switches numbers depending on which is bigger, if there is no swtich, keep walking in the FOR` 
https://medium.com/basecs/inching-towards-insertion-sort-9799274430da

## algo
- a function that takes in an array of integers
- FOR 1 to array length
  - assign variable j to i - 1
  - assign variable temp to arr[i]
  - WHILE j is greater than or equal to 0 OR temp is less than arr[j]
    - arr[j+1] = arr[j]
    - j = j -1
  - temp = arr[j+1]


### Round 1
feed: [8,4,23,42,16,15]

`for i in range(1, len(arr))`
=
`for i in range(1, 6)`

feed the array into the function.
make a for loop that goes from 1 to the length of the array, 6 in this case

this makes `i` start at 1
currently `i = 1`

### Round 1.1
make a `j` variable that holds `i -1`
so in this round `j = 0`
make a `temp` varialbe that holds `arr[i]`
so in this round `temp = arr[1]`

### Round 1.2
`while j >= 0 AND temp < arr[j]`
so in this round
`while j=0 >= 0 AND temp=arr[1] < arr[j]`
`while 0 >= 0 AND 4 < 8`

### Round 1.2.1
`arr[j+1] = arr[j]`
`j = j-1`
so in this round...
`arr[1] = arr[j]`
`arr[j] = 8`
so the 8 position in the array is now arr[1]
`j = j-1`
`j = 0`

## Round 1.2.2
back at the WHILE
`8 < 4` -> false so it breaks out of the loop

### Round 1.3
`arr[j + 1] <-- temp`
`arr[1] = temp`

