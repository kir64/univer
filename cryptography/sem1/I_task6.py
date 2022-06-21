import string

alph = string.ascii_lowercase
tab = '\n\n'

def encrypt(txt, key):
	ans = ''
	txt = txt.lower()
	for i in range(len(txt)):
		x = (alph.find(txt[i]) + alph.find(key[i % len(key)])) % 26
		ans += alph[x]
	return ans.upper()

def decrypt(txt, key):
	ans = ''
	txt = txt.lower()
	for i in range(len(txt)):
		x = (26 + alph.find(txt[i]) - alph.find(key[i % len(key)])) % 26
		ans += alph[x]
	return ans.lower()

with open('input.txt', 'r') as rf:
	txt = rf.read()
	key1 = alph[:12]
	key2 = alph[:22]
	key12 = ''
	for i in range(len(txt)):
		x = (alph.find(key1[i % len(key1)]) + alph.find(key2[i % len(key2)])) % 26
		key12 += alph[x]
	print(key12)

with open('output.txt', 'w') as wf:
	print(txt + '\n', file = wf)
	
	E1 = encrypt(txt, key1)
	E2 = encrypt(txt, key2)
	E1E2 = encrypt(E1, key2)
	E12 = encrypt(txt, key12)

	print(E1, E2, E1E2, sep = tab, file = wf)
	print(E12 + '\n', file = wf)

	e12 = decrypt(E12, key2)
	e1 = decrypt(e12, key1)

	print(e12, e1, sep = tab, file = wf)
