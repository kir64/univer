import time


flag = False


def timer(func):
	def wrapper(*args):
		time1 = time.time()
		func(*args)
		time2 = time.time()
	return time2 - time1


def standard(x):
	if set(x) is not {0}:
		x = list(map(int, ''.join(map(str, x)).rstrip('0')))
	if x == []:
		x = [0]
	return x


def mul(u, v):
	w = [0] * (len(u) + len(v) + 1)
	k = 0
	if (len(u) < len(v) or len(v) == len(u) and v > u):
		u, v = v.copy(), u.copy()
	u.append(0)


	for i in range(len(v)):
		for j in range(len(u)):
			tmp = u[j] * v[i] + w[j + i] + k
			w[j+i] = tmp % 10
			k = tmp // 10	

	return standard(w)


def dif(u, v):
	global flag
	m = max(len(u), len(v))
	u = standard(u)
	v = standard(v)

	
	u.reverse()
	v.reverse()
	if (len(v) > len(u) or len(v) == len(u) and v > u):
		u, v = v, u
		flag = True
	u.reverse()
	v.reverse()

	if (len(v) < len(u)):
		r = len(u) - len(v)
		for _ in range(r):
			v.append(0)
	
	w, k = [], 0
	for i in range(len(u)):
		w.append((u[i] - v[i] + k + 10) % 10)
		k = int((u[i] - v[i] + k - 9) / 10)
	
	for _ in range(m):
		w.append(0)
	return w


def add(u, v):
	m = max(len(u), len(v))
	u = standard(u)
	v = standard(v)
	if len(v) > len(u):
		u, v = v.copy(), u.copy()

	w, k = [], 0
	for _ in range(len(u) - len(v)):
		v.append(0)
	for i in range(len(u)):
		tmp = u[i] + v[i] + k
		w.append(tmp % 10)
		k = tmp // 10

	for _ in range(m):
		w.append(0)
	
	return w


def divmod(x, y):
	global flag
	u, v = [int(i) for i in x.lstrip('0')], [int(i) for i in y.lstrip('0')]
	u.reverse()
	v.reverse()
	w = [0] * (len(u) + 1)
	ans_div = [0] * (len(u))
	cur, ost = 0, 0


	if len(v) == 1:
		for i in range(len(u)-1, -1, -1):
			cur = 10 * ost + u[i]
			w[i] = cur // v[0]
			ost = cur % v[0]
		w = standard(w)
		
		return ''.join(map(str, reversed(w))), ost
	else:
		m = len(u) - len(v)
		n = 10 // (v[len(v) - 1] + 1)
		d = [n]
		u = mul(u, d)
		v = mul(v, d)


		if (m + len(v) > len(u) - 1):
			u.append(0)
		
		for i in range(m, -1, -1):
			tmp = u[i + len(v)] * 10 + u[i + len(v) - 1]
			q = int(tmp / v[len(v) - 1])
			r = tmp % v[len(v) - 1]

		
			while r < 10:
				if q == 10 or q * v[len(v) - 2] > 10 * r + u[i + len(v) - 2]:
					q -= 1
				r += v[len(v) - 1]
			
			
			Q = [q]
			u_new = [0] * (len(v) + 1)
			differ = [0] * (len(v) + 1)
			
			for j in range(i + len(v), i-1, -1):
				u_new[j - i] = u[j]
				
			step = [0] * (len(v) + 1) + [1]
			
			
			t_mul = mul(Q, v)
			t_dif = dif(u_new, t_mul)
			differ = dif(u_new, mul(Q, v))

			if flag:
				differ = dif(step, differ)
			ans_div[i] = q

			if flag:
				ans_div[i] -= 1
				differ = add(v, differ)
				flag = False

			for j in range(i + len(v), i-1, -1):
				u[j] = differ[j - i]
			

		
		ans_div = standard(ans_div)
		ans_div.reverse()

		u2 = [u[i] for i in range(len(v) - 1, -1, -1)]
		u2.reverse()

		w2 = [0] * len(u2)
		for i in range(len(u2) - 1, -1, -1):
			cur = 10 * ost + u2[i]
			w2[i] = cur // d[0]
			ost = cur % d[0]
		
		w2 = standard(w2)
		w2.reverse()

	return ''.join(map(str, ans_div)), ''.join(map(str, w2))


def check(x, y):
	if x[0] == '-' or y[0] == '-' or not x.isdigit() or not y.isdigit():
		return False
	return True


print('Enter x and y:')
x, y = input(), input()


if not check(x, y):
	print('Input error')
elif set(y) == {'0'}:
	print('Zero division')
elif set(x) == {'0'}:
	print(f'Div = 0, mod = 0')
else:
	ans = divmod(x, y)
	print(f'Div = {ans[0]}, mod = {ans[1]}')
