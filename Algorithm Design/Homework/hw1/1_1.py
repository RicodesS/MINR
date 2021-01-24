def max_palindhrome(w, n,subs):
	max_length = 0
	max_pal = ""
	x = len(subs)
	
	for j in range(0, x):
		y = len(subs[j])
		for i in range(0, y):
			if (n - y) > 0:
				if subs[j][i] == subs[j][y-(i+1)]:
					continue
				else:
					break
			if y > max_length:
				max_length = y
				max_pal = subs[j]
				

	return max_pal

def main():
	s = "raddafdar"

	subs = [s[i: j] for i in range(len(s)) 
          for j in range(i + 1, len(s) + 1)] 

	print(max_palindhrome(s,len(s),subs))

main()