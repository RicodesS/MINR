import random
import timeit
# Iterative Binary Search Function 
# It returns index of x in given array arr if present, 
# else returns -1 
def binary_search(arr, x): 
    low = 0
    high = len(arr) - 1
    mid = 0
    n = 0 
  
    while low <= high: 
  
        mid = (high + low) // 2
  
        # Check if x is present at mid 
        if arr[mid] < x: 
            n+=1
            low = mid + 1
  
        # If x is greater, ignore left half 
        elif arr[mid] > x: 
            n+=1
            high = mid - 1
  
        # If x is smaller, ignore right half 
        else: 
            n+=1
            return mid, n 
  
    # If we reach here, then the element was not present 
    return -1
  

start = timeit.timeit()

arr = []
for i in range(1000000):
    arr.append(i)

ci = []
ai = []
for i in range(100000):
    ci.append("c"+str(i))
    ai.append(random.randrange(2,1000001))

# Test array 
n_tot = 0 
x = 10
min_p=""
min = 60
for i in range(len(ci)):
    x, n = binary_search(arr,ai[i])
    n_tot += n
    if x < min:
        min = x
        min_p=ci[i]

print("Vaccine " + min_p + " destroys COVID-19 with "+ str(min) + " doses, with "+str(n_tot)+" tests.")

end = timeit.timeit()
print(end-start)