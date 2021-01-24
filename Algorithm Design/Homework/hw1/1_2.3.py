# A Dynamic Programming based Python 
# program for LPS problem Returns the length 
# of the longest palindromic subsequence in seq 
def lps(str): 
	n = len(str) 
	max_p = []
	# Create a table to store results of subproblems 
	L = [[0 for x in range(n)] for x in range(n)] 
	cur=""
	r = str[::-1]
	# Strings of length 1 are palindrome of length 1 
	for i in range(n): 
		L[i][i] = 1


	for cl in range(2, n+1): 
		for i in range(n-cl+1): 
			j = i+cl-1

			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
				if cur == "":
					cur = str[i:i+cl]
				elif cur != "" and cur in str[0:i]:
					cur = cur + str[i:i+cl]  
				elif cur != "" and cur in str[i:len(str)-1]:
					cur = str[i:i+cl] + cur
				else:
					cur = str[0] + cur + str[len(str)-1]
				#print(cur)

			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
				if cur == "":
					cur = str[i:i+cl]
				elif cur != "" and cl == n:
					cur = str[0] + cur + str[len(str)-1]
				elif cur != "" and cur in str[0:i]:
					cur = cur + str[i:i+cl]  
				elif cur != "" and cur in str[i:len(str)-1]:
					cur = str[i:i+cl] + cur
				#print(cur)
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]); 

	return L,cur

# Driver program to test above functions 
seq = "BBABCBCAB"
print(seq)
n = len(seq)
l,p = lps(seq) 
print(p)
for i in range(n): 
	print(l[i]) 

# This code is contributed by Bhavya Jain 
