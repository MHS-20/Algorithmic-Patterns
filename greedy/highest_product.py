# given an array of integers
# return the highest product multiplying 3 elements

def highest_product(arr):
   arr = sorted(arr)

   res1 = arr[-1] * arr[-2] * arr[-3]
   res2 = arr[0] * arr[1] * arr[-1]

   return max(res1, res2)

