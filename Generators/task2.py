import re
import sys
import math

def alg1(): #стандартное раавномерное
	s = input()
	m = int(s[3:len(s)])
	
	with open('output.txt', 'w') as wf:
		for line in sys.stdin:
			t = int(line)
			if t >= m:
				tmp = str((m-1) / m)
				if len(tmp) > 5:
					hlp = tmp[2:5]
				else:
					ans = float(tmp)
			else:
				tmp = str(t / m)
				if len(tmp) > 5:
					hlp = tmp[2:5]
					ans = 0 if (hlp == '000') else float('0.' + hlp)
				else:
					ans = 0 if (tmp == '0.0') else float(tmp)
			print(ans, file=wf)
#alg1()


def alg2(): #равномерное
	pars = re.findall(r'\d+', input())
	m, a, b = map(int, pars)
	
	with open('output.txt', 'w') as wf:
		for line in sys.stdin:
			tmp = str(a + int(line) / m * b)
			d = ''.join(re.findall(r'\.\d+', tmp))
			c = ''.join(re.findall(r'\d+[.]', tmp)).rstrip('.')
			
			if (d == '.0'):
				ans = int(c)
			else:
				if len(d) < 5:
					ans = float(c + d)
				else:
					ans = float(c + d[0:4])
			print(ans, file=wf)
#alg2()

def alg3(): #треугольное
	X = []
	m = input().split(' ')
	m = [float(x[3:]) for x in m]
	for line in sys.stdin:
		for var in line.split():
			X.append(float(var))
	
	with open('output.txt', 'w') as wf:
		for i in range(0, len(X), 2):
			y = m[1] + m[2] * (X[i] / m[0] + X[i + 1] / m[0] - 1)
			print(y, file=wf)
alg3()


def alg4(): #экспоненциальное
	def ex(x, a, b, m):
		return a - b * math.log(x / m)

	pars = re.findall(r'\d+', input())
	m, a, b = map(int, pars)

	v, i = [], 0
	flag = False
	with open('output.txt', 'w') as wf:
		for line in sys.stdin:
			t = int(line)
			i += 1
			v.append(int(line))

			if i != 2:
				continue
			else:
				tmp = str(ex(t, a, b, m))
				if (tmp[0] == '-'):
					flag = True
				d = ''.join(re.findall(r'\.\d+',tmp))
				c = ''.join(re.findall(r'\d+[.]' ,tmp)).rstrip('.')
				if d == '.0':
					ans = int(c)
				else:
					if len(d) < 5:
						ans = float(c + d)
						if flag:
							ans *= -1
					else:
						ans = float(c + d[:4])
						if flag:
							ans *= -1
					
				print(ans, file=wf)
				v, i = [], 0
				flag = False
#alg4()

def alg5(): #нормальное
	def nr(x1, x2, a, b, m):
		y1 = a + b * math.sqrt(math.fabs(-2 * math.log(1 - x1 / m))) * math.cos(2*math.pi * x2 / m)
		y2 = a + b * math.sqrt(math.fabs(-2 * math.log(1 - x1 / m))) * math.sin(2*math.pi * x2 / m)
		return [y1, y2]

	pars = re.findall(r'\d+', input())
	m, a, b = map(int, pars)
	v, i = [], 0

	with open('output.txt', 'w') as wf:
		for line in sys.stdin:   
			i += 1
			v.append(int(line))
			if (i != 2):
				continue
			else:
				tmp = list(map(str, nr(v[0], v[1], a, b, m)))
				for key in tmp:
					flag = False
					if (key[0] == '-'):
						flag = True
					c = ''.join(re.findall(r'\d+[.]',key)).rstrip('.')
					d = ''.join(re.findall(r'\.\d+', key))
					if (d == '.0'):
						ans = int(c)
					else:
						if len(d) < 5:
							ans = float(c + d)
							if flag:
								ans *= -1
						else:
							ans = float(c + d[:4])
							if flag:
								ans *= -1         
					print(ans, file=wf)
			v, i = [], 0
#alg5()

def alg6(): # логнормальное
	def nr(x1, x2, a, b, m):
		y1 = a + b * math.sqrt(math.fabs(-2 * math.log(1 - x1 / m))) * math.cos(2 * math.pi * x2 / m)
		y2 = a + b * math.sqrt(math.fabs(-2 * math.log(1 - x1 / m))) * math.sin(2 * math.pi * x2 / m)
		return [y1, y2]

	def lnr(x1, x2, a, b):
		tmp = nr(x1, x2, 0, 1, m)
		y1 = a + math.exp(b - tmp[0])
		y2 = a + math.exp(b - tmp[1])
		return [y1, y2]

	pars = re.findall(r'[-]?\d+', input())
	m, a, b = map(int, pars)
	v, i = [], 0
	flag = False

	with open('output.txt', 'w') as wf:
		for line in sys.stdin:
			i += 1
			v.append(int(line))
			if (i != 2):
				continue
			else:
				for key in list(map(str, lnr(v[0], v[1], a, b))):
					flag = False
					if (key[0] == "-"):
						flag = True
					c = ''.join(re.findall(r'\d+[.]', key)).rstrip('.')
					d = ''.join(re.findall(r'\.\d+', key))
					if (d == '.0'):
						ans = int(c)
					else:
						if len(d) < 5:
							ans = float(c + d)
							if flag:
								ans *= -1
						else:
							ans = float(c + d[:4])
							if flag:
								ans *= -1
					print(ans, file=wf)
			v, i = [], 0
#alg6()

def alg7(): #логистическое
	def logistic(x, a, b, m):
		u = x / m
		return a + b * math.log(u / (1 - u))    

	pars = re.findall(r'[-]?\d+', input())
	m, a, b = map(int, pars)
	flag = False
	
	with open('output.txt', 'w') as wf:
		for line in sys.stdin:
			tmp = str(logistic(int(line), a, b, m))
			c = ''.join(re.findall(r'[-]?\d+[.]' ,tmp)).rstrip('.')
			d = ''.join(re.findall(r'\.\d+', tmp))
			if (d == '.0'):
				ans = int(c)
			else:
				if len(d) < 5:
					ans = float(c + d)
					if flag:
						ans *= -1
				else:
					ans = float(c + d[:4])
					if flag:
						ans *= -1
			print(ans, file=wf)
#alg7()

def alg8(): # биномиальное
	def binominal(x, a, b, m):
		u = x / m
		s, k, y = 0, 0, 0

		for k in range(b):
			cb = math.factorial(b) / (math.factorial(k) * math.factorial(b - k))
			s += cb * (a ** k) * ((1 - a ) ** (b - k))
			if s > u:
				y = k
				break
			y = b
			k += 1
		return y

	pars = re.findall(r'\d+[.]?\d?', input())
	m, b = int(pars[0]), int(pars[2])

	if (pars[1].find('.')):
		a = float(pars[1])
	else:
		a = int(pars[1])

	with open('output.txt', 'w') as wf:
		for line in sys.stdin:
		   print(str(binominal(int(line), a, b, m)), file=wf)
#alg8()

def alg9(): # гамма распределение
	def nr(x1, x2, a, b, m):
		y1 = a + b * math.sqrt(math.fabs(-2 * math.log(1- x1 / m))) * math.cos(2 * math.pi * x2 / m)
		y2 = a + b * math.sqrt(math.fabs(-2 * math.log(1- x1 / m))) * math.sin(2 * math.pi * x2 / m)
		return [y1, y2]

	def gamma(x, a, b, c, flag, m):
		y, z1, z2, k = 0, 0, 0, 0
		ans = []
		if not flag:
			mul = 1
			for key in x:
				mul *= (1 - key / m)
			y = a - b * math.log(math.fabs(mul))
			ans.append(y)
		else:
			k = int(c - 0.5)
			mul = 1
			z1, z2 = nr(x[0], x[1], 0, 1, m)
			for key in range(2, k + 2):
				mul *= (1 - x[key] / m)
			y1 = a + b * ( ((z1 ** 2) / 2)  - math.log(mul))
			mul = 1
			for key in range(k + 2, 2 * k + 2):
				mul *= (1 - x[key] / m)
			y2 = a + b * (((z2 ** 2) / 2)  - math.log(mul))
			ans.append(y1)
			ans.append(y2)
		return ans

	flag = False
	pars = re.findall(r'[-]?\d+[.]?\d?', input())
	m = int(pars[0])

	if (pars[1].find('.') != -1):
		a = float(pars[1])
	else:
		a = int(pars[1])
	if (pars[2].find('.')  != -1):
		b = float(pars[2])
	else:
		b = int(pars[2])

	if (pars[3].find('.')  != -1):
		c = float(pars[3])
		flag = True
	else:
		c = int(pars[3])

	v, i = [], 0
	with open('output.txt', 'w') as wf:
		if flag:
			edge = int(c - 0.5)
			for line in sys.stdin:
				t = int(line)
				i += 1
				v.append(t)
				if (i != (edge * 2) + 2):
					continue
				else:
					i = 0
					for key in gamma(v, a, b, c, flag, m):
						key = str(key)
						pars_c = ''.join(re.findall(r'[-]?\d+[.]', key)).rstrip('.')
						pars_d = ''.join(re.findall(r'\.\d+', key))

						if (pars_d == '.0'):
							ans = int(pars_c)
						else:
							if len(pars_d) < 5:
								ans = float(pars_c + pars_d)
							else:
								ans = float(pars_c + pars_d[:4])
						print(ans, file=wf)
					v = []
		else:
			if not flag:
				edge = c 
				for line in sys.stdin:
					i += 1
					v.append(int(line))
					if(i != c):
						continue
					else:
						i = 0
						for key in gamma(v, a, b, c, flag, m):
							key = str(key)
							pars_c = ''.join(re.findall(r'[-]?\d+[.]', key)).rstrip('.')
							pars_d = ''.join(re.findall(r'\.\d+', key))
							if (pars_d == '.0'):
								ans = int(pars_c)
							else:
								if len(pars_d) < 5:
									ans = float(pars_c + pars_d)
								else:
									ans = float(pars_c + pars_d[:4])
							print(ans, file=wf)
						v = []
#alg9()
