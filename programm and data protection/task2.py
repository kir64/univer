import os

def hash_calc(file_path):
	with open(file_path, 'rb') as txt:
		sum, chunk = 0, txt.read(4)
		while chunk:
			sum ^= int.from_bytes(chunk, "little", signed=True)
			chunk = txt.read(4)
	return sum


file_name = 'team1.py'
file_path = os.path.abspath(file_name)
file_copy_path1 = os.path.abspath('tmp.txt')
file_copy_path2 = os.path.abspath('output.txt')

with open(file_name, 'r') as rf:
	line = rf.read()
	with open('tmp.txt', 'w') as wf1:
		print(line, file=wf1)

hash = hash_calc(file_copy_path1)
cur_hash = hash_calc(file_copy_path2)
print('No invasion.') if hash == cur_hash else print('Invasion!')

with open('output.txt', 'w') as wf2:
	print(line, file=wf2)
