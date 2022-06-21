import itertools
import textwrap

def find_permutation(tmp_a, tmp_b):
	lst = []
	tmp = range(len(tmp_a[0]))
	all_pers_lst = itertools.permutations(tmp)
	for per in all_pers_lst:
		cur_per = ''.join([tmp_a[0][i] for i in per])
		if cur_per == tmp_b[0]:
			lst.append(per)
	return lst

def check(a, b):
	if sorted(a) != sorted(b):
		return None
	for chunks in [i for i in range(2, len(a)) if len(a) % i == 0]:
		tmp_a = textwrap.wrap(a, chunks)
		tmp_b = textwrap.wrap(b, chunks)
		wrap_check = all([sorted(tmp_a[chunk]) == sorted(tmp_b[chunk]) for chunk in range(len(tmp_a))])
		if not wrap_check:
			continue
		lst = find_permutation(tmp_a, tmp_b)
		for per in lst:
			ans = []
			for chunk in range(len(tmp_a)):
				cur_per = ''.join([tmp_a[chunk][i] for i in per])
				if cur_per == tmp_b[chunk]:
					ans.append(cur_per == tmp_b[chunk])
				else:
					break
			if all(ans) and len(ans) == len(tmp_a):
				return len(tmp_a[chunk])

	return len(a)

with open('input.txt', 'r') as rf:
	a, b = [rf.readline().strip() for _ in range(2)]

with open('output.txt', 'w') as wf:
	print(a, b, sep = '\n')
	print(check(a, b))
