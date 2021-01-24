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
            n += 1
            low = mid + 1
  
        # If x is greater, ignore left half 
        elif arr[mid] > x: 
            n += 1
            high = mid - 1
  
        # If x is smaller, ignore right half 
        else: 
            n += 1
            return mid,n 
  
    # If we reach here, then the element was not present 
    return -1
  

start = timeit.timeit()

arr = []
for i in range(1000000):
    arr.append(i)
# Test array 
ci = []
ai = []
for i in range(100000):
    ci.append("c"+str(i))
    ai.append(random.randrange(2,1000001))

x = ""
y = 0

min = 60
i = random.randrange(-1,len(ci))
min_c = ci[i]
min_a,n = binary_search(arr,ai[i])
i = len(ai)-1
while len(ci)>1:
    if(len(ci) == 1):
        break
    if min_a <= ai[i] and ci[i] != min_c:
        x =ci.pop()
        y =ai.pop()
        i = len(ci) -1
    elif min_a > ai[i]:
        min_a = ai[i]
        min_c = ci[i]
        i = len(ci) -1
    elif ci[i] == min_c:
        i -= 1
    n += 1

print("Vaccine " + min_c + " destroys COVID-19 with "+ str(min_a) + " doses, in "+str(n)+" tests.")

end = timeit.timeit()
print(end-start)
