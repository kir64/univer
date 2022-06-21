import math

def H(s):
	ans = 0
	d = {i:s.count(i) for i in s}
	for k in d.keys():
		p = d[k] / len(s)
		ans += p * math.log2(p)
	return -ans

with open('input.txt', 'r') as rf:
	txt = rf.read()
	
s = ''.join(txt.split('\n'))
print(f'{H(s):.5f}')
