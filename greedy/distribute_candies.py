# given an array of numbers, everyone receive at least one candy
# if the numbers is greater than one of its neighbor, he get more candy than the neighbor

def distribute(arr): 
    n = len(arr)
    pos = sorted((rating,index) for index, rating in enumerate(arr)) # sort by rating, but keep reference to the original indexes
    candies = [1] * n

    # in order of rating
    for _, i  in pos: 
        if i > 0 and arr[i] > arr[i-1]:
            candies[i] = max(candies[i], candies[i-1]+1)

        if i < n-1 and arr[i] > arr[i+1]:
            candies = max(candies[i], candiens[i+1]+1)

    return sum(candies)
