import numpy as np

def longestpal(s):
	n = len(s)
	M = np.zeros((n,n))

	max_l = 1
	for i in range(0,len(s)-1):
		M[i][i] = 1
		if s[i] == s[i+1]:
			M[i][i+1] = 1
			beg = i 
			max_l = 2

	i = 0
	for l in range(3,n+1):
		for i in range(0,n-l+1):
			j = i+l-1
			if M[i+1][j-1] == 1 and s[i] == s[j]:
				M[i][j] = 1
				
				if l > max_l: 
					beg = i
					max_l = l 
	
	return max_l, beg

def main():

	s = "abbag"
	l, beg = longestpal(s)
	print(s[beg: beg+l])

main()
