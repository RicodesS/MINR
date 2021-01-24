import numpy as np

def lps(s): 
	n = len(s) 

	# Create a table to store results of subproblems 
	T = np.zeros((n,n))
	print(T)
	max_p = ""
	# Strings of length 1 are palindrome of length 1 
	for i in range(n):
		T[i][i] = 1
	print(T)

	l = 2
	i = 0 
	for l in range(2, n+1):		
		for i in range(n-l+1):
			j = i+l-1
			if l == 2 and s[i] == s[j]:
				T[i][j] = 2
				max_p += s[i+1]
			elif s[i] == s[j]:
				T[i][j] = T[i+1][j-1] + 2
				max_p += s[j-1]
			else:
				T[i][j] = max(T[i+1][j],T[i][j-1])
			print(T)
			
		

	print(T)
	return max_p

# Driver program to test above functions 
seq = "agbdba"
 
print("The LPS is: " + lps(seq))

# This code is contributed by Bhavya Jain 
