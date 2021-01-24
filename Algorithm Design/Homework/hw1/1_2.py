alla fine sono riuscito a risolvere ma senza dp, uso sempre la matrice 
per ogni lettera itero a sinistra e ogni volta che raggiungo il margine 
sinistro aumento di 1 la scansione sul lato destro della stringa perciò 
il costo dovrebbe comunque essere cubico.


def pal(s):
	max_l = 1
	start = 0
	n = len(s)
	for i in range(2,n):
		for j in range(0,n-i):
			x = s[j:j+i]
			print(x)
			y = x[::-1]
			print(y)
			if y in s[j+i:n]:
				print("s: %s"%s[j+i:n])
				max_l = i
				print("max_l: %d"%max_l)
				start = j
				print("start: %d" %start)
	
	return max_l, start

def main():

	s = "abcdcsba"
	l, start = pal(s)
	print(l)
	print(s[start: start+l])

main()