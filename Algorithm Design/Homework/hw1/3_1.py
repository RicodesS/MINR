def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i].req < right[j].req:
              # The value from the left half has been used
              myList[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

class Project: 
	def __init__(self, name, req, profit): 
		self.name = name 
		self.req = req 
		self.profit = profit 


def bestSuc(C, lst):
	best_p = None
	best = 0

	for i in range(len(lst)-1):
		if(lst[i].req <= C):
			if((lst[i].profit - lst[i].req) > best):
				best_p = lst[i]
				best = i
			elif((lst[i].profit - lst[i].req) == best):
				if(lst[i].req > best_p.req):
					best = i
					best_p = lst[i]
	return best,best_p.profit

def compute(C,opt,lst,n):
	print(len(lst))
	if len(lst) == 0:
		return 
	elif lst[0].req <= C:
		lst.pop(0)
		opt = opt.append(lst[0])
		compute(C+lst[0].profit, opt, lst, n)
	else:
		compute(C, opt, lst[1:], n)
	exit()
def main():

	N = 100

	p1 = Project("p1", 10, 2)
	p2 = Project("p2", 6, -2)
	p3 = Project("p3", 2, 6)
	p4 = Project("p4", 10, 7)
	p5 = Project("p5", 4, 1)
	p6 = Project("p6", 7, -3)

	lst = [p1,p2,p3,p4,p5,p6]
	mergeSort(lst)
	C = 5+N
	suc,b = bestSuc(C,lst)
	C += b
	opt = []
	opt.append(lst[suc])
	#print(len(opt))
	lst.pop(suc)
	n = len(lst)
	opt = compute(C,opt,lst,n)

	#print(opt)

main()
