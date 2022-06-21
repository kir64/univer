from array import *


def Lin_Gen():
	with open('output.txt', 'w') as wf:
		n, a, c, m, x = map(int, input().split())
		while n > 0:
			n -= 1
			x = ((a * x) + c) % m
			print(x, file=wf)
#Lin_Gen()

def Add_Gen():
	n, s = map(int, input().split())
	a, x = array('i', []), array('l', [])
	i = 0
	while i < s:
		ai , xi = map(int, input().split())
		a.append(ai)
		x.append(xi)
		i += 1
	c, m = int(input()), int(input())
	i = 0
	with open('output.txt', 'w') as wf:
		while i < n :
			ans, j = 0, 0
			while j < s :
				ans += (a[j] * x[i+j])
				j +=1 
			ans = (ans + c) % m
			print (ans, file=wf)
			x.append(ans)
			i += 1
#Add_Gen()

def RSLOS_Gen():
	a1, a2, a3 = list(map(int, input().split()))
	tmp = list(map(int, input().split()))
	a4 = tmp[0]

	j = [tmp[i + 1] for i in range(a4)]
	x = list(map(int, list(bin(int(input()))[2:])))
	for _ in range(a2 - len(x)):
		x.insert(0, 0)
	for i in range(a2 * (a1+ 1) + a3):
		x_tmp = 0
		for k in range(a4):
			x_tmp += x[i + j[k] - 1]
		x.append(x_tmp % 2)
	with open('output.txt', 'w') as wf:
		for i in range(a1):
			ans = ''
			for j in range(a3):
				ans += str(x[a2 + i * a3 + j])
			print(int(ans, 2), file=wf)
#RSLOS_Gen()

def FiveParam_Gen():
	a1, a2, a3, a4, a5, a6, y = list(map(int, input().split()))
	x = list(map(int, list(bin(y)[2:])))
	for _ in range(a2 - len(x)):
		x.insert(0, 0)
	for i in range(a2 * (a1 + 1) + a3):
		tmp = x[i + a4] + x[i + a5] + x[i + a6] + x[i]
		x.append(tmp % 2)
	with open('output.txt', 'w') as wf:
		for i in range(a1):
			ans = ''
			for j in range(a3):
				ans += str(x[a2 + i * a3 + j])
			print(int(ans, 2), file=wf)
#FiveParam_Gen()

def RSA_Gen():
	c, n, e, x, w, l = list(map(int, input().split()))
	s, cnt = '', 0
	with open('output.txt', 'w') as wf:
		while cnt != c:
			x = pow(x, e, n)
			a = bin(x)[2:]
			if len(a) < w:
				a = '0' * (w - len(a)) + a
			s += a[-w:]
			while len(s) >= l:
				print(int(str(s[:l]), 2), file=wf)
				s = s[l:]
				cnt += 1
#RSA_Gen()

def BBS_Gen():
	a1, a2, a3, a4 = list(map(int, input().split()))
	with open('output.txt', 'w') as wf:
		for i in range(a1):
			s = ''
			for j in range(a4):
				a3 = pow(a3, 2, a2)
				s += bin(a3)[-1]
			print(int(s, 2), file=wf)
BBS_Gen()

def RC4_Gen():
	a1 = input().split()
	a2, a3 = int(a1[0]), int(a1[1])
	k = []
	for i in range(16):
		k += [int(i) for i in input().split()]
	s = list(range(256))
	j = 0
	for i in range(256):
		j = (j + s[i] + k[i]) % 256
		s[i], s[j] = s[j], s[i]

	i, j, y = 0, 0, ''
	with open('output.txt', 'w') as wf:
		while a2 > 0:
			i = (i + 1) % 256
			j = (j + s[i]) % 256
			s[i], s[j] = s[j], s[i]
			x = bin(s[(s[i] + s[j]) % 256])[2:]
			if len(x) < 8:
				 x = '0' * (8 - len(x)) + x
			y += x[-8:]
			while len(y) >= a3 and a2 > 0:
				print(int(y[:a3], 2), file=wf)
				y = y[a3:]
				a2 -= 1
#RC4_Gen()

def nRSLOS_Gen():
	def bit_string(Y, p):
		p -= 1
		ans = []
		while p >= 0:
			tmp = pow(2, p)
			if Y >= tmp:
				Y -= tmp
				ans.append(1)
			else:
				ans.append(0)
			p -= 1
		return ans

	c, k, w = map(int, input().split())
	X, J, P, L = [], [], [], []

	for i in range(k):
		tmp1 = input().split(' ')
		tmp2 = input().split(' ')
		
		P.append(tmp1[0])
		L.append(max(int(P[i]), w))
		X.append(bit_string(int(tmp1[1]), L[i]))
		J.append(tmp2[1:])
	
	tmp3 = input().split(' ')
	q = int(tmp3[0])
	
	Jq = [int(x, 2) for x in tmp3[1:]]
	
	with open('output.txt', 'w') as wf:
		for cycle in range(c):
			for jj in range(k):
				X_0 = X[jj]
				A_0 = [0 for i in range(1, int(P[jj]) + 1)]
				for i in range(len(A_0)):
					for j in J[jj]:
						if (i + 1) == int(j):
							A_0[i] = 1
							break
				new_X = X[jj]
				i = 0
				while i < w:
					Xjj = []
					tmp = 0
					for ii in range(len(new_X) - int(P[jj]), len(new_X)):
						Xjj.append(A_0[tmp] * new_X[ii])
						tmp += 1
					x = Xjj[0] ^ Xjj[1]
					for ii in range(2, int(P[jj])):
						x ^= Xjj[ii]
					new_X.append(x)
					if len(new_X) > L[jj]:
						new_X = new_X[::-1]
						new_X.pop()
						new_X = new_X[::-1]
					i += 1
				X[jj] = new_X
			Y = 0
			for i in range(w-1, -1, -1):
				tmp = 0
				for ii in range(q):
					tmp2 = 1
					for iii in range(k):
						if Jq[ii] & (1<< iii) != 0:
							tmp2 = (tmp2 * X[k - 1 - iii][w-1 - i]) % 2
					tmp = (tmp ^ tmp2) % 2
				if tmp == 1:
					Y |= 1 << i
			print(Y, file=wf)
#nRSLOS_Gen()


def MersenVortex_Gen():
	n, p, w, r, q, a = int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
	u, s, t, l, b, c = int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
	x =  list(map(int, input().split()))
	rez = []

	def form_srt(m, l1, n1, l2, n2):
		for i in range(l1):
			m.append(n1)
		for i in range(l2):
			m.append(n2)
		return m

	tmp1 = ''.join(form_srt([], w-r, '1', r, '0'))
	tmp2 = ''.join(form_srt([], w-r, '0', r, '1'))
	
	mask1 = int(tmp1, 2)
	mask2 = int(tmp2, 2)
	
	with open('output.txt', 'w') as wf:
		for i in range(n):
			Y = x[i] & mask1  | (x[i+1]) & mask2
			if not Y % 2:
				 tempx = (x[i+q] % 2**w) ^ (Y >> 1) ^ 0
			else:
				 tempx = (x[i+q] % 2**w) ^ (Y >> 1) ^ a
			Y = tempx
			Y ^= Y >> u
			Y ^= (Y << s) & b
			Y ^= (Y << t) & c
			Z = Y ^ (Y >> l)
			x.append(tempx)
			print(Z, file=wf)
			rez.append(Z)
#MersenVortex_Gen()
