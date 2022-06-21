f = open("input.txt", 'r')
txt = f.readlines()

alph = 'abcdefghijklmnopqrstuvwxyz'
n = alph.find(input()) + 1
v = [(i * n) % 26 for i in range(1, 27)]
tmp = ''.join([alph[i] for i in v])

def hlp(txt, tmp):
	d = {alph[i] : i+1 for i in range(26)}
	ans = ''
	for i in range(len(txt)):
		for j in range(len(txt[i])):
			ans += tmp[d[txt[i][j]]]

if (n % 2):
	print('Wrong input')
else:
	print(v)
	print(tmp)
	hlp(txt, tmp)
	ans = ''.join([str(i) for i in tmp])
	f = open('output.txt', 'w')
	f.write(ans)
